import numpy as np
from collections import namedtuple


class LinearFeedbackShiftRegister:
    def __init__(self, setup=None,
                 config=None, init_state=None, bit_size=8, xor_bit=-1):
        if not setup is None:
            # print("my setup: ", setup)
            try:
                config = setup['config']
                init_state = setup['init_state']
                bit_size = setup['bit_size']
                xor_bit = setup['xor_bit']

            except TypeError as te:
                print("TypeError: ", te)

            except NameError as ne:
                print("Name error: ", ne)

        self._bit_size = bit_size
        self._max_num = 2**bit_size - 1

        if (not init_state is None) and init_state >= 0:
            try:
                init_state = int(init_state)
            except ValueError:
                init_state = int(init_state, 2)

            self.state = init_state % (self._max_num + 1)
        else:
            self.state = int(np.random.random()*(self._max_num - 1) + 1)

        if (not config is None) and config != 0:
            self.config = (config % (self._max_num + 1))

        else:
            self.config = int(np.random.random()*(self._max_num - 1) + 1)
        if xor_bit > 1 or xor_bit < 0:
            self.xor_bit = int(np.random.random()*2)
        else:
            self.xor_bit = xor_bit

        self.config = bin(self.config)
        self.last_bit = 0

    def __repr__(self):
        name = "LFSRegister"
        Point = namedtuple(name, ['config', 'bit_size', 'state'])
        return str(Point(f'0b{self.config[2:]:>08}', self._bit_size, self.state))

    def next_step(self):
        bin_state = bin(self.state)[2:].rjust(self._bit_size, '0')
        bin_config = self.config[2:].rjust(self._bit_size, '0')

        new_val = self.xor_bit
        self.last_bit = self.state >> (self._bit_size - 1)
        for bit_id, bit in enumerate(bin_config):
            if bit == '1':
                new_val = new_val ^ int(bin_state[bit_id])

        self.state = ((self.state << 1) | new_val) & self._max_num
        return self.last_bit


class GeffeGenerator:
    default = {'bit_size': 16, 'config': 0, 'init_state': -1, 'xor_bit': 1}

    def __init__(self, reg1_setup=default, reg2_setup=default, reg3_setup=default):
        self.reg1 = LinearFeedbackShiftRegister(setup=reg1_setup)
        self.reg2 = LinearFeedbackShiftRegister(setup=reg2_setup)
        self.reg3 = LinearFeedbackShiftRegister(setup=reg3_setup)
        self.max_size = max(reg1_setup['bit_size'],
                            reg2_setup['bit_size'],
                            reg3_setup['bit_size'])
        self.last_bit = None

    def next(self):
        self.reg1.next_step()
        self.reg2.next_step()
        self.reg3.next_step()

        x1 = self.reg1.last_bit
        x2 = self.reg2.last_bit
        x3 = self.reg3.last_bit

        self.last_bit = (x1 & x2) | ((x2 ^ 1) & x3)
        return self.last_bit

    def get_state(self):
        state = []
        state.append(bin(self.reg1.state)[2:].rjust(self.reg1._bit_size, '0'))
        state.append(bin(self.reg2.state)[2:].rjust(self.reg2._bit_size, '0'))
        state.append(bin(self.reg3.state)[2:].rjust(self.reg3._bit_size, '0'))
        return state


class StopAndGoGenerator:
    default = {'bit_size': 16, 'config': 0, 'init_state': -1, 'xor_bit': 1}

    def __init__(self, reg1_setup=default, reg2_setup=default, reg3_setup=default):
        self.reg1 = LinearFeedbackShiftRegister(setup=reg1_setup)
        self.reg2 = LinearFeedbackShiftRegister(setup=reg2_setup)
        self.reg3 = LinearFeedbackShiftRegister(setup=reg3_setup)
        self.max_size = max(reg1_setup['bit_size'],
                            reg2_setup['bit_size'],
                            reg3_setup['bit_size'])
        self.last_bit = None
        self.clock_next = 0

    def next(self):
        self.reg1.next_step()
        self.clock_next = self.reg1.last_bit
        if self.clock_next == 1:
            self.reg2.next_step()
        elif self.clock_next == 0:
            self.reg3.next_step()
        else:
            raise ValueError("Clock is not in <1,2,3> values")

        x2 = self.reg2.last_bit
        x3 = self.reg3.last_bit

        self.last_bit = (x2+x3) % 2
        return self.last_bit

    def get_state(self):
        state = []
        state.append(bin(self.reg1.state)[2:].rjust(self.reg1._bit_size, '0'))
        state.append(bin(self.reg2.state)[2:].rjust(self.reg2._bit_size, '0'))
        state.append(bin(self.reg3.state)[2:].rjust(self.reg3._bit_size, '0'))
        return state


class ShrinkingGenerator:
    default = {'bit_size': 16, 'config': 0, 'init_state': -1, 'xor_bit': 1}

    def __init__(self, reg1_setup=default, reg2_setup=default):
        self.reg1 = LinearFeedbackShiftRegister(setup=reg1_setup)
        self.reg2 = LinearFeedbackShiftRegister(setup=reg2_setup)
        self.max_size = max(reg1_setup['bit_size'],
                            reg2_setup['bit_size'])
        self.last_bit = 0

    def next(self):
        self.reg1.next_step()
        self.reg2.next_step()

        if self.reg1.last_bit == 1:
            self.last_bit = self.reg2.last_bit

        return self.last_bit

    def get_state(self):
        state = []
        state.append(bin(self.reg1.state)[2:].rjust(self.reg1._bit_size, '0'))
        state.append(bin(self.reg2.state)[2:].rjust(self.reg2._bit_size, '0'))
        return state


class MonoBitTest:
    def __init__(self, stream):
        if len(stream) < 100:
            raise ValueError('Stream is too short')
        elif len(stream) != 20000:
            print("Error lenght:", len(stream))
            raise ValueError('Stream length must be 20.000')

        self._stream = stream
        self.count = self._stream.count('1')

    def run_test(self):
        return self.count > 9725 and self.count < 10275


class LongRunTest:
    def __init__(self, stream):
        if len(stream) < 100:
            raise ValueError('Stream is too short')
        elif len(stream) != 20000:
            print("Error lenght:", len(stream))
            raise ValueError('Stream length must be 20.000')

        self._stream = stream

    def run_test(self):
        val = 0
        current = None
        for letter in self._stream:
            if letter == current:
                val += 1
            else:
                current = letter
                val = 1

            if val > 26:
                return False
        return True


class PokerTest:
    def __init__(self, stream):
        if len(stream) < 100:
            raise ValueError('Stream is too short')
        elif len(stream) != 20000:
            print("Error lenght:", len(stream))
            raise ValueError('Stream length must be 20.000')
        self._stream = stream

    def run_test(self):
        combinations = {}
        for i in range(0, len(self._stream)-3, 4):
            pack = self._stream[i:i+4]
            combinations[pack] = 1 + combinations.get(pack, 0)

        epsilon = 0
        for key, value in combinations.items():
            epsilon += (value**2)
        x = ((16/5000)*epsilon)-5000

        return x > 2.16 and x < 46.17

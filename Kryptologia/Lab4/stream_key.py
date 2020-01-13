import numpy as np
from collections import namedtuple


class LinearFeedbackShiftRegister:
    def __init__(self, config=None, init_state=None, bit_size=8):
        self._bit_size = bit_size
        self._max_num = 2**bit_size - 1

        if (not init_state is None) and init_state != 0:
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
        # print("new config: ", bin(self.config)[2:].rjust(bit_size, '0'), self.config)
        self.config = bin(self.config)
        self.last_bit = 0

    def __repr__(self):
        name = "LFSRegister"
        Point = namedtuple(name, ['config', 'bit_size', 'state'])
        return str(Point(f'0b{self.config[2:]:>08}', self._bit_size, self.state))

    # def state(self):
    #     pass

    def next_step(self):
        bin_state = bin(self.state)[2:].rjust(self._bit_size, '0')
        bin_config = self.config[2:].rjust(self._bit_size, '0')

        new_val = 1
        self.last_bit = self.state >> (self._bit_size - 1)
        for bit_id, bit in enumerate(bin_config):
            if bit == '1':
                new_val = new_val ^ int(bin_state[bit_id])

        self.state = ((self.state << 1) | new_val) & self._max_num
        return self.last_bit


class GeffeGenerator:
    def __init__(self, config=None, init_state=None, bit_size=8):
        self._bit_size = bit_size

        self.reg1 = LinearFeedbackShiftRegister(
            config=config, init_state=init_state, bit_size=bit_size)
        self.reg2 = LinearFeedbackShiftRegister(
            config=config, init_state=init_state, bit_size=bit_size)
        self.reg3 = LinearFeedbackShiftRegister(
            config=config, init_state=init_state, bit_size=bit_size)
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
        state.append(bin(self.reg1.state)[2:].rjust(self._bit_size, '0'))
        state.append(bin(self.reg2.state)[2:].rjust(self._bit_size, '0'))
        state.append(bin(self.reg3.state)[2:].rjust(self._bit_size, '0'))
        return state


class StopAndGoGenerator:
    def __init__(self, config=None, init_state=None, bit_size=8):
        self._bit_size = bit_size
        self.reg1 = LinearFeedbackShiftRegister(
            config=config, init_state=init_state, bit_size=bit_size)
        self.reg2 = LinearFeedbackShiftRegister(
            config=config, init_state=init_state, bit_size=bit_size)
        self.reg3 = LinearFeedbackShiftRegister(
            config=config, init_state=init_state, bit_size=bit_size)
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

        # x1 = self.reg1.last_bit
        x2 = self.reg2.last_bit
        x3 = self.reg3.last_bit

        self.last_bit = (x2+x3) % 2
        return self.last_bit

    def get_state(self):
        state = []
        state.append(bin(self.reg1.state)[2:].rjust(self._bit_size, '0'))
        state.append(bin(self.reg2.state)[2:].rjust(self._bit_size, '0'))
        state.append(bin(self.reg3.state)[2:].rjust(self._bit_size, '0'))
        return state


class ShrinkingGenerator:
    def __init__(self, config=None, init_state=None, bit_size=8):
        self._bit_size = bit_size
        self.reg1 = LinearFeedbackShiftRegister(
            config=config, init_state=init_state, bit_size=bit_size)
        self.reg2 = LinearFeedbackShiftRegister(
            config=config, init_state=init_state, bit_size=bit_size)
        self.last_bit = 0

    def next(self):
        self.reg1.next_step()
        self.reg2.next_step()

        if self.reg1.last_bit == 1:
            self.last_bit = self.reg2.last_bit

        return self.last_bit

    def get_state(self):
        state = []
        state.append(bin(self.reg1.state)[2:].rjust(self._bit_size, '0'))
        state.append(bin(self.reg2.state)[2:].rjust(self._bit_size, '0'))
        return state


class MonoBitTest:
    def __init__(self, stream):
        if len(stream) < 100:
            raise ValueError('Stream is too short')
        elif len(stream) != 20000:
            raise ValueError('Stream length must be 20.000')

        self._stream = stream
        self.count = self._stream.count('1')

    def run_test(self):
        return self.count > 9725 and self.count < 10275



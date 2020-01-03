import numpy as np
from collections import namedtuple


class LinearFeedbackShiftRegister:
    def __init__(self, config=None, init_state=None, bit_size=8):
        self._bit_size = bit_size
        self._max_num = 2**bit_size - 1

        if init_state:
            self.state = init_state
        else:
            self.state = int(np.random.random()*(self._max_num - 1) + 1)

        if not (config is None):
            self.config = (config % (self._max_num + 1))

        else:
            self.config = int(np.random.random()*(self._max_num - 1) + 1)

        self.config = bin(self.config)

    def __repr__(self):
        name = "LFSRegister"
        Point = namedtuple(name, ['config', 'bit_size', 'state'])
        return str(Point(f'0b{self.config[2:]:>08}', self._bit_size, self.state))

    def state(self):
        pass

    def next_step(self):
        bin_state = bin(self.state)[2:].rjust(self._bit_size, '0')
        bin_config = self.config[2:].rjust(self._bit_size, '0')

        new_val = 1

        for bit_id, bit in enumerate(bin_config):
            if bit == '1':
                new_val = new_val ^ int(bin_state[bit_id])

        self.state = ((self.state << 1) | new_val) % (self._max_num + 1)


# class Polynomial:  # Wielomian, liczenie wartosci w punktach x
# 	def __init__(self, coeffs):
# 		self.coeffs = coeffs
# 		#print(f"New coeffs {self.coeffs}")

# 	def __repr__(self):
# 		txt = 'f(x) ='
# 		for i in range(len(self.coeffs)-1, 0, -1):
# 			txt += f' {self.coeffs[i]} *x^{i} +'
# 		txt = txt[:-2] + f' + {self.coeffs[0]}'
# 		return txt

# 	def __call__(self, x):
# 		y = 0
# 		for i, coeff in enumerate(self.coeffs):
# 			y += x**i * coeff
# 		return y, f'f({x}) = {y}'

if __name__ == '__main__':
    app = FeedbackShiftRegister(config=3, init_state=7)
    print(app.next_step())

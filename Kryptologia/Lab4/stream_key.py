import numpy as np


class FeedbackShiftRegister:
    def __init__(self, config=None, init_state=None, bits=8):
        self._bits = bits
        self._max_num = 2**bits - 1

        if init_state:
            self.state = init_state
        else:
            self.state = int(np.random.random()*(self._max_num - 1) + 1)

        if config:
            self.config = (config % (self._max_num + 1))
        else:
            self.config = int(np.random.random()*(self._max_num - 1) + 1)

        self.config = bin(self.config)
        # self.state = bin(self.state)

    def next_step(self):
        out = bin(self.state)[-self._bits]
        x = 1
        print(config)
        for i in range(self._bits):
        	if self.config[-i] == '1':
	        	x = x ^ self.state[-i]
        
        self.state.pop(0)
        self.state.append(x)
        return out


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
app = FeedbackShiftRegister(config=3, init_state=7)
print(app.next_step())

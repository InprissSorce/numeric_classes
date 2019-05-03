import math, frac

def approx_eq(a, b, t):
    # test a and b for equality with tolerance t
    return abs(a - b) < t

def is_numer(*args):
    numeric_types = [int, float, frac.frac]
    for arg in args:
        if type(arg) not in numeric_types:
            return False
    return True

class cnum():

    def __init__(self, real, imag = 0):
        if not is_numer(real, imag):
            raise TypeError
        self.rp = real
        self.ip = imag

    def __neg__(self):
        return cnum(-1, 0) * self

    def conj(self):
        a, b = self.rp, self.ip
        return cnum(a, -b)

    def __abs__(self):
        return math.sqrt(self.rp ** 2 + self.ip ** 2)

    def __mul__(self, second):
        if isinstance(second, (int, float)):
            second = cnum(second)
        a, b = self.rp, self.ip
        c, d = second.rp, second.ip
        return cnum(a*c - b*d, a*d + b*c)
    
    def __rmul__(self, second):
        # handle cases of form real * complex
        # self is complex (the right operand), second is real (the left operand)
        second = cnum(second)
        a, b = self.rp, self.ip
        c, d = second.rp, second.ip
        return cnum(a*c - b*d, a*d + b*c)

    def __add__(self, second):
        if isinstance(second, (int, float)):
            second = cnum(second)
        a = self.rp + second.rp
        b = self.ip + second.ip
        return cnum(a, b)

    def __radd__(self, second):
        # handle cases of form real + complex
        # self is complex (the right operand), second is real (the left operand)
        return self + second

    def __sub__(self, second):
        return self + -1 * second

    def __rsub__(self, second):
        # handle cases of form real - complex
        # self is complex (the right operand), second is real (the left operand)
        second = cnum(second)
        return second + -1 * self

    def __truediv__(self, second):
        # multiply dividend and divisor by conjugate of divisor
        if isinstance(second, (int, float)):
            second = cnum(second, 0)
        top = self * second.conj()
        bottom = second.rp ** 2 + second.ip ** 2
        a, b = top.rp / bottom, top.ip / bottom
        return cnum(a, b)

    def __rtruediv__(self, second):
        # handle cases of form real / complex
        # self is complex (the bottom), second is real (the top)
        second = cnum(second, 0)
        top = second * self.conj()
        bottom = self.rp ** 2 + self.ip ** 2
        a, b = top.rp / bottom, top.ip / bottom
        return cnum(a, b)

    def __pow__(self, power):
        if power == 0:
            return 1
        elif power == 1:
            return self
        elif power < 0:
            return 1 / self ** abs(power)
        else:
            return self * (self ** (power - 1))

    def __eq__(self, second):
        if isinstance(second, (float, int)):
            second = cnum(second, 0)
        tolerance = 0.0000001
        return approx_eq(self.rp, second.rp, tolerance) and approx_eq(self.ip, second.ip, tolerance)

    def __ne__(self, second):
        return not self == second

    def __repr__(self):
        return "(" + str(self.rp) + " + " + str(self.ip) + "i)"

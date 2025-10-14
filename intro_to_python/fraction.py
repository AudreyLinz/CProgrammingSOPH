class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        divisor = gcd(numerator, denominator)
        self._numerator = numerator // divisor
        self._denominator = denominator // divisor

    #getters
    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    #setters
    @numerator.setter
    def numerator(self, value):
        self._numerator = value

    @denominator.setter
    def denominator(self, value):
        if value == 0:
            print("Incorrect input")
            self._denominator = 1
        else:
            self._denominator= value
    def __str__(self):
        return f"{self.numerator}/{self._denominator}"
    
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    def __sub__(self, other):
        n = self.numerator * other.denominator - other.numerator*self.denominator
        d = self.denominator * other.denominator
        return Fraction(n, d)
    
    def __cmp__(self, other):
        temp = self - other
        if temp.numerator < 0:
            return -1
        elif temp.numerator > 0:
            return 1
        else: 
            return 0
    def __lt__(self, other):
        return self.__cmp__(other) < 0
def gcd(a, b):
    while (b!=0):
        a = b
        b = a % b
    return abs(a)

f1 = Fraction(2, 3)
print(f1.numerator)
print(f1.denominator)

print(f1)

f1.numerator = 7
print(f1)

f2 = Fraction(3,7)
print(f"{f1} * {f2} = {f1 * f2}")
print(f"{f1} < {f2} is {f1 < f2}")
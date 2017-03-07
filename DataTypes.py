import math

class Fraction:
    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "%d/%d" % (self.numerator, self.denominator)

    def __cmp__(self, other):
        if (math.floor(self.numerator/self.denominator) > other):
            return 1
        if (math.floor(self.numerator/self.denominator) == other):
            return 0
        else:
            return -1

    def __eq__(self, other):
        return (math.floor(self.numerator/self.denominator) == other)


class MixedNumbers:
    def __init__(self, wholeNum, numerator, denominator):
        self.wholeNum = wholeNum
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "%d %d/%d" % (self.wholeNum, self.numerator, self.denominator)

    def __cmp__(self, other):
        if (math.floor(self.wholeNum + self.numerator/self.denominator) > other):
            return 1
        if (math.floor(self.wholeNum + self.numerator/self.denominator) == other):
            return 0
        else:
            return -1

    def __eq__(self, other):
        return (math.floor(self.wholeNum + self.numerator / self.denominator) == other)


#Testing
a = Fraction(7,5)
b = Fraction(4,5)
c = Fraction(3,5)
print("Printing some fractions")
print(a)
print(b)
m = MixedNumbers(1, 2, 5)
n = MixedNumbers(0, 4, 5)
k = MixedNumbers(2, 1, 3)
print("Printing some mixed numbers")
print(m)
print(n)
print("Comparing a fraction and a fraction")
print(a.__cmp__(b))
print("Comparing the opposite of the previous")
print(b.__cmp__(a))
print("Comparing a fraction and a mixed number")
print(a.__cmp__(k))
print("Comparing a mixed number and a fraction")
print(n.__cmp__(a))
print("Comparing the opposite of the previous")
print(a.__cmp__(n))
print("Comparing an equal fraction and mixed number")
print(b.__cmp__(n))
print("Comparing a mixed number and a mixed number")
print(n.__cmp__(k))
print("Comparing the opposite of the previous example")
print(k.__cmp__(n))
print("Are 4/5 and 0 4/5 equal?")
print(b.__eq__(n))
print("Are 3/5 and 7/5 equal?")
print(a.__eq__(c))
print("Are 1 2/5 and 2 1/3 equal?")
print(m.__eq__(k))
print("Are 7/5 and 1 2/5 equal?")
print(a.__eq__(m))


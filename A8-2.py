# rp = real part & ip = imaginary part
class ComplexNumber:
    def __init__(self, rp, ip):
        self.r = rp
        self.i = rp

    def mul(self, other):

        result = ComplexNumber(0, 0)
        result.r = self.r * other.r - self.i * other.i
        result.i = self.r * other.i + self.i * other.r

        return result

    def sum(self, other):

        result = ComplexNumber(0, 0)
        result.r = self.r + other.r
        result.i = self.i + other.i

        return result

    def minus(self, other):

        result = ComplexNumber(0, 0)
        result.r = self.r - other.r
        result.i = self.i - other.i

        return result

    def div(self, other):

        result = ComplexNumber(0, 0)
        a = other.r ** 2 + other.i ** 2
        result.r = (self.r * other.r + self.i * other.i) / a
        result.i = (self.i * other.r - self.r * other.i) / a

        return result


s1 = int(input("Enter a real part for variable one: "))
m1 = int(input("Enter a imaginary part for variable one: "))
s2 = int(input("Enter a real part for variable two: "))
m2 = int(input("Enter a imaginary part for variable two: "))
a = ComplexNumber(s1, m1)
b = ComplexNumber(s2, m2)

while True:
    print('done! Now choose your action from the list below: ')
    print('1- multiplication two Complex numbers')
    print('2- Addition two Complex numbers')
    print('3- minus two Complex numbers')
    print('4- div two Complex numbers')
    print('5- exit')
    choice = int(input('choose what do you want?: '))
    if choice == 1:
        c = a.mul(b)
        print('the multiplication of these two complex number is: ')
        print(c.r, '+', c.i, 'i')
    elif choice == 2:
        c = a.sum(b)
        print('the Addition of these two complex number is: ')
        print(c.r, '+', c.i, 'i')
    elif choice == 3:
        c = a.minus(b)
        print('the minus of these two complex number is: ')
        if c.i < 0:
            print(c.r, c.i, 'i')
        else:
            print(c.r, '+', c.i, 'i')
    elif choice == 4:
        c = a.div(b)
        print('the division  of these two complex number is: ')
        print(c.r, '+', c.i, 'i')
    elif choice == 5:
        exit()
    else:
        print('Enter correct option from menu')

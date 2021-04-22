class Fraction:

    def __init__(self, ss, mm):

        self.s = ss
        self.m = mm

    def mul(self, other):
        result = {'s': self.s * other.s, 'm': self.m * other.m}
        return result

    def sum(self, other):
        result = {'s': self.s * other.m + self.m * other.s, 'm': self.m * other.m}
        return result

    def minus(self, other):
        result = {'s': self.s * other.m -self.m * other.s, 'm': self.m *other.m}
        return result

    def div(self, other):
        result = {'s': self.s * other.m, 'm': self.m * other.s}
        return result


s1 = int(input("Enter a numerator for variable one: "))
m1 = int(input("Enter a denominator for variable one: "))
s2 = int(input("Enter a numerator for variable two: "))
m2 = int(input("Enter a denominator for variable two: "))
a = Fraction(s1, m1)
b = Fraction(s2, m2)

while True:
    print('done! Now choose your action from the list below: ')
    print('1- multiplication two Fraction')
    print('2- Addition two Fraction')
    print('3- minus two Fraction')
    print('4- div two Fraction')
    print('5- exit')
    choice = int(input('choose what do you want?: '))
    if choice == 1:
        c = a.mul(b)
        print('the multiplication of these two Fraction is: ')
        print(c['s'], '/', c['m'])
    elif choice == 2:
        c = a.sum(b)
        print('the Addition of these two Fraction is: ')
        print(c['s'], '/', c['m'])
    elif choice == 3:
        c = a.minus(b)
        print('the minus of these two Fraction is: ')
        print(c['s'], '/', c['m'])
    elif choice == 4:
        c = a.div(b)
        print('the division  of these two Fraction is: ')
        print(c['s'], '/', c['m'])
    elif choice == 5:
        exit()
    else:
        print('Enter correct option from menu')

class Fraction:

    def __init__(self, ss1, mm1, ss2, mm2):

        self.s1 = ss1
        self.m1 = mm1
        self.s2 = ss2
        self.m2 = mm2

    def mul(self):
        result = {'s': self.s1 * self.s2, 'm': self.m1 * self.m2}
        return result

    def sum(self):
        result = {'s': self.s1 * self.m2 + self.m1 * self.s2, 'm': self.m1 * self.m2}
        return result

    def minus(self):
        result = {'s': self.s1 * self.m2 -self.m1 * self.s2, 'm': self.m1 *self.m2}
        return result

    def div(self):
        result = {'s': self.s1 * self.m2, 'm': self.m1 * self.s2}
        return result


s1 = int(input("Enter a numerator for variable one: "))
m1 = int(input("Enter a denominator for variable one: "))
s2 = int(input("Enter a numerator for variable two: "))
m2 = int(input("Enter a denominator for variable two: "))
a = Fraction(s1, m1, s2, m2)

while True:
    print('done! Now choose your action from the list below: ')
    print('1- multiplication two Fraction')
    print('2- Addition two Fraction')
    print('3- minus two Fraction')
    print('4- div two Fraction')
    print('5- exit')
    choice = int(input('choose what do you want?: '))
    if choice == 1:
        c = a.mul()
        print('the multiplication of these two Fraction is: ')
        print(c['s'], '/', c['m'])
    elif choice == 2:
        c = a.sum()
        print('the Addition of these two Fraction is: ')
        print(c['s'], '/', c['m'])
    elif choice == 3:
        c = a.minus()
        print('the minus of these two Fraction is: ')
        print(c['s'], '/', c['m'])
    elif choice == 4:
        c = a.div()
        print('the division  of these two Fraction is: ')
        print(c['s'], '/', c['m'])
    elif choice == 5:
        exit()
    else:
        print('Enter correct option from menu')

# rp = real part & ip = imaginary part
class ComplexNumber:
    def __init__(self, rp1, ip1, rp2, ip2):
        self.r1 = rp1
        self.i1 = ip1
        self.r2 = rp2
        self.i2 = ip2

    def mul(self):
        result = {'rp': self.r1 * self.r2 - self.i1 * self.i2, 'ip': self.r1 * self.i2 + self.i1 * self.r2}

        return result

    def sum(self):
        result = {'rp': self.r1 + self.r2, 'ip': self.i1 + self.i2}

        return result

    def minus(self):
        result = {'rp': self.r1 - self.r2, 'ip': self.i1 - self.i2}

        return result

    def div(self):
        a = self.r2 ** 2 + self.i2 ** 2
        result = {'rp': (self.r1 * self.r2 + self.i1 * self.i2) / a, 'ip': (self.i1 * self.r2 - self.r1 * self.i2) / a}

        return result


s1 = int(input("Enter a real part for variable one: "))
m1 = int(input("Enter a imaginary part for variable one: "))
s2 = int(input("Enter a real part for variable two: "))
m2 = int(input("Enter a imaginary part for variable two: "))
a = ComplexNumber(s1, m1, s2, m2)

while True:
    print('done! Now choose your action from the list below: ')
    print('1- multiplication two Complex numbers')
    print('2- Addition two Complex numbers')
    print('3- minus two Complex numbers')
    print('4- div two Complex numbers')
    print('5- exit')
    choice = int(input('choose what do you want?: '))
    if choice == 1:
        c = a.mul()
        print('the multiplication of these two complex number is: ')
        print(c['rp'], '+', c['ip'], 'i')
    elif choice == 2:
        c = a.sum()
        print('the Addition of these two complex number is: ')
        print(c['rp'], '+', c['ip'], 'i')
    elif choice == 3:
        c = a.minus()
        print('the minus of these two complex number is: ')
        if c['ip'] < 0:
            print(c['rp'], c['ip'], 'i')
        else:
            print(c['rp'], '+', c['ip'], 'i')
    elif choice == 4:
        c = a.div()
        print('the division  of these two complex number is: ')
        print(c['rp'], '+', c['ip'], 'i')
    elif choice == 5:
        exit()
    else:
        print('Enter correct option from menu')

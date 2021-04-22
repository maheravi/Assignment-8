class Time:
    def __init__(self, hr, min, sec):

        self.h = hr
        self.m = min
        self.s = sec

    def sum(self, other):
        result = {'hr': self.h + other.h, 'm': self.m + other.m, 's': self.s + other.s}
        if result['s'] > 59:
            result['m'] += 1
            result['s'] -= 60
        if result['m'] > 59:
            result['hr'] += 1
            result['m'] -= 60
        return result

    def minus(self, other):
        result = {'hr': self.h - other.h, 'm': self.m - other.m, 's': self.s - other.s}
        if result['s'] < 0:
            result['m'] -= 1
            result['s'] += 60
        if result['m'] < 0:
            result['hr'] -= 1
            result['m'] += 60
        return result

    def sec2time(self):
        result = Time(None, None, None)
        sec = int(input('pleas enter seconds: '))
        result.h = sec // 3600
        sec = sec % 3600
        result.m = sec // 60
        sec = sec % 60
        result.s = sec
        print('the second is: ')
        print(result.h, ':', result.m, ':', result.s)
        return result

    def time2sec(self):
        result = self.h * 3600 + self.m * 60 + self.s
        return result


while True:
    print('1- addition two time')
    print('2- minus two time')
    print('3- second to time converter')
    print('4- time to second converter')
    print('5- exit')

    choice = int(input('choose what do you want?: '))
    if choice == 1:
        hr = int(input("Enter a hour for time one: "))
        m = int(input("Enter a minute for time one: "))
        s = int(input("Enter a second for time one: "))
        a = Time(hr, m, s)
        hr = int(input("Enter a hour for time one: "))
        m = int(input("Enter a minute for time one: "))
        s = int(input("Enter a second for time one: "))
        b = Time(hr, m, s)
        c = a.sum(b)
        print('the Addition of these two time is: ')
        print(c['hr'], ':', c['m'], ':', c['s'])
    elif choice == 2:
        hr = int(input("Enter a hour for time one: "))
        m = int(input("Enter a minute for time one: "))
        s = int(input("Enter a second for time one: "))
        a = Time(hr, m, s)
        hr = int(input("Enter a hour for time one: "))
        m = int(input("Enter a minute for time one: "))
        s = int(input("Enter a second for time one: "))
        b = Time(hr, m, s)
        c = a.minus(b)
        print('the minus of these two time is: ')
        print(c['hr'], ':', c['m'], ':', c['s'])
    elif choice == 3:
        c = Time(0, 0, 0)
        a = c.sec2time()
    elif choice == 4:
        hr = int(input("Enter a hour: "))
        m = int(input("Enter a minute: "))
        s = int(input("Enter a second: "))
        a = Time(hr, m, s)
        c = a.time2sec()
        print('the second is: ')
        print(c)
    elif choice == 5:
        exit()
    else:
        print('Enter correct option from menu')

class Date:
    def __init__(self, dd, mm, yyyy):

        self.d = dd
        self.m = mm
        self.y = yyyy

    def show(self):
        print(self.y, '/', self.m, '/', self.d)

    def add(self, other):
        result = Date(0, 0, 0)
        result.d = self.d + other.d
        result.m = self.m + other.m
        result.y = self.y + other.y
        if result.d > 30:
            result.m += 1
            result.d -= 30
        if result.m > 12:
            result.y += 1
            result.m -= 12
        return result

    def getMonthName(self):
        mm = ['Farvardin', 'Ordibehesht', 'Khordad', 'Tir', 'Mordad', 'Shahrivar', 'Mehr', 'Aban', 'Azar', 'Dey',
                 'Bahman', 'Esfand']
        print('The equivalent month to', self.m, 'is', mm[self.m])

    def isLeapYear(self):
        List = [1, 5, 9, 13, 17, 22, 26, 30]
        if self.y % 33 in List:
            result = True
        else:
            result = False
        return result

    def sub(self, other):
        result = Date(0, 0, 0)
        result.d = self.d - other.d
        result.m = self.m - other.m
        result.y = self.y - other.y
        if result.d < 0:
            result.m -= 1
            result.d += 30
        if result.m < 0:
            result.y -= 1
            result.m += 12
        return result

    def isValidDate(self):
        if 0 < self.d < 30 and 0 < self.m < 12 and 1 < self.y < 9999:
            result = True
            print('your input date is', result)
        else:
            result = False
            print('your input date is', result)


# while True:
#     print('Choose your action from the list below: ')
#     print('1- show date')
#     print('2- add two date')
#     print('3- name of month')
#     print('4- is leap year checker')
#     print('5- minus two date')
#     print('6- check date is valid')
#     print('7- exit')
#     choice = int(input('choose what do you want?: '))
#     if choice == 1:
#         dd = int(input("Enter day: "))
#         mm = int(input("Enter month: "))
#         yyyy = int(input("Enter year: "))
#         a = Date(dd, mm, yyyy)
#         a.show()
#     elif choice == 2:
#         dd = int(input("Enter day for date one: "))
#         mm = int(input("Enter month for date one: "))
#         yyyy = int(input("Enter year for date one: "))
#         a = Date(dd, mm, yyyy)
#         dd = int(input("Enter day for date two: "))
#         mm = int(input("Enter month for date two: "))
#         yyyy = int(input("Enter year for date two: "))
#         b = Date(dd, mm, yyyy)
#         a.add(b).show()
#     elif choice == 3:
#         mm = int(input("Enter month: "))
#         a = Date(0, mm-1, 0)
#         a.getMonthName()
#     elif choice == 4:
#         yyyy = int(input("Enter year: "))
#         a = Date(0, 0, yyyy)
#         b = a.isLeapYear()
#         print('The result of checking leap for', yyyy, 'is', b)
#     elif choice == 5:
#         dd = int(input("Enter day for date one: "))
#         mm = int(input("Enter month for date one: "))
#         yyyy = int(input("Enter year for date one: "))
#         a = Date(dd, mm, yyyy)
#         dd = int(input("Enter day for date two: "))
#         mm = int(input("Enter month for date two: "))
#         yyyy = int(input("Enter year for date two: "))
#         b = Date(dd, mm, yyyy)
#         a.sub(b).show()
#     elif choice == 6:
#         dd = int(input("Enter day: "))
#         mm = int(input("Enter month: "))
#         yyyy = int(input("Enter year: "))
#         a = Date(dd, mm, yyyy)
#         a.isValidDate()
#     elif choice == 7:
#         exit()
#     else:
#         print('Enter correct option from menu')

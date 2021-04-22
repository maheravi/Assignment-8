from classdate import Date

print('Welcome to Age calculation program: ')
print('First you need to enter date: ')
dd = int(input("Enter day: "))
mm = int(input("Enter month: "))
yyyy = int(input("Enter year: "))
a = Date(dd, mm, yyyy)
print('Alright! now enter your birth date')
dd = int(input("Enter day: "))
mm = int(input("Enter month: "))
yyyy = int(input("Enter year: "))
print('Okay! Now you are')
b = Date(dd, mm, yyyy)
a.sub(b).show()


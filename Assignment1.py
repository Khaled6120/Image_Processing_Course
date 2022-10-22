# Variables and Input function
name = input('what is your name? ')
print('Hello ' + name)

# Type convertion
birthYear = input('what is your birth year? ')
age = 2022 - int(birthYear)
print(age)


# int()   ==> converting to integer
# float() ==> converting to float number
# bool()  ==> converting to boolean value
# str()   ==> converting to string

# Functions
def sum(num1, num2):
    total = float(num1) + float(num2)
    print(total)


sum(2.4, 4)

# if satement
temp = int(input('what is the temperature now ? '))
if temp < 15:
    print('its a cold weather')
elif temp > 15 & temp < 30:
    print('the weather is nice')
else:
    print('its a hot weather')

# While Loop
digit = int(input('multiple table of number :'))
i = 0
while (i <= 10):
    print(str(i) + '*' + str(digit) + '=' + str(i * digit))
    i = i + 1

# List
names = ['khaled', 'Amro', 'Yasin', 'Omer']
print(names[0:2])
names.append('Hamad')
names.insert(0, 'Mustafa')
names.remove('Amro')
print('khaled' in names)
print(len(names))
names.clear()

# for loops
numbers = [1, 2, 3, 4, 5]
total = 0
for item in numbers:
    total = total + item
print(total)

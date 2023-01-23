import random

# 1
print('Hello World')

# 2
user_input = input('What is your name?  ')
print('Hello', user_input)

# 3
user_input2 = input('What is your name?  ')
print("Hello " + user_input2)

# 4
user_input3 = input('Enter a number:  ')
for i in range(int(user_input3)):
    print(i+i+1)

# 6
user_input4 = input('Enter a number and product or sum. EX(9,sum):  ')
x = user_input4.split(',')
if x[1] == ' sum':
    for i in range(int(user_input4[0])):
        print(i+i+1)
if x[1] == ' product':
    for i in range(int(user_input4[0])):
        print(i*(i+1))

# 7
number = 12

for x in range(1, 11):
   print(number, 'x', x, '=', number * x)

# 8
for y in range (1, 501):
    count = 0
    for z in range(2, (y//2 + 1)):
        if(y % z == 0):
            count = count + 1
            break

    if (count == 0 and y != 1):
        print(" %d" %y, end = '  ')

# 9
number = random.randint(0,100)
for c in range(6):
    user_input7 = input('What is your guess?  ')
    if int(user_input7) == number:
        print('Correct!')
    else:
        print('Wrong.')

# 10
current_year = 2020
for a in range(2020, 3000):
    if (0 == a % 4) and (0 != a % 100) or (0 == a % 400):
        print(a)

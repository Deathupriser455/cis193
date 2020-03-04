#Kevin Craig
#March 2
#new topic - if statements
pw = 'Auburn'
#Ask the user for password
pwInput = input('Enter your password: ')
if pw == pwInput:
    print('True works')
else:
    print('false works')

#keep going
x = 5
print(x > 0 and x < 10)
print(not(x > 0 and x < 10))

n = 25
print(n % 2 == 0 or n % 3 == 0)
print(not(n % 2 == 0 or n % 3 == 0))

if 4 + 5 == 10:
    print("TRUE")
else:
    print("FALSE")
print('True')

#define y
y = 5

if x < y:
    print('%d < %d' % (x, y))
else:
    if x > y:
        print('%d > %d' % (x, y))
    else:
        print('%d == %d' % (x, y))

print('Done')

#chained conditional
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y must be equal")


#assign A or B or C
#ask user for score
score = int(input('Enter a score: '))
grade = ''

#if..elif..elif..else
if score >= 90 and score <= 100:
    grade = 'A'
elif score >= 80 and score < 90:
    grade = 'B'
else:
    grade = 'F'

print(grade)

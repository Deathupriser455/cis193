#In-Class lab Feb 3, 2020
#Kevin Craig
#range function and repetition

for i in range (1,101):
    print(i,'I will not drink water from the faucet.')

#Create new total var == create new storage location
total = 0

for i in range(4):
    total = total + i
    print('Total is: ', total)

print('End')

import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
andy.goto(-100,20)
lance.goto(-100,-20)

# your code goes here
#create two random numbers
x = random.randrange(50,100)
y = random.randrange(50,100)

#turtles move forward using random numbers x, y as input parameter
for i in range(4):
    lance.forward(x)
    andy.forward(y)

wn.exitonclick()

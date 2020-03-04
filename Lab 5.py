#Kevin Craig
#2/12/20
#Lab 5
import turtle
#It will print numbers from 1 to 10
for i in range (1,11):
    print(i)
print(' ')
#It will print numbers from 10 to 1
for i in range(10):
    i = 10 - i
    print(i)

#Sum up the numbers entered by the user
total = 0
for i in range(4):
    Num = int(input("What is the number? "))
    total = total + Num

#Print the total
print('Total:',total)

#Turtle Joe will make a Hexagon
Joe = turtle.Turtle()
Joe.pensize(5)
Joe.fillcolor('blue')
Joe.begin_fill()
for i in range(6):
    Joe.forward(100)
    Joe.left(60)
Joe.end_fill()

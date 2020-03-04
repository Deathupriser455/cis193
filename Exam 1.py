#Kevin Craig
#2/17/20
#Exam 1 Part 1

import turtle
wn = turtle.Screen()
bill = turtle.Turtle()
bill.pensize(3)
turtle.bgcolor('Black')

#Draw first circle
bill.penup()
bill.goto(0,10)
bill.pendown()
bill.pencolor('green')
bill.fillcolor('blue')
bill.begin_fill()
bill.circle(30)
bill.end_fill()

#Draw second circle
bill.penup()
bill.goto(0,-60)
bill.pendown()
bill.pencolor('orange')
bill.fillcolor('red')
bill.begin_fill()
bill.circle(40)
bill.end_fill()

#Draw third circle
bill.penup()
bill.goto(0,-120)
bill.pendown()
bill.pencolor('green')
bill.fillcolor('blue')
bill.begin_fill()
bill.circle(50)
bill.end_fill()

#Draw fourth circle
bill.penup()
bill.goto(0,-200)
bill.pendown()
bill.pencolor('orange')
bill.fillcolor('red')
bill.begin_fill()
bill.circle(60)
bill.end_fill()

#Draw fifth circle
bill.penup()
bill.goto(0,-260)
bill.pendown()
bill.pencolor('green')
bill.fillcolor('blue')
bill.begin_fill()
bill.circle(70)
bill.end_fill()

#Draw sixth circle
bill.penup()
bill.goto(0,-320)
bill.pendown()
bill.pencolor('orange')
bill.fillcolor('red')
bill.begin_fill()
bill.circle(80)
bill.end_fill()

wn.exitonclick()

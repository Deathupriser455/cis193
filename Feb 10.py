#Kevin Craig
#Feb 10 in-class labs
#Python modules - Chapter 5
#Python functions - Chapter 6
import math
import random

#function definitions go up here
#functions with 2 inputs and a return value
def add(x, y):
    #use keyword return to bring out the return value
    return x + y

#define a function that draws Lab 1 box in the character of your choices
def drawBox(ch):
    print(ch * 5,'\n')
    print(ch,' ',ch, '\n')
    print(ch * 5,'\n')
    print(ch,' ',ch,'\n')
    print(ch * 5)

#define main()
def main():
    print('Number PIL ', math.pi)
    x = 16
    print('Square root: ', math.sqrt(x))

    y = 2
    result = math.pow(x, y)
    print(x, 'to the power of', y, 'is: ', result)

    #random numbers
    prob = random.random()
    print(prob)

    ###Write for loop using range() to put 100 random numbers between 1 and 6
    ##for i in range(100):
    ##    diceThrow = random.randrange(1, 7)       # return an int, one of 1,2,3,4,5,6
    ##    print(diceThrow)

    #Testing randint(a,b)
    for i in range(100):
        diceThrow = random.randint(1, 6)
        print(diceThrow)
    
    #Calling add(x,y)
    result = add(x, y)
    print(x, '+', y, '=', result)

    #Calling drawBow(ch)
    drawBox('*')
    
#function call main()
main()

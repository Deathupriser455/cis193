#Kevin Craig
#2/26/20
#Lab 7

import random
#global

#define function up here
def getRands1to100(userInput):
    #set up total
    total = 0
    for x in range(userInput):
        #use accumulator pattern to sum up random numbers
        r = random.randint(1,100)
        print(r)
        total += r
    return total

def getRandsAnyRange(userInput, x,y):
    #set up total
    total = 0
    for x in range(userInput):
        #use accumulator pattern to sum up random numbers
        r = random.randint(x,y)
        print(r)
        total += r
    return total
##for x in range(100):
##    print(random.randint(1,100))


#define ONE main() only
def main():
    #ask user
    userInput = int(input('Enter # of numbers to sum up: '))
    #call function: 1 input, has an output
    result = getRands1to100(userInput)
    print('Result is: %d' % result)

    #Second function call
    #ask user
    userInput = int(input('Enter # of numbers to sum up: '))
    x = int(input('Start value: '))
    y = int(input('End value: '))
    #call function: 1 input, has an output
    result = getRandsAnyRange(userInput, x,y)
    print('Result is: %d' % result)
#call main
main()


#nothing follows

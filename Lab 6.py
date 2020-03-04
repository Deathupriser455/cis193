#Kevin Craig
#2/19/20
#Lab 6
#Import statements
import math
#def all functions here
def sumTo(n):
    sum = (n * (n + 1)) / 2
    return sum
#define function area of rectangle
def areaRect(l, w):
    return l * w

#define function area of circle
def areaCircle(r):
    return math.pi * r ** 2

#define conversion function - miles to km
#conversion factor is 1.60934
def milesToKm(x):
    factor = 1.60934
    return x * factor
#def main():
def main():
    print('Hello main!')
    x = 5
    result = sumTo(x)
    print('The sum of all numbers from 1 to', x, 'is:', result)

    #call areaRect(l,w) function
    l = 30
    w = 10
    area = areaRect(l, w)
    print('The area of a rectangle of length', l, 'and width', w, 'is:', area)

    #area of a circle
    #print(2 ** 4)
    area = areaCircle(x)
    print('The area of a circle of radius %d is %f.' % (x, area))

    #call converter miles to km
    result = milesToKm(x)
    #print('%f miles is %f kilometer.', % (x, result))
    
#call main()
main()
#nothing follows

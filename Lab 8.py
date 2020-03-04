#Kevin Craig
#Lab 8
#boolean functions

def isValidVoter(age):
    #if statement - 18+
    if age >= 18 and age <= 135:
        return True
    else:
        return False
    
def isLeapYear(year):
    if year % 4 == 0:
        return True
    else:
        return False
    
#define main()
def main():
    #ask user for name and age
    name = 'Beth'
    age = 4
    year = 2024
    
    #call isValidVoter
    if isValidVoter(age):
        print('%s, at %d years old you are a valid voter' % (name, age))
    else:
        print('%s, at %d years old you are NOT a valid voter' % (name, age))

    #call isLeapYear
    if isLeapYear(year):
        print('%d is a leap year' % (year))
    else:
        print('%d is NOT a leap year' % (year))

    
#Call main()
main()

#Nothing follows

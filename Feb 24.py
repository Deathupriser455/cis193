#Kevin Craig
#Feb 24, 2020
#Lab

#Convert miles to kilometer
#function  def at the top
#function with 1 input: miles
#returns KM

def convertMtoKM(miles):
    factor = 1.60934
    #conversion calculation
    km = miles * factor
    return km

#def function to convert US $ to Yen
def convertUStoYen(US):
    Yen = 110.49
    #conversion calculation
    total = US * Yen
    return total

#def function to convert MB to GB
def convertMBtoGB(MB):
    Data = 0.001
    #conversion calculation
    GB = MB * Data
    return GB

#define main():
def main():
    #ask user for miles input
    miles = float(input('Enter miles: '))

    #call conversion function
    km = convertMtoKM(miles)

    #output
    print('%.2f miles is %.4f km.' % (miles, km))

    #convert $ to yen
    US = float(input('Enter the amount of US dallor: '))
    total = convertUStoYen(US)
    print('%.f US dallor is %.2f Yen.' % (US, total))

    #convert MB to GB
    MB = float(input('Enter the amount of MB: '))
    GB = convertMBtoGB(MB)
    print('%.2f MB is %.3f GB.' % (MB, GB))
main()

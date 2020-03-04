#Lab 4
#Kevin Craig
#2/5/20

#beginning of the loop

count = 5
total = 0
for i in range(count):
    test = int(input("What is your test score? " ))
    total = total + test

#The average after the loop
print('Total: ',total)
print('Average: ', total/count)

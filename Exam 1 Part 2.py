#Kevin Craig
#2/17/20
#Exam 1 Part 2

pizza = int(input('How much pizza are you getting? '))
price = 10.99
foodTotal = pizza * price
taxRate = 0.085
Tax = foodTotal * taxRate
billTotal = foodTotal + Tax

print('Your order:', pizza,'at',price,'each')
print('Food total:',foodTotal)
print('Tax amount:',Tax)
print('Your bill:',billTotal)

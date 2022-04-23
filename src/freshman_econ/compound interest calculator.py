
#input

p = eval(input('principal: '))
n = eval(input('frequency: '))
r = eval(input('rate: '))
t = eval(input('years: '))


#processing

total = p*(1+r/n)**(n*t)


#output

print('Your total is')
print(total)

input("\nPress enter to close window... ")

import matplotlib.pyplot as plt


#input
print('Choose 1 item to be A and another to be B')
UnitA = input('Good A is: ')
UnitB = input('Good B is: ')
A = eval(input('Maximum output of product A: '))
B = eval(input('Maximum output of product B: '))

#processing

OpCostA = B/A
OpCostB = A/B


#BreakdownA = A - OpCostB
#BreakdownB = 0 + OpCostA
#A = i[0]
#i[ = A*
#A* = i - OpcostA

#output

print(' ')
print(' ')

print('Oppertunity Cost is...')

print('Each unit of', UnitA, 'costs' , OpCostA , 'units of', UnitB)

print('Each unit of', UnitB, 'costs' , OpCostB , 'units of', UnitA)

print(' ')
print(' ')

input("\nPress enter for breakdown and graph... ")
print('Breakdown...',(UnitA, UnitB))

CountA = A
A2 = CountA
CountB = 0
B2 = CountB
x = [A]
y = [0]


print(A, 0)
while (A2 > 0) and (B2 < B) and (CountA > 0) and (CountB < B): 
    CountA = A2 - OpCostB
    A2 = CountA - OpCostB
    CountB = B2 + (OpCostB * OpCostA)
    B2 = CountB + (OpCostB * OpCostA)

    print(CountA, CountB)
    x.append(CountA)
    y.append(CountB)
    print(A2, B2)
    x.append(A2)
    y.append(B2)


print(' ')
print(' ')

title = 'y =',-OpCostA,'x +',B
print('Equation...')
print('y =',-OpCostA,'x +', B)


plt.plot(x,y)

plt.xlabel(UnitA)
plt.ylabel(UnitB)
plt.title(title)


plt.show()




input("\nPress enter to close window... ")
    



#input

Q1 = eval(input('Quantity 1: '))
Q2 = eval(input('Quantity 2: '))
P1 = eval(input('Price 1: '))
P2 = eval(input('Price 2: '))

#processing

dQ = (Q2-Q1)/(Q1+Q2)
dP = (P2-P1)/(P1+P2)

Elasticity = dQ/dP

#output

print('Elasticity is')
print(Elasticity)

input("\nPress enter to close window... ")

print('Demand = A - Bp')
print('Supply = C + Dp')

A = eval(input('A = '))
B = eval(input('B = '))
C = eval(input('C = '))
D = eval(input('D = '))

p = (A - C)/(D - B)

q = A - B*p

print('Equilibrium Price = {}'.format(p))
print('Equilibrium Quantity = {}'.format(q))

input('Press enter')

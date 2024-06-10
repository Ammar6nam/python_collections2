from addition import add as a
from division import div as d
from powering import power as p
from subtraction import sub as s

n1 = int(input('enter the first number: '))
n2= int(input('Enter the second number: '))

print(f'Result of addition is {a(n1,n2)}')
print(f'Result of subtraction is {s(n1,n2)}')
print(f'Result of ceiling is {d(n1,n2)}')
print(f'Result of powering is {p(n1,n2)}')
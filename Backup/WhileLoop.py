# while loop
'''
a = 0

while a < 100:
    a = a + 1
    print(a)
'''

# Fibonacci Series - 0 1 1 3 5 8 13 21 34
'''
a = 1
b = 0

while b < 100:
    print(b, end=' ')
    a,b = b, a+b
'''

'''
a = 1
b = 0
n = int(input("Enter the terms : "))
i = 0
while i < n:
    print(b)
    a,b = b, a+b
    i = i + 1
'''

for i in range(5):
    print(' ' * (5-i) + '*' * (2*i + 1))

for i in range(5):
    for k in range(5-i):
        print(' ',end='')
    for j in range(2*i + 1):
        print('*', end='')
    print()

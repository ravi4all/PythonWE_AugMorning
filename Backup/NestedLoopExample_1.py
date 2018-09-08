# Nested For Loop
'''
for i in range(5):
    print("I is",i)

    for j in range(5):
        print("J is",j)
'''

# Prg_1
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()

# Prg_2
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end='')
    print()

# Prg_3
for i in range(1,6):
    for j in range(i,0,-1):
        print(j, end='')
    print()

# Prg_4
for i in range(0,5):
    for j in range(1,2*i + 2):
        print(j, end='')
    print()

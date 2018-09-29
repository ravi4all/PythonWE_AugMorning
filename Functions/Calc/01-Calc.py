def add(x,y):
    result = x + y
    print("Sum is",result)

def sub(x,y):
    # result = x - y
    result = x - y if x > y else y - x
    print("Sub is", result)

def div(x,y):
    result = x / y
    print("Div is", result)

def mul(x,y):
    result = x * y
    print("Mul is", result)

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

userCh = input("Enter your choice : ")

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

operations = {
    "1" : add,
    "2" : sub,
    "3" : div,
    "4" : mul
}

result = operations.get(userCh)
result(num_1, num_2)
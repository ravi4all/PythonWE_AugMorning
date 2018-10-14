try:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    c = a + b
    print("Sum is",c)
    d = a - b
    print("Diff is",d)
    e = a / b
    print("Div is",e)
    f = a * b
    print("Mul is",f)
except BaseException as ex:
    print(ex)
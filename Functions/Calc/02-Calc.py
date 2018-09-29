def calc(x,y,opr):
    expression = x + opr + y
    # expression = '10' + '*' + '12'
    # expression ='10 * 12'
    result = eval(expression)
    print("Output is",result)

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

userCh = input("Enter your choice : ")

num_1 = input("Enter first number : ")
num_2 = input("Enter second number : ")

operations = {
    "1" : '+',
    "2" : "-",
    "3" : "/",
    "4" : "*"
}
opr = operations.get(userCh)
calc(num_1, num_2, opr)

# operations = {
#     "1" : num_1 + num_2,
#     "2" : num_1 - num_2,
#     "3" : num_1 / num_2,
#     "4" : num_1 * num_2
# }
#
# result = operations.get(userCh)
# print(result)
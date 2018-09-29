# lambda - anonymous function
# def temp_conv(c):
#     return 9/5 * c + 32

# temp_conv = lambda c : 9/5 * c + 32
# print(temp_conv(32.4))

temp = [34.5,32.4,37.6,31.2,29.8]
f = list(map(lambda c : 9/5 * c + 32,temp))
print(f)
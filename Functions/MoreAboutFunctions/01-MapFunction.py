def temp_conv(c):
    return 9/5 * c + 32
# f = temp_conv(34.5)
# print(f)
temp = [34.5,32.4,37.6,31.2,29.8]

# f = []
# for t in temp:
#     f.append(temp_conv(t))
# print(f)

f = list(map(temp_conv, temp))
print(f)
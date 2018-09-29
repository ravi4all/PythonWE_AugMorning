def temp_conv(c):
    return 9/5 * c + 32

temp = [34.5,32.4,37.6,31.2,29.8]

def myMap(func,iter):
    data = []
    for i in range(len(iter)):
        data.append(func(iter[i]))

    return data

f = myMap(temp_conv, temp)
print(f)
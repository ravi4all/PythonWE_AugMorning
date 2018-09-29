def even_num(num):
    return num % 2 == 0

# even_num(12)

numbers = [i for i in range(1,101)]
# e = []
# for num in numbers:
#     e.append(even_num(num))
# print(e)

e = list(filter(even_num, numbers))
print(e)
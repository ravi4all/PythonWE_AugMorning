# *args
# **kwargs
def add(num_1, num_2, *num):
    result = num_1 + num_2
    for n in num:
        result += n
    print("Result is",result)
    # print(num)

add(12,4,6)
add(12,4,6,5)
add(12,4,6,9,2)
add(12,4)

def emp(**details):
    print(details)

emp(name = "Ram", age = 30, sal = 30000)
emp(name = "Shyam", sal = 40000, dept = "IT")
emp(name = "Aman", dept = "HR")
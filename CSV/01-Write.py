# comma seperated values
import csv

data = [
    ["FirstName", "LastName"],
    ["Sachin", "Tendulkar"],
    ["Virat", "Kohli"],
    "MS,Dhoni".split(","),
    "Yuvraj,Singh".split(",")
]

# file = open('data.csv', 'w')
# file.close()

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for row in data:
        writer.writerow(row)

# file.read()
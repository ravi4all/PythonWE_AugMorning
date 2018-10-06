import csv

def read_data():
    data = []
    with open('data.csv') as file:
        reader = csv.reader(file)

        for row in reader:
            data.append(row)

    return data

def write_data(users):
    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        for data in users:
            writer.writerow(data.values())

def read_post():
    pass

def write_post():
    pass
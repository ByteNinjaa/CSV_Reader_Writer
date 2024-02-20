import csv

data = [
        ['name', 'age', 'major'],
        ['alice', 24, 'computer science'],
        ['bob', 22, 'mathematics'],
        ['charlie', 23, 'physics']
    ]

filename = "data.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f'CSV file "{filename}" has been created successfully')


with open('data.csv', 'r') as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        print(row)


new_row = ['john', '20', 'Psychology']

with open('data.csv', 'a', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(new_row)

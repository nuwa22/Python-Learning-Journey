import csv

products = [
    ["Item", "Price"],
    ["Apple", 100],
    ["Banana", 50],
    ["Orange", 80]
]

with open("products.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerows(products)
print("CSV file saved successfully.")

with open("products.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
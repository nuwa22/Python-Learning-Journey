# write csv file

import csv

user_data = [
    ["Name", "Age", "City"],
    ["Suresh", 26, "Matugama"],
    ["Nuwan", 25, "Kalutara"],
    ["Tharaka", 27, "Colombo"]
]

# Open a CSV file for writing
with open("user_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(user_data)
print("CSV file saved successfully.")

with open("user_data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
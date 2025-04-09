import csv

with open("Weather.csv", "r") as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")

for row in data [1:0]:
    if row[0] == city:
        print(row[1])
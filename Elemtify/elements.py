from __init__ import element
import csv
import elements

elementList = []

with open("elements.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        elementList.append(element(row[0], row[1], row[2], row[3], row[4]))
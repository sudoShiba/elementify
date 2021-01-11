from __init__ import element
import csv
import pandas
import elements

while True:
    # Search Options
    print("Search options: ")
    print("Search by Atomic Symbol")
    print("Search by Atomic Number")
    print("Search by Atomic Weight")
    print("Search by English Name")
    print("Search by Dutch Name")

    searchOption = input().lower()

    if searchOption == "atomic number":
        # Search by atomic number
        atNum = int(input("Atomic number: "))

        df = pandas.read_csv("elements.csv", index_col="atNum")

        print(f"Atomic Symbol: {df.iloc[atNum - 1].atSym}")
        print(f"Atomic Weight: {df.iloc[atNum - 1].atWeight}")
        print(f"English Name:  {df.iloc[atNum - 1].ENname}")
        print(f"Dutch Name:    {df.iloc[atNum - 1].NLname}")
        
        print("=====================================")
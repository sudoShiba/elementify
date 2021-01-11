from __init__ import element
import csv
import pandas
import elements

atNum = int(input("Atomic number: "))

df = pandas.read_csv("elements.csv")

print(f"Atomic Symbol: {df.loc[atNum - 1].atSym}")
print(f"Atomic Number: {df.loc[atNum - 1].atNum}")
print(f"Atomic Weight: {df.loc[atNum - 1].atWeight}")
print(f"English Name:  {df.loc[atNum - 1].ENname}")
print(f"Dutch Name:    {df.loc[atNum - 1].NLname}")
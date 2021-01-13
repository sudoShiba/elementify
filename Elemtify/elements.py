import csv
import pandas

df = pandas.read_csv("elementsList.csv")

# mapping between search options and columns in the DataFrame
d = {
    'atomic symbol': 'atSym',
    'atomic number': 'atNum',
    'atomic weight': 'atWeight',
    'english name': 'ENname',
    'dutch name': 'NLname',
}

while True:
    # Search Options
    print("Search options: ")
    print("Search by Atomic Symbol")
    print("Search by Atomic Number")
    print("Search by Atomic Weight")
    print("Search by English Name")
    print("Search by Dutch Name")

    # get search option and select the right column to search on
    # we're converting the column to lowercase strings, so that
    # we can conveniently find it later
    searchOption = input("Search option: ").lower()
    df_ix = df[d[searchOption]].astype(str).str.lower()
    
    # get value to search for, convert to lowercase and find row
    searchValue = input("Search query: ").lower()
    row = df[df_ix==searchValue]
    
    # rename columns to human-readable based on our mapping and print
    print("==========================================================================")
    print(row.rename(columns={v: k for k, v in d.items()}))
    print("==========================================================================")
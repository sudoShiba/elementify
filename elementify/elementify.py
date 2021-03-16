import pandas

df = pandas.read_csv("elementsList.csv")


# declaring lines
def lines(input: str):
    print("=================================================================")
    print(input)
    print("=================================================================")


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

    try:
        # get search option and select the right column to search on
        # converting the column to lowercase strings, so that
        # it can conveniently be found later
        searchOption = input("Search option: ").lower()
        df_ix = df[d[searchOption]].astype(str).str.lower()

        # get value to search for, convert to lowercase and find row
        searchValue = input("Search query: ").lower()
        row = df[df_ix == searchValue]

        # renaming columns to human-readable based on our mapping and print
        lines(row.rename(columns={
            v: k for k, v in d.items()
            }).to_string(index=False))

    except KeyError:
        # tells user that an invalid search option/query was used
        lines("You can't use that as a search option/query")

    # asks if user wants to do another search
    if input("Search another? (y/n) ").lower() == "y":
        continue
    else:
        break

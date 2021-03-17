import pandas

df = pandas.read_csv("elementsList.csv")


# declaring lines
def lines(input):
    print("=================================================================")
    print(input)
    print("=================================================================")


# mapping between search options and columns in the DataFrame
d = {
    "atomic symbol": "atSym",
    "atomic number": "atNum",
    "atomic weight": "atWeight",
    "english name":"ENname",
    "dutch name": "NLname",
    "1": "atSym",
    "2": "atNum",
    "3": "atWeight",
    "4":"ENname",
    "5": "NLname"
}

while True:
    # Search Options
    print("Search options: ")
    print("1. Search by Atomic Symbol")
    print("2. Search by Atomic Number")
    print("3. Search by Atomic Weight")
    print("4. Search by English Name")
    print("5. Search by Dutch Name")

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

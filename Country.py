def display_menu():
    print("COMMAND MENU")
    print("view - View coulntry name")
    print("add - Add a country")
    print("del - Delete a country")
    print("exit - Exit program")
    print()

def display_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    codes_line = "Country codes: "
    for code in codes:
        codes_line += code + " "
    print(codes_line)

def view(countries):
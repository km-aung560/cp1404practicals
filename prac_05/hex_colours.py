"""Hex Colours"""

COLOURS_TO_HEX = {"Absolute Zero": "#0048ba", "Alizarin Crimson": "#e32636", "Celtic Blue": "#246bce",
                  "Chocolate": "#d2691e", "Electric Purple": "#bf00ff", "Ghost White": "#f8f8ff",
                  "Green Lizard": "#a7f432",
                  "Jasmine": "#f8de7e", "Magic Mint": "aaf0d1", "Wisteria": "c9a0dc"}

colour_name = input("Enter Colour name: ").title()
while colour_name != "":
    try:
        print(colour_name, "is", COLOURS_TO_HEX[colour_name])
    except KeyError:
        print("Invalid Colour name")
    colour_name = input("Enter Colour name: ").title()
print("Goodbye")

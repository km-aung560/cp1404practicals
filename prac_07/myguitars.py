"""More Guitars

1. Read each guitar from file, display guitars
2. sort list by year, display sorted list
3. Add user input, store into list
4. write guitars to file
"""
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = load_file()
    my_guitars = add_guitars(guitars)
    print(my_guitars)
    display_guitars(my_guitars)

def load_file():
    with open(FILENAME) as in_file:
        guitars = [line.strip().split(",") for line in in_file]
    return guitars


def add_guitars(guitars):
    """Store guitars as class objects"""
    my_guitars = []
    for guitar in guitars:
        name = guitar[0]
        year = guitar[1]
        cost = guitar[2]
        guitar_to_add = Guitar(name, year, cost)
        my_guitars.append(guitar_to_add)
    return my_guitars

def display_guitars(my_guitars):
    my_guitars.sort(reverse=1)
    for guitar in my_guitars:
        print(guitar)

main()

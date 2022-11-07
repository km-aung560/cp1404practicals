"""More Guitars

1. Read each guitar from file, display guitars
2. sort list by year, display sorted list
3. Add user input, store into list
4. write guitars to file
"""
from prac_07.guitar import Guitar
import csv

FILENAME = "guitars.csv"


def main():
    guitars = load_file()
    my_guitars = add_guitars(guitars)
    my_guitars = get_guitars(my_guitars)
    print(my_guitars)
    display_guitars(my_guitars)
    save_guitars(my_guitars)

def load_file():
    with open(FILENAME) as in_file:
        guitars = [line.strip().split(",") for line in in_file]
    return guitars


def add_guitars(guitars):
    """Store guitars from file as class objects"""
    my_guitars = []
    for guitar in guitars:
        name = guitar[0]
        year = guitar[1]
        cost = guitar[2]
        guitar_to_add = Guitar(name, year, cost)
        my_guitars.append(guitar_to_add)
    return my_guitars

def get_guitars(my_guitars):
    """Get guitars from user input and store as class objects"""
    name = input("Name: ")
    while name != "":
        year = (input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        my_guitars.append(guitar_to_add)
        print(f"{name} ({year}) : ${cost} added\n")
        name = input("Name: ")
    return my_guitars

def display_guitars(my_guitars):
    """Display guitars, sorted by year"""
    my_guitars.sort(reverse=1)
    for guitar in my_guitars:
        print(guitar)

def save_guitars(my_guitars):
    with open(FILENAME, "w", encoding="UTF8", newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(my_guitars)
        print(f"{len(my_guitars)} guitars saved to {FILENAME}")

main()

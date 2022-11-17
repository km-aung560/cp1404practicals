"""Project Management
Estimate: 60 mins
Actual:

"""
from prac_07.project import Project

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new " \
       "project\n- (U)pdate project\n- (Q)uit "
FILENAME = "projects.txt"
HEADER = "Name	Start Date	Priority	Cost Estimate	Completion Percentage"


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            # filename = input("filename: ")
            projects = load_file()
            print(projects)
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def load_file():
    with open(FILENAME, encoding="UTF8") as in_file:
        projects = [line.strip().replace("\t", ",").split(',') for line in in_file]
        projects.remove(projects[0])
    return projects

    # def display_projects():
    # find all incomplete projects
    # sort incomplete projects
    # print incomplete projects
    #
    # find all complete projects
    # sort complete projects
    # print complete projects


main()

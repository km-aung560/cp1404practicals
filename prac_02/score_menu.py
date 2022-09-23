""" Menu """

"""
function get_valid_score
display menu
get choice
while choice != Q
   if choice == R
       function print_result
   else if choice == S
       function print_stars
   else
       display invalid message
   display menu
   function get_valid_score
display finished message


"""
MENU = "(R)esult\n(S)tars\n(Q)uit"


def main():
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "R":
            print_result(score)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_score():
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def print_result(score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def print_stars(score):
    print("*" * score)


main()

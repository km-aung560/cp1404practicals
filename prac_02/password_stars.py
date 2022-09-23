""" Password Check with Functions """

MIN_LENGTH = 10


def main():
    """ Main function for Password Check"""
    password = input("Enter password: ")
    password = get_password(password)
    print_stars(password)


def get_password(password):
    """ Gets valid password"""
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input("Enter password: ")
    return password


def print_stars(password):
    """ Prints stars"""
    print("*" * len(password))


main()

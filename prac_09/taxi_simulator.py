"""
Taxi Simulator Program
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            taxis = display_taxis(taxis)
            current_taxi = choose_taxi(taxis)
            print(current_taxi)
        elif choice == "d":
            drive_taxi(current_taxi)
        else:
            print("Invalid option")
            print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    return taxis


def choose_taxi(taxis):
    is_valid_taxi_index = False
    while not is_valid_taxi_index:
        try:
            taxi_choice = int(input("Choose taxi: "))
            if taxi_choice < 0:
                print("Number must be >= 0")
            elif taxi_choice > len(taxis):
                print("Invalid taxi choice")
            else:
                current_taxi = taxis[taxi_choice]
                is_valid_taxi_index = True
                return current_taxi
        except IndexError:
            print("Invalid input; enter a valid number")


def drive_taxi(current_taxi):
    if current_taxi:
        current_taxi.start_fare()
        distance = float(input("Drive how far?: "))
        current_taxi.drive(distance)
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
    else:
        print("You need to choose a taxi before you can drive")


main()

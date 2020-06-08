from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_bill = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("let's drive!" "\n" + MENU)

    menu_choice = input(">>>").lower()
    while menu_choice != "q":

        if menu_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose Taxi: "))
            current_taxi = taxis[taxi_choice]
        elif menu_choice == "d":
            current_taxi.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            current_taxi.drive(distance_to_drive)
            trip_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
            total_bill += trip_cost

        else:
            print("invalid option")
        print("Total bill: ${:.2f}".format(total_bill) + "\n" + MENU)
        menu_choice = input(">>>").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now: " "\n")
    display_taxis(taxis)


def display_taxis(taxis):

    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, str(taxi)))


main()

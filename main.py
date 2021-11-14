from club import Club
import time

# clubs_list = [{'name': 'ABC', 'city': 'LKO', 'address': 'ADDDD', 'timings': '10-18', 'slots': ['10 - 11', '11 - 12', '12 - 13', '13 - 14', '14 - 15', '15 - 16', '16 - 17', '17 - 18']}]
clubs_list = []


def remove_slot(chosen_slot, city):
    # print(chosen_slot)
    for item in clubs_list:
        if item['city'] == city:
            # print("Item: ", item)
            if chosen_slot in item['slots']:
                item['slots'].remove(chosen_slot)
                # print(item)


def book_slot(chosen_slot, slots_ava, city):
    # print(chosen_slot, slots_ava, city)
    if chosen_slot in slots_ava:
        print("Booked")
        remove_slot(chosen_slot, city)
    else:
        print("Slot not available. Please book another slot")
    # pass


def show_slots_available(slots_available):
    count = 0
    for slot in slots_available:
        count += 1
        print(f"{count} : {slot}")


def slots(timings):
    # print(timings)
    slots_available = timings.split('-')
    count = 0
    slots_ava = []
    # print(slots_available)
    for slot in range(int(slots_available[0]), int(slots_available[1])):
        count += 1
        print(f"{count} : {slot} - {slot+1}")

        slots_ava.append(f"{slot} - {slot+1}")
    return slots_ava


def boiler_code():
    facilities = ['Register a club', 'View all clubs', 'Book a slot', 'Cancel a slot', 'Quit']
    print("Hi!!\nWelcome to this app\n")
    print("Facilities available are: ")
    ind = 0
    for item in facilities:
        ind += 1
        print(f"{ind} : {item}")

    while True:
        try:
            print("\nWaiting for user input")
            option = int(input("Choose a facility: "))
            if option == 1:
                new_club = Club()
                club = new_club.register_club()
                # slots_ava = slots(club['timings'])

                clubs_list.append(club)

                # print("Inside 1st: ", slots_ava)

            elif option == 2:

                count = 0
                # print(clubs_list)
                if len(clubs_list):
                    print("Clubs available are:")
                    for club in clubs_list:
                        # print(club)
                        count += 1
                        print(f"{count}: Name: {club['name']}\n"
                              f"City: {club['city']}\n"
                              f"Address: {club['address']}\n"
                              f"Timings: {club['timings']}")
                else:
                    print("Please add a club")

            elif option == 3:
                print("Please choose a city:\n Available cities are:")
                count = 0
                cities = []
                for item in clubs_list:
                    count += 1
                    print(f"{count} : {item['city']}")
                    cities.append(item['city'])

                city = str(input("Please choose a city: "))
                # print(cities)

                if city not in cities:
                    print("City unavailable")
                else:
                    for item in clubs_list:
                        if item['city'] == city:
                            # print(item)
                            slots_ava = item['slots']
                            # print(slots_ava)
                            show_slots_available(slots_ava)
                            slot = str(input("Please choose a slot: "))
                            book_slot(slot, slots_ava, item['city'])

            elif option == 4:
                pass
            elif option == 5:
                print("\n\n###### Thank you for using the app... ######")
                print("###### Designed by Sachin Mehndiratta ######")
                print("____________________________________________\n\n")
                print("Quiting in: ")
                for i in reversed(range(5)):
                    print(f"{i + 1}")
                    time.sleep(1)
                print("Bye!!")
                exit()
            else:
                print("###### That's a wrong input. Please choose the correct input... ######\n")
        except Exception as e:
            print(f"That's a wrong set of input. Please input in range(1-{len(facilities)})\n", e)


def main():
    boiler_code()

    list_of_clubs = []


if __name__ == '__main__':
    main()

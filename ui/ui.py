from random import randint

from domain.entities import Room, Reservation, date


class UI:
    def __init__(self, controller):
        self.__controller = controller

    @staticmethod
    def print_menu():
        print("1. Create reservation")
        print("2. List all reservations")
        print("3. Delete reservation")
        print("4. Show available rooms")
        print("0. Exit")

    def main(self):
        ok = True
        while ok:
            UI.print_menu()
            option = input("Enter option: ")
            if option == '1':
                index = 0
                fam_name = input("Enter family name: ")
                room_type = input("Enter room type: ")
                nr_guests = int(input("Enter number of guests: "))
                arr_date_month = input("Enter arrival date month (mm): ")
                arr_date_day = input("Enter arrival date day (dd): ")
                dep_date_month = input("Enter departure date month (mm): ")
                dep_date_day = input("Enter departure date day (dd): ")
                free = self.__controller.get_all_free()
                for room in free:
                    if str(room.get_type()) == str(room_type) and index == 0:
                        reserve_room = Room(room.get_number(), room.get_type())
                        self.__controller.remove_free(room.get_number())
                        self.__controller.add_occupied(reserve_room)
                        index = 1
                if index == 0:
                    print("No free room of the specified type!")
                else:
                    r_id = UI.generate_id()
                    try:
                        self.__controller.add_reservation(Reservation(r_id, reserve_room.get_number(), fam_name, nr_guests, date(arr_date_month, arr_date_day), date(dep_date_month, dep_date_day)))
                    except ValueError as ve:
                        print(ve)
            elif option == '2':
                for index in self.__controller.get_all_reservation():
                    print(index)
            elif option == '3':
                r_id = int(input("Enter a 4 digit id: "))
                reservations = self.__controller.get_all_reservation()
                for reservation in reservations:
                    if reservation.get_r_id() == r_id:
                        for index in self.__controller.get_all_occupied():
                            if index.get_number() == reservation.get_room_nr():
                                r_type = index.get_type()
                        self.__controller.remove_occupied(reservation.get_room_nr())
                        self.__controller.add_free(Room(reservation.get_room_nr(), r_type))
                        self.__controller.remove_reservation(r_id)
                    else:
                        print("Reservation with this id does not exist!")
            elif option == '4':
                for index in self.__controller.get_all_free():
                    print(index)
            elif option == '0':
                return

    @staticmethod
    def read_reservation():
        fam_name = input("Enter family name: ")
        room_type = input("Enter room type: ")
        nr_guests = int(input("Enter number of guests: "))
        arr_date_month = input("Enter arrival date month (mm): ")
        arr_date_day = input("Enter arrival date day (dd): ")
        dep_date_month = input("Enter departure date month (mm): ")
        dep_date_day = input("Enter departure date day (dd): ")
        return fam_name, room_type, nr_guests, arr_date_month, arr_date_day, dep_date_month, dep_date_day

    @staticmethod
    def generate_id():
        r_id = randint(1000, 9999)
        return r_id

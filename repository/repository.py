class RoomRepo:
    def __init__(self):
        self.__data = []

    def add_room(self, room):
        self.__data.append(room)

    def remove_room(self, nr):
        index = 0
        while self.__data[index].get_number() != nr:
            index += 1
        self.__data.pop(index)

    def get_all(self):
        return self.__data


class ReservationRepo:
    def __init__(self):
        self.__data = []

    def add_reservation(self, reserv):
        self.__data.append(reserv)

    def remove_reservation(self, r_id):
        index = 0
        while self.__data[index].get_r_id() != r_id:
            index += 1
        self.__data.pop(index)

    def get_all(self):
        return self.__data


class OccupiedRooms:
    def __init__(self):
        self.__data = []

    def add_room(self, room):
        self.__data.append(room)

    def remove_room(self, nr):
        index = 0
        while self.__data[index].get_number() != nr:
            index += 1
        self.__data.pop(index)

    def get_all(self):
        return self.__data

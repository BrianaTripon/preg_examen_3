class ReservationController:
    def __init__(self, reservation_repo, room_repo, occupied_repo):
        self.__reservation_repo = reservation_repo
        self.__room_repo = room_repo
        self.__occupied_repo = occupied_repo

    def add_reservation(self, r):
        reservations = self.__reservation_repo.get_all()
        for reservation in reservations:
            if reservation.get_room_nr() == r.get_room_nr():
                raise ValueError("Room is not available")
        if int(r.get_arr_date().get_month()) > int(r.get_dep_date().get_month()) or (int(r.get_arr_date().get_month()) == int(r.get_dep_date().get_month()) and int(r.get_arr_date().get_day()) > int(r.get_dep_date().get_day())):
            raise ValueError("Invalid dates")
        self.__reservation_repo.add_reservation(r)

    def add_free(self, r):
        self.__room_repo.add_room(r)

    def add_occupied(self, r):
        self.__occupied_repo.add_room(r)

    def remove_free(self, nr):
        self.__room_repo.remove_room(nr)

    def remove_reservation(self, r_id):
        self.__reservation_repo.remove_reservation(r_id)

    def remove_occupied(self, nr):
        self.__occupied_repo.remove_room(nr)

    def get_all_free(self):
        return self.__room_repo.get_all()

    def get_all_occupied(self):
        return self.__occupied_repo.get_all()

    def get_all_reservation(self):
        return self.__reservation_repo.get_all()

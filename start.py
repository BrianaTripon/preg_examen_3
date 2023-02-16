from controller.controller import ReservationController
from domain.entities import Room, Reservation
from repository.repository import ReservationRepo, RoomRepo, OccupiedRooms
from ui.ui import UI

reservation_repo = ReservationRepo()
free = RoomRepo()
occupied = OccupiedRooms()

free.add_room(Room(1, "family"))
free.add_room(Room(2, "double"))
free.add_room(Room(3, "single"))
free.add_room(Room(4, "family"))
free.add_room(Room(5, "double"))
free.add_room(Room(6, "single"))
free.add_room(Room(7, "family"))
free.add_room(Room(8, "double"))
free.add_room(Room(9, "single"))
free.add_room(Room(10, "family"))


controller = ReservationController(reservation_repo, free, occupied)
ui = UI(controller)
ui.main()

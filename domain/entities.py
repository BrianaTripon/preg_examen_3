class date:
    def __init__(self, day, month):
        self.__day = day
        self.__month = month

    def get_day(self):
        return self.__day

    def get_month(self):
        return self.__month

    def __str__(self):
        s = ''
        s += self.__month
        s += '.'
        s += self.__day
        return s


class Room:
    def __init__(self, number, r_type):
        self.__number = number
        self.__r_type = r_type

    def get_number(self):
        return self.__number

    def get_type(self):
        return self.__r_type

    def __str__(self):
        s = ''
        s += str(self.__number)
        s += ' '
        s += self.__r_type
        return s


class Reservation:
    def __init__(self, r_id, room_nr, family_name, nr_guests, arr_date, dep_date):
        self.__r_id = r_id
        self.__room_nr = room_nr
        self.__family_name = family_name
        self.__nr_guests = nr_guests
        self.__arr_date = arr_date
        self.__dep_date = dep_date

    def get_r_id(self):
        return self.__r_id

    def get_room_nr(self):
        return self.__room_nr

    def get_family_name(self):
        return self.__family_name

    def get_nr_guests(self):
        return self.__nr_guests

    def get_arr_date(self):
        return self.__arr_date

    def get_dep_date(self):
        return self.__dep_date

    def __str__(self):
        s = ''
        s += str(self.__r_id)
        s += ' '
        s += str(self.__room_nr)
        s += ' '
        s += str(self.__family_name)
        s += ' '
        s += str(self.__nr_guests)
        s += ' '
        s += str(self.__arr_date)
        s += ' '
        s += str(self.__dep_date)
        return s



# class date():
#     def __init__(self, d, m):
#         self.__d = d
#         self.__m = m
#
#     def getDay(self):
#         return self.__d
#
#     def getMounth(self):
#         return self.__m
#
#     def __str__(self):
#         s = ''
#         s += self.__m
#         s += '.'
#         s += self.__d
#         return s
#
#
# class Room():
#     def __init__(self, Nr, Type):
#         self.__Nr = Nr
#         self.__Type = Type
#
#     def getNr(self):
#         return self.__Nr
#
#     def getType(self):
#         return self.__Type
#
#     def __str__(self):
#         s = ''
#         s += str(self.__Nr)
#         s += ' '
#         s += str(self.__Type)
#         return s
#
#
# class Reservation():
#     def __init__(self, ID, roomNr, famName, nrGuests, adate, ddate):
#         self.__ID = ID
#         self.__roomNr = roomNr
#         self.__famName = famName
#         self.__nrGuests = nrGuests
#         self.__adate = adate
#         self.__ddate = ddate
#
#     def getID(self):
#         return self.__ID
#
#     def getRoomNr(self):
#         return self.__roomNr
#
#     def getFam(self):
#         return self.__famName
#
#     def getGuests(self):
#         return self.__nrGuests
#
#     def getAdate(self):
#         return self.__adate
#
#     def getDdate(self):
#         return self.__ddate
#
#     def __str__(self):
#         s = ''
#         s += str(self.__ID)
#         s += ' '
#         s += str(self.__roomNr)
#         s += ' '
#         s += str(self.__famName)
#         s += ' '
#         s += str(self.__nrGuests)
#         s += ' '
#         s += str(self.__adate)
#         s += ' '
#         s += str(self.__ddate)
#         return s
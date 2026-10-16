# TODO: Implementing theater into main will automatically implement seat into the project too.
class Seat:
    def __init__(self, seat_label, seat_type = "Regular", price = 50000):
        self.seat_label = seat_label # Seat name, e.g. A1, B2, C3
        self.seat_type = seat_type
        self.is_reserved = False
        self.price = price

    def reserve(self):
        if self.is_reserved == True: # if the seat is reserved. Return false.
            return False
        elif self.is_reserved == False: # if the seat is not reserved. Reserve it and return true.
            self.is_reserved = True
            return True

    def cancel_reservation(self): # Opposite of how reserve function works. That's why it seems similar.
        if self.is_reserved == True: # if the seat is reserved. Cancel it and return true.
            self.is_reserved = False
            return True
        elif self.is_reserved == False: # if the seat is not reserved. Return false.
            return False

# TODO: Implement different types of seats on the theater with different pricings.
# class SleeperSeat(Seat):
#     def __init__(self, seat_label):
#         super().__init__(seat_label, seat_type = "Sleeper", price = 85000) # Calls on Seat's constructor. Uses inheritance. Is only used to give a different seat type and pricing.

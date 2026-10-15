from seat import Seat

# TODO: Implement Theater into main. Implementing object oriented programming and inheritance into the project.
class Theater:
    def __init__(self, rows, cols):
        self.seats = []
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for i in range(rows):
            row_letter = letters[i]
            current_row = []

            for j in range(cols):
                seat_number = j + 1 # +1 because list is 0-indexed. Seat numbers start at 1 not 0.
                seat_label = row_letter + str(seat_number) # Seat name so it looks like A1, B2, C3, etc.
                new_seat = Seat(seat_label)
                current_row.append(new_seat)

            self.seats.append(current_row)

    def display_seats(self):
        for i in self.seats:
            for j in i:
                print(j.seat_label, end=" ")
            print()

    # Find seat function. Automatically used inside reserve_seat. Doesn't need to be used independently.
    def find_seat(self, seat_label):
        for i in self.seats:
            for j in i:
                if j.seat_label == seat_label:
                    return j
        return None # Returns nothing if the seat the user typed in doesn't exist.
    
    def reserve_seat(self, seat_label):
        chosen_seat = self.find_seat(seat_label) # Checks if the seat exists

        while True:
            if chosen_seat is None:
                return "That seat doesn't exist. Please try again."
            else:
                seat_reservation_result = chosen_seat.reserve()
                if seat_reservation_result == True:
                    return f"Reservation successful!\nSeat {seat_label} has been reserved for you."
                else:
                    return f"Reservation failed!\nSeat {seat_label} is already booked. Please select a different seat."

    def cancel_reservation(self, seat_label):
        chosen_seat = self.find_seat(seat_label)

        if chosen_seat is None:
            return "That seat doesn't exist. Please try again."
        else:
            seat_cancellation_result = chosen_seat.cancel_reservation()
            if seat_cancellation_result == True:
                return f"Cancellation successful!\nReservation of seat {seat_label} has been cancelled."
            else:
                return f"Cancellation failed!\nSeat {seat_label} is not reserved. Please select a different seat."

# TODO: Try the display seats function without implementing main.py. Just to remind myself what I was doing with the project.

theater = Theater(3, 4)
print("Welcome to the Movie Theater!\nHere are the available seats:")
theater.display_seats()

# Testing
for row in theater.seats:
    for seat in row:
        print(seat.seat_label, seat.seat_type, seat.is_reserved)
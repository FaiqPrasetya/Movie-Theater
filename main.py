from theater import Theater

# User Interface
print("Welcome to the Movie Theater!\nHere are the available seats:")
theater = Theater(3,4) # Declare theater object. 3 rows and 4 columns
theater.display_seats() # Display seats.
while True:
    seat_label = input("Please pick a seat (e.g A1, B2, C3): ").strip().upper() # strip removes spaces. upper makes the input uppercase for the seat label.
    # TODO: Implement showing seat pricing before confirming reservation
    reservation_result = theater.reserve_seat(seat_label) # Check if the seat exists. Throws an error if the seat doesn't exist.
    print(reservation_result)

    # Booking cancellation
    choice = input("Do you want to cancel your reservation? (Y/N): ").strip().upper()
    if choice == 'Y':
        reservation_result = theater.cancel_reservation(seat_label)
        print(reservation_result)

    # Booking another seat
    choice = input("Do you want to book another seat? (Y/N): ").strip().upper()
    if choice == 'N':
        break
    elif choice == 'Y':
        theater.display_seats() # # TODO: Make it so that the displayed seats are only the available seats.
    else:
        print("Invalid input.")

# List of seating arrangements for the movie theater.
# TODO: Static. Make it dynamic later by using rows and columns to create the seating with a for loop. For concept, static list will do for now.
seats = [
    ['A1', 'A2', 'A3', 'A4'], # Regular seats
    ['B1', 'B2', 'B3', 'B4'], # Sleeper seats
    ['C1', 'C2', 'C3', 'C4'], # Regular seats
    ]

seats_reserved = [
    [False, False, False, False], # Regular seats
    [False, False, False, False], # Sleeper seats
    [False, False, False, False], # Regular seats
]

# User Interface
print("Welcome to the Movie Theater!")
print("Here are the available seats:")

for i in range(0,3): # Columns
    for j in range(0,4): # Rows
        print(f"{seats[i][j]}", end=" ") # End functions the same as System.out.print in Java.
                                         # Not using end acts as if you're typing System.out.println in Java.
                                         # Where typing end="" means that the next print statement will be on the same line.
    print()

while True:
    row = input("Please select a seat row (A = 1, B = 2, C = 3): ").strip()
    col = input("Please select a seat column (1-4): ").strip()

    if (seats_reserved[int(row) - 1][int(col) - 1] == False):
        seats_reserved[int(row) - 1][int(col) - 1] = True # -1 Because the list is 0-indexed.
        print(f"Seat {seats[int(row) - 1][int(col) - 1]} has been reserved for you.")
        break
    elif (seats_reserved[int(row) - 1][int(col) - 1] == True):
        print("That seat is already reserved. Please select a different seat.")
    else:
        print("That seat does not exist. Please try again.")

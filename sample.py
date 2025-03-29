class Vehicle:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.seats = [False] * total_seats  # False indicates the seat is vacant

    def book_seat(self, seat_number):
        if 0 <= seat_number < self.total_seats:
            if not self.seats[seat_number]:
                self.seats[seat_number] = True
                print(f"Seat {seat_number} has been booked.")
            else:
                print(f"Seat {seat_number} is already booked.")
        else:
            print("Invalid seat number.")

    def cancel_seat(self, seat_number):
        if 0 <= seat_number < self.total_seats:
            if self.seats[seat_number]:
                self.seats[seat_number] = False
                print(f"Seat {seat_number} has been canceled.")
            else:
                print(f"Seat {seat_number} is already vacant.")
        else:
            print("Invalid seat number.")

    def available_seats(self):
        vacant_seats = [index for index, seat in enumerate(self.seats) if not seat]
        return vacant_seats

    def display_seat_status(self):
        for index, seat in enumerate(self.seats):
            status = "Vacant" if not seat else "Booked"
            print(f"Seat {index}: {status}")

#  if name == "main":

vehicle = Vehicle(total_seats=5)



vehicle.display_seat_status()

print("Available seats:", vehicle.available_seats())sdf 



vehicle.book_seat(2)

vehicle.book_seat(4)

vehicle.display_seat_status()

print("Available seats:", vehicle.available_seats())



vehicle.cancel_seat(2)

vehicle.display_seat_status()

print("Available seats:", vehicle.available_seats())

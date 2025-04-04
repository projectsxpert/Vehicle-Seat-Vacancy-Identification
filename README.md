# Vehicle-Seat-Vacancy-Identification
This document provides a sample Python code for identifying seat vacancies in a vehicle. The code is designed to help users determine which seats are available in a vehicle based on a predefined seating arrangement. This can be particularly useful for applications in transportation services, ride-sharing platforms, or any system that requires seat management.



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



if name == "main":

vehicle = Vehicle(total_seats=5)



vehicle.display_seat_status()

print("Available seats:", vehicle.available_seats())



vehicle.book_seat(2)

vehicle.book_seat(4)

vehicle.display_seat_status()

print("Available seats:", vehicle.available_seats())



vehicle.cancel_seat(2)

vehicle.display_seat_status()

print("Available seats:", vehicle.available_seats())


This sample code defines a `Vehicle` class that manages seat bookings. It includes methods to book and cancel seats, check available seats, and display the current status of each seat. The example usage at the bottom demonstrates how to create a vehicle instance, book and cancel seats, and check the availability of seats.


 To get more information: https://projectsxpert.com/project/873/advanced-arduino-based-vehicle-seat-vacancy-identification

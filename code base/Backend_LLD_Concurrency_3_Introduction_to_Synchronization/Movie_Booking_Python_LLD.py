'''
Movie Ticket Booking
Consider an online reservation system for booking tickets for a movie hall. The system needs to handle concurrent requests from multiple
users trying to reserve seats. To ensure thread safety and prevent race conditions, a Reentrant Lock can be employed. You can assume there
is only one movie for which people are trying to book tickets.

Requirements:
The reservation system manages the availability of seats for a movie hall.
Multiple users can attempt to reserve seats concurrently.
A user should be able to reserve multiple seats in one booking.
The system should prevent overbooking and ensure the integrity of seat reservations.
MovieTicketBookingSystem Class
Instance Variables:
available_seats: An integer representing the total number of available seats for the movie.
lock: A ReentrantLock used to ensure thread safety when modifying the availableSeats.
total_seats: An integer denoting the total number of seats available for reservation.
Constructor:
Initializes the available_seats and total_seats with the total number of seats provided as an argument.
Creates a ReentrantLock instance to be used for synchronization.
reserve_seats Method:
Takes an integer num_seats as a parameter representing the number of seats a user wants to reserve.
Acquires the reservationLock using self.lock to ensure that only one thread can modify the availableSeats at a time.
Checks if there are enough available seats:
If there are enough seats, it decrements the availableSeats by num_seats and returns True.
If there are not enough seats, it returns False.
get_available_seats Method:
Returns the current number of available seats for the movie.
Summary
This simplified implementation manages the reservation of seats for a single movie, with the total number of available seats represented as an integer.
Thread safety is ensured using a ReentrantLock, allowing multiple users to reserve seats concurrently while preventing race conditions.
The reserve_seats method allows users to reserve seats, and the get_available_seats method provides information about the remaining available seats.
'''
import threading
from concurrent.futures import ThreadPoolExecutor

class MovieTicketBookingSystem:

    def __init__(self, total_seats: int):
        self._available_seats = total_seats
        self._total_seats = total_seats
        self._lock = threading.Lock()


    def reserve_seats(self, num_seats : int)-> bool:
        with self._lock:
            if self._available_seats >= num_seats:
                self._available_seats -=num_seats
                return True
            else: return False

    def get_available_seats(self)-> int:
        with self._lock:
            return self._available_seats

if __name__ =="__main__":
    total_seats = 10
    booking_system = MovieTicketBookingSystem(total_seats)
    print(f"Total seats available: {booking_system.get_available_seats()}")

    num_seats_to_reserve = 11
    if booking_system.reserve_seats(num_seats_to_reserve):
        print(f"Successfully reserved {num_seats_to_reserve} seats.")
    else:
        print(f"Failed to reserve {num_seats_to_reserve} seats. Not enough available seats.")


    # with multiple threads
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for _ in range(10):
            futures.append(executor.submit(booking_system.reserve_seats, 2))

        for future in futures:
            if future.result():
                print("Reservation successful.")
            else:
                print("Reservation failed. Not enough seats available.")

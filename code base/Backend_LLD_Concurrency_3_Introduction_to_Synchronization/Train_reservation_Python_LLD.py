'''
Train Reservation System (Assignment)
Consider an online reservation system for booking tickets for an Indian train system. The system needs to handle concurrent requests
from multiple users trying to reserve seats. To ensure thread safety and prevent race conditions, a Reentrant Lock can be employed.

Requirements:
The reservation system manages the availability of seats for different seat types on Indian trains, including 1AC, 2AC, 3AC, and Sleeper.
You can assume all seats types are available in the train.
Multiple users can attempt to reserve seats concurrently.
A user should be able to reserve multiple seats of the same seat type.
The system should prevent overbooking and ensure the integrity of seat reservations
ReservationSystem Class
Instance Variables:
available_seats: A Map that stores the available seats for each seat type. The key is the seat type and the value is the number of available
 seats for that particular seat type.
lock: A Reentrant lock which ensures that only one thread can modify the available seats for any seat type at a time.
Constructor:
Initializes the available_seats and lock based on the provided initial available seats.
reserve_seats Method:
Takes two parameters: the seat_type and num_seats (the number of seats to reserve).
Acquires the lock using self.lock to ensure that only one thread can modify the available seats for the seatType at a time.

Checks if there are enough available seats for the reservation.

If there are enough seats, it decrements the available seats for the particular seat type and returns True.

If there are not enough seats, it returns False.

get_available_seats Method:
Takes the seat_type as a parameter and returns the number of available seats of that seat type.
'''
import threading


class ReservationSystem:

    def __init__(self, initial_seats: dict):
        self.available_seats = initial_seats.copy()
        self._lock = threading.RLock()

    def reserve_seats(self, seat_type, num_seats)-> bool:

        with self._lock:
            if seat_type not in self.available_seats:
                raise ValueError("Invalid seat type. Choose from '1AC', '2AC', '3AC', or 'Sleeper'.")
            else:
                if self.available_seats[seat_type] >= num_seats:
                    self.available_seats[seat_type] -= num_seats
                    return True
                else:
                    return False

    def get_available_seats(self, seat_type)->int:
        with self._lock:
            if seat_type not in self.available_seats:
                raise ValueError("Invalid seat type. Choose from '1AC', '2AC', '3AC', or 'Sleeper'.")
            else:
                return self.available_seats[seat_type]


if __name__ == "__main__":
    initial = {"1AC": 5, "2AC": 10, "3AC": 20, "Sleeper": 50}
    system = ReservationSystem(initial)

    print("Before booking 1AC:", system.get_available_seats("1AC"))
    if system.reserve_seats("1AC", 3):
        print("Successfully booked 3 1AC seats.")
    else:
        print("Failed to book 3 1AC seats.")

    print("After booking 1AC:", system.get_available_seats("1AC"))




'''
Facade pattern for a travel booking platform
Problem Statement
You are working on an online booking platform for travel accommodations. The platform needs to handle bookings, payments,
and notifications through different external services. The goal is to provide a simplified interface for customers and
internal modules to perform booking-related tasks without directly dealing with the intricacies of each external service.

Assignment
Your task is to implement the Facade pattern to refactor the existing BookingManager class. The BookingManager class has
multiple dependencies and methods that handle bookings, payments, and notifications. Your goal is to create a facade class
that provides a unified and simplified interface for these complex operations.

Implementing the Facade Pattern
Review the original class: Take a closer look at the BookingManager class and its methods. Understand the dependencies
it uses and the interactions with external services.

Create the facade class: Create a new class called BookingFacade that implements the Facade pattern. This class will
encapsulate the complex interactions with the external services and provide a simplified interface for clients.

Remember to call the constructor of your facade using the same arguments from the BookingManager class: The constructor
of your BookingFacade class should take the same arguments that the BookingManager class constructor does. This allows
you to pass the necessary dependencies to the facade.

Test your implementation: Test cases have been provided for you to test your implementation. Run the test cases to ensure
that your facade class works correctly and provides the expected functionality.
'''

# flow
'''
(CLIENT)
┌───────────────────────────┐
│   Travel Booking Platform │
└───────────────────────────┘
            │
            ▼
      (FACADE INTERFACE)
┌───────────────────────────┐
│      BookingFacade        │
├───────────────────────────┤
│ + book_trip(customer,     │
│    trip_details, payment) │
│ + cancel_booking(booking) │
│ + get_booking_status(id)  │
└───────────────────────────┘
            │
            ▼
┌───────────────────────────┐
│    BookingManager         │
├───────────────────────────┤
│ + create_booking(...)     │
│ + process_payment(...)    │
│ + send_notification(...)  │
│ + check_availability(...) │
└───────────────────────────┘
      ▲           ▲           ▲
      │           │           │
      │           │           │
      │           │           │
┌─────────┐ ┌──────────────┐ ┌───────────────┐
│ Booking │ │ Payment      │ │ Notification  │
│ Service │ │ Service      │ │ Service       │
│         │ │              │ │               │
└─────────┘ └──────────────┘ └───────────────┘
'''



# services: bookings, payments, notifications

# Step1: create services

class BookingService:

    def createBooking(self, userId:int, bookingInfo:dict)->str:
        return "Booking Created"

class PaymentService:

    def pay(self, userId:int, amount:float)->str:
        return "Payment Successful"

class Notification:

    def notify(self, userId:int, message:str)->str:
        return "Notification Sent"

class BookingFacade:

    def __init__(self, userId:int):
        self.userId = userId
        self.booking_service = BookingService()
        self.payment_service = PaymentService()
        self.notification_service = Notification()

    def accommodationBooking(self, bookingInfo:dict, amount:float):

        booking_status = self.booking_service.createBooking(self.userId, bookingInfo)
        payment_status = self.payment_service.pay(self.userId,amount)
        notification_status = self.notification_service.notify(self.userId,"Notification")

        return booking_status, payment_status, notification_status


# client
class Client:

    @staticmethod
    def bookAccommodation(userId:int, bookingInfo:dict, amount:float):
        facade = BookingFacade(userId)
        return facade.accommodationBooking(bookingInfo, amount)

if __name__ == "__main__":
    userId = 1
    bookingInfo = {"hotel":"xyz", "date":"2023-10-10"}
    amount = 100.0
    result = Client.bookAccommodation(userId, bookingInfo, amount)
    print(result)
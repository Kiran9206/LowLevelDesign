'''
Adapter Pattern for Insurance Providers Integration
Problem Statement
Your company needs to integrate with various insurance providers, each having different APIs and data formats.
To simplify the integration and ensure a consistent data format, you decide to implement the Adapter pattern.
This pattern will allow you to create adapter classes for different insurance providers, converting their APIs into a
common format that your application can use.

Assignment
Your task is to implement the Adapter pattern to create adapter classes for different insurance providers' APIs.
These adapters should conform to a common interface, making it easy to integrate new providers in the future. Your goal is
to abstract away the differences in APIs and data formats and provide a unified interface for your application to work with.

Implementing the Adapter Pattern
Review the existing APIs: Study the APIs and data formats of the insurance providers you need to integrate with.
Understand the differences in their APIs and how they interact with their respective systems.

Implement the adapter interface: You have been provided with an TravelInsuranceAdapter interface. Your task is to
implement this interface in different adapter classes, each corresponding to a different insurance provider. The
adapters should adapt the provider-specific APIs into a format that matches the TravelInsuranceAdapter interface.

Use composition: Create adapter classes that internally use instances of the actual insurance provider APIs. You should
not modify the provider APIs directly. Instead, create methods in the adapter classes that map to the provider APIs and
perform the necessary transformations.

Test your implementation: Run the provided test cases in the TravelInsuranceAdapterTest class to ensure that your adapter
classes work correctly. These test cases will check if your adapters have the required methods and if they interact with
the provider APIs properly.
'''

# steps
# step1: identify the target interface/client requirement...
# step2: identify the adaptee/existing interface...
# step3: create the adapter class that implements the target interface and uses the adaptee...
# step4: implement the methods in the adapter class to call the adaptee methods and perform any necessary transformations...
# step5: test the adapter class to ensure it works as expected...
# step6: integrate the adapter class into the client code...
# step7: document the adapter class and its usage for future reference...
# step8: maintain and update the adapter class as needed when the adaptee or target interface changes...

'''
(CLIENT)
┌─────────────────────┐
│  Your
Application   │
└─────────────────────┘
│
▼
(TARGET INTERFACE)
┌────────────────────────────┐
│ TravelInsuranceAdapter     │
├────────────────────────────┤
│ + get_quote(...)           │
│ + book_insurance(...)      │
└────────────────────────────┘
▲
┌────────────────┴──────────────┐
│                               │
(ADAPTER)     │                               │     (ADAPTER)
┌────────────────────┐                 ┌────────────────────────┐
│ ProviderAAdapter   │                 │ ProviderBAdapter       │
├────────────────────┤                 ├────────────────────────┤
│ + get_quote(...)   │◄──────────────┐ │ + get_quote(...)       │◄──────────────┐
│ + book_insurance() │               │ │ + book_insurance()     │               │
└────────────────────┘               │ └────────────────────────┘               │
▲                          │             ▲                            │
uses      │                          │     uses    │                            │
▼                          │             ▼                            │
(ADAPTEE / LEGACY CLASS)            │   (ADAPTEE / LEGACY CLASS)              │
┌────────────────────┐               │ ┌────────────────────────┐              │
│ ProviderAAPI       │               │ │ ProviderBAPI           │              │
├────────────────────┤               │ ├────────────────────────┤              │
│ getQuoteAmount()   │               │ │ calculateInsurance()   │              │
│ purchase()         │               │ │ confirmPurchase()      │              │
└────────────────────┘               │ └────────────────────────┘              │
│                                          │

'''

# step1: target interface is TravelInsuranceAdapter which is common for my application to interact with different insurance providers

from abc import ABC, abstractmethod
class TravelInsuranceAdapter(ABC):
    @abstractmethod
    def get_insurance_quote(self, destination: str, duration: int, age: int) -> float:
        pass

    @abstractmethod
    def purchase_insurance(self, quote_id: str, payment_info: dict) -> bool:
        pass


# ----------------------------------------------------------------------------------------------

# step2: existing interface is InsuranceProviderA which has different method names and parameters
class InsuranceProviderA:
    def fetch_quote(self, location: str, days: int, traveler_age: int) -> float:
        # Simulate fetching a quote from Provider A's API
        return 100.0 + days * 10 + traveler_age * 2

    def buy_policy(self, quote_reference: str, payment_details: dict) -> bool:
        # Simulate purchasing a policy from Provider A's API
        return True

class InsuranceProviderB:

    def get_quote_amount(self, dest: str, trip_length: int, person_age: int) -> float:
        # Simulate fetching a quote from Provider B's API
        return 120.0 + trip_length * 12 + person_age * 3

    def confirm_purchase(self, quote_id: str, payment_info: dict) -> bool:
        return True

# ----------------------------------------------------------------------------------------------


# step3: create the adapter class that implements the target interface and uses the adaptee

class InsuranceAAdapter(TravelInsuranceAdapter):
    def __init__(self, provider: InsuranceProviderA):
        self.provider = provider

    def get_insurance_quote(self, destination: str, duration: int, age: int) -> float:
        return self.provider.fetch_quote(destination, duration, age)

    def purchase_insurance(self, quote_id: str, payment_info: dict) -> bool:
        return self.provider.buy_policy(quote_id,payment_info)

class InsuranceBAdapter(TravelInsuranceAdapter):
    def __init__(self, provider: InsuranceProviderB):
        self.provider = provider

    def get_insurance_quote(self, destination: str, duration: int, age: int) -> float:
        return self.provider.get_quote_amount(destination, duration, age)

    def purchase_insurance(self, quote_id: str, payment_info: dict) -> bool:
        return self.provider.confirm_purchase(quote_id,payment_info)

# ----------------------------------------------------------------------------------------------

# step5: test the adapter class to ensure it works as expected...

class TravelInsuranceAdapterTest:

    @staticmethod
    def test_adapter(adapter: TravelInsuranceAdapter):
        quote = adapter.get_insurance_quote('blr', 5, 30)
        print(f"Quote: {quote}")
        purchase = adapter.purchase_insurance("1234_id", {"card": "1234-5678-9876-5432"})
        print(f"Purchase: {purchase}")
        assert quote > 0
        assert purchase is True
        print("All tests passed!")

if __name__ == "__main__":
    insurance_provider_A = InsuranceProviderA()
    travel_adapter = InsuranceAAdapter(insurance_provider_A)
    travel_insurance = TravelInsuranceAdapterTest.test_adapter(travel_adapter)

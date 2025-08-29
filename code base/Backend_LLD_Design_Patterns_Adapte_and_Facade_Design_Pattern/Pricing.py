'''
Refactoring Pricing Calculation with the Strategy Pattern
Problem Statement
You are tasked with refactoring a pricing calculator for a ride-sharing app. The existing pricing manager class (PricingManager) uses a monolithic approach to calculate ride prices based on different strategies: distance-based, time-based, and surge pricing. The goal is to refactor the code to use the Strategy pattern, allowing for more flexible pricing strategies and better maintenance.

Assignment
Your task is to refactor the PricingManager class to use the Strategy pattern effectively. You will create separate pricing strategy classes for each pricing type (distance-based, time-based, surge) by implementing the PricingStrategy interface. Each strategy class will provide its own implementation for calculating the ride price.

Distance-Based Pricing
Calculate the ride price based on the distance traveled.
Base fare: 5.0
Rate per kilometer: 2.0
Time-Based Pricing
Calculate the ride price based on the duration of the ride.
Base fare: 5.0
Rate per minute: 0.5
Surge Pricing
Implement surge pricing logic to increase the ride price during peak hours.
Surge multiplier: 2.0 (e.g., 2x the base price)
By implementing the Strategy pattern, you'll have a more flexible and maintainable pricing calculator that can accommodate various pricing strategies, making it easier to adjust pricing rules in the future.

Implementing the Strategy Pattern
Complete the PricingStrategy Interface: Begin by adding methods to the PricingStrategy interface. This interface should define a method calculate_price for calculating the ride price.

Implement Concrete Pricing Strategy Classes: Complete the concrete classes that implement the PricingStrategy interface. These classes represent different pricing strategies, including:

DistanceBasedPricingStrategy: Calculate the price based on the distance traveled.
TimeBasedPricingStrategy: Calculate the price based on the duration of the ride.
SurgePricingStrategy: Implement surge pricing logic.
Refactor the PricingManager Class: Refactor the existing PricingManager class by removing the hardcoded pricing logic and instead delegating the price calculation to the selected pricing strategy. The PricingManager class should now use composition to hold an instance of the selected pricing strategy. You need to accept the pricing strategy as a parameter in the PricingManager constructor and use it to calculate the ride price.

Test Your Refactored Code: Write test cases to ensure that the refactored code produces accurate pricing calculations for each pricing strategy. You should test different scenarios to verify that each strategy behaves as expected.

Instructions
Refactor the PricingManager class by implementing the Strategy pattern:

Add a method calculate_price to the PricingStrategy interface.
Implement separate pricing strategy classes for distance-based, time-based, and surge pricing.
Add a field to the PricingManager class to hold the selected pricing strategy.
Pass the pricing strategy as a parameter to the PricingManager constructor and use it to calculate the ride price.
'''
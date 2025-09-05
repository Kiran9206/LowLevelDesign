'''
Strategy Pattern for Stock Trading Indicators
Problem Statement
You are tasked with refactoring a stock trading application. The application currently calculates various trading
indicators such as moving averages, momentum, and volatility. These indicators are used to make decisions about buying,
selling, or holding stocks. However, the current implementation relies on a single class, making it challenging to extend
and maintain as new indicators are added. To address this, you need to refactor the application to use the Strategy pattern.
This pattern allows you to encapsulate each trading indicator as a separate strategy and easily switch between them without
modifying the core trading algorithm.

Assignment
Your task is to refactor the StockTradingManager class to use the Strategy pattern for calculating trading indicators.
You should create separate strategy classes for each trading indicator (Moving Averages, Momentum, and Volatility) that
implement a common interface. Each strategy should define its calculation method for the respective indicator.
The StockTradingManager class should utilize these strategies to calculate indicators based on the selected strategy type.
Additionally, each strategy should provide a method to check if it supports a specific indicator type.

Implementing the Strategy Pattern
Create a Strategy Interface: Define a common interface, e.g., TradingIndicatorStrategy, that declares a method for calculating
the trading indicator and another method for checking if the strategy supports a specific indicator type.

Implement Concrete Strategies: Create concrete strategy classes for each trading indicator (Moving Averages, Momentum, and Volatility).
Implement the methods defined in the TradingIndicatorStrategy interface for calculating the respective indicators. Ensure that each strategy
class also implements the supportsType method to specify which indicator type it supports.

Refactor StockTradingManager: Modify the StockTradingManager class to accept a TradingIndicatorStrategy instead of a TradingStrategyType.
The calculateIndicator method should delegate the calculation to the selected strategy.

Copy Existing Logic: For each strategy, copy the existing indicator calculation logic from the original StockTradingManager class into the
corresponding strategy class.

Test Your Implementation: Write test cases to ensure that each strategy correctly calculates the corresponding indicator, and that the
StockTradingManager class works seamlessly with different strategies.

Trading Indicator Calculations
Moving Averages: This indicator calculates the average of a stock's price and its previous price. It can help identify trends by
smoothing out price fluctuations.

Momentum: Momentum is the difference between the current stock price and its previous price. It provides insights into the stock's rate of change.

Volatility: Volatility measures the magnitude of price fluctuations in a stock. It calculates the absolute difference between the current
price and the previous price.
'''

from abc import ABC, abstractmethod

# step1: create the Strategy Interface
class TradingIndicatorStrategy(ABC):
    @abstractmethod
    def calculate_indicator(self, current_price, prev_price)-> float:
        pass

    @abstractmethod
    def supports_type(self, indicator_type)-> bool:
        pass


# step2: Implement Concrete Strategies
class MovingAverageStrategy(TradingIndicatorStrategy):

    def __init__(self):
        self.supported_type = 'Moving Average'

    def calculate_indicator(self, current_price: float, prev_price) -> float:
        if not current_price:
            return 0.0
        return (current_price + prev_price) / 2

    def supports_type(self, indicator_type) -> bool:
        return indicator_type == self.supported_type

class MomentumStrategy(TradingIndicatorStrategy):

    def __init__(self):
        self.supported_type = 'Momentum'

    def calculate_indicator(self, current_price, prev_price) -> float:
        if not current_price:
            return 0.0
        return current_price - prev_price

    def supports_type(self, indicator_type) -> bool:
        return indicator_type == self.supported_type

class VolatilityStrategy(TradingIndicatorStrategy):
    def __init__(self):
        self.supported_type = 'Volatility'

    def calculate_indicator(self, current_price, prev_price) -> float:
        return abs(current_price - prev_price)

    def supports_type(self, indicator_type) -> bool:
        return indicator_type == self.supported_type


# step3: create strategy factory

class TradingIndicatorFactory:


    def get_strategy(self, indicator:str)-> TradingIndicatorStrategy:
        if indicator == 'Moving Average':
            return MovingAverageStrategy()
        elif indicator == 'Momentum':
            return MomentumStrategy()
        elif indicator == 'Volatility':
            return VolatilityStrategy()
        else:
            raise ValueError("Invalid indicator type")

# step4: create StockTradingManager class

class StockTradingManager:

    def __init__(self, strategy: TradingIndicatorStrategy):
        self.strategy = strategy

    def calculate_indicator(self, current_price, prev_price) -> float:
        return self.strategy.calculate_indicator(current_price, prev_price)

    def supports_type(self, indicator_type) -> bool:
        return self.strategy.supports_type(indicator_type)


# Example usage
if __name__ == "__main__":
    current_price = 150.0
    previous_price = 145.0

    # Moving average
    strategy = TradingIndicatorFactory().get_strategy('Moving Average')
    Moving_average = StockTradingManager(strategy)
    assert Moving_average.supports_type('Moving Average')
    print("Moving Average:", Moving_average.calculate_indicator(current_price, previous_price))

    # Momentum
    strategy = TradingIndicatorFactory().get_strategy('Momentum')
    momentum = StockTradingManager(strategy)
    assert momentum.supports_type('Momentum')
    print("Momentum:", momentum.calculate_indicator(current_price, previous_price))

    # Volatility
    strategy = TradingIndicatorFactory().get_strategy('Volatility')
    volatility = StockTradingManager(strategy)
    assert volatility.supports_type('Volatility')
    print("Volatility:", volatility.calculate_indicator(current_price, previous_price))


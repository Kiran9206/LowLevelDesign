'''3. Temperature Converter
Task: Create a TemperatureConverter class that:
Has a private attribute for storing the temperature in Celsius.
Public methods to:
Set the temperature in Celsius.
Convert it to Fahrenheit and return the result.
Convert it to Kelvin and return the result.
Ensure that the temperature is only set through the method, not directly.'''


class TemperatureConverter:

    def __init__(self) -> None:
        self.__celsius = 0

    def set_temperature(self, celsius: float) -> None:
        # Ensure the input is a valid numerical value
        if isinstance(celsius, (int, float)):
            self.__celsius = celsius
            print(f"Current temperature in Celsius is {self.__celsius}°C")
        else:
            print("Please provide a valid numerical value for the temperature.")

    def convert_to_fahrenheit(self) -> float:
        # Convert Celsius to Fahrenheit
        result = (self.__celsius * 9/5) + 32
        return result

    def convert_to_kelvin(self) -> float:
        # Convert Celsius to Kelvin
        result = self.__celsius + 273.15
        return result

    def get_temperature(self) -> float:
        # Optional: Retrieve the current temperature in Celsius
        return self.__celsius



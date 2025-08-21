'''
Builder Pattern Implementation for a database configuration class
Problem Statement
You are tasked with creating a system-wide database configuration for a complex software suite. The configuration is responsible for managing
various configuration settings that affect the data layer. To ensure a flexible and readable way to create configuration instances that are immutable,
you decide to implement the Builder pattern.

Assignment
Your task is to implement the Builder pattern to create instances of a configuration manager class. The Builder pattern allows for step-by-step
construction of complex objects while keeping the creation process separate from the main object.

Implementing the Builder Pattern
Review the original class - You have been provided with a class that represents the database configuration DatabaseConfiguration. The class has a
number of properties that are used to configure the database connection. Your task is to implement the Builder pattern to create instances of a class
with the same properties.

Create the builder class - Create a new class called DatabaseConfigurationBuilder that will implement the builder patter. A dummy class has been
 provided for you to start with. Remember to annotate the class with the @WithBuilder annotation. The name does not matter as long as it is annotated.

Test your implementation - A test case has been provided for you to test your implementation. Run the test case to ensure that your implementation
is correct. This will pick the correct implementation of the builder class based on the @WithBuilder annotation.
'''



# step1: identify the complex object....
# step2: create a concrete product class that will be built using the builder pattern.
class DatabaseConfiguration:

    def __init__(self, host: str, port: int, username: str, password: str, database_name: str):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._database_name = database_name

    @property
    def host(self): return self._host

    @property
    def port(self): return self._port

    @property
    def username(self): return self._username

    @property
    def password(self): return self._password

    @property
    def database_name(self): return self._database_name

    def __str__(self):
        return f"DatabaseConfiguration(host={self.host}, port={self.port}, username={self.username}, password={self.password}, database_name={self.database_name})"

# step3: create a builder class that will build the complex object.
class DatabaseConfigurationBuilder:

    def __init__(self):
        self.host = None
        self.port = None
        self.username = None
        self.password = None
        self.database_name = None

    def set_host(self, host: str):
        self.host = host
        return self

    def set_port(self, port: int):
        self.port = port
        return self

    def set_username(self, username: str):
        self.username = username
        return self

    def set_password(self, password: str):
        self.password = password
        return self

    def set_database_name(self, database_name: str):
        self.database_name = database_name
        return self

    def build(self):
        if not all([self.host, self.port, self.username, self.password, self.database_name]):
            raise ValueError("All fields must be set before building the configuration.")
        return DatabaseConfiguration(self.host, self.port, self.username, self.password, self.database_name)

# step4: create a test case to test the builder pattern implementation.

class Client:
    def __init__(self):
        self.builder = DatabaseConfigurationBuilder()

    def create_configuration(self):
        return (self.builder
                .set_host('1.2.3.4.5')
                .set_port(1099)
                .set_username('kiran@123')
                .set_password('password123')
                .set_database_name('db_name')
                .build())

if __name__ == "__main__":
    client = Client()
    obj = client.create_configuration()
    print(obj)




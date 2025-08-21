'''
Prototype Pattern for Configuration Object Cloning
Problem Statement
You are developing a configuration management system for your application. This system allows users to define and manage various configurations
with different attributes. Creating new configurations with specific attributes is a frequent task during testing and development. However,
setting up these configurations manually can be time-consuming and error-prone. To streamline this process, you decide to implement the Prototype
pattern. This pattern will enable you to create prototype configuration objects and clone them when needed, saving time and reducing the risk of errors.

Assignment
Your task is to implement the Prototype pattern to create prototype objects for configuration management. There is a Cloneable interface that contains
the clone method, which should be implemented by configuration objects. Additionally, you need to implement a ConfigurationPrototypeRegistry interface
that provides methods for adding and retrieving configuration prototypes and for cloning configuration objects. The goal is to simplify the process of
creating configurations with specific attributes.

Implementing the Prototype Pattern
Review the Cloneable interface: Have a look at the interface named Cloneable with a single method, clone_object(), that returns a cloned copy of the
implementing object.

Implement the clone_object() method: Review the Configuration class with attributes for the app. Implement the clone_object() from the Cloneable interface.
Your method should create a new Configuration object and copy the attribute values from the original object to the new object. Return the new object as the
cloned copy. You can either implement the cloning logic or use a library like copy clone the object. You can use any of shallow or deep cop.

Review the ConfigurationPrototypeRegistry interface: See the interface named ConfigurationPrototypeRegistry that includes methods for adding prototypes,
retrieving prototypes by type, and cloning configuration objects.

Complete the registry implementation: A class that inherits from the ConfigurationPrototypeRegistry interface is present in the codebase. However, the
methods are not implemented. You need to implement the methods to manage configuration prototypes and perform cloning operations. In this class, manage
a collection of configuration prototypes and provide methods to add prototypes, retrieve prototypes by type, and clone configuration objects based on
their type.

Instructions
Clone this repository to your local machine.
Implement the Prototype pattern by completing the clone_object() method in the Configuration class.
Implement the ConfigurationPrototypeRegistry interface to manage configuration prototypes and perform cloning operations. Complete the methods in the
ConfigurationPrototypeRegistryImpl class.
Run the provided test cases in the ConfigurationPrototypeRegistryTest class to validate the correctness of your prototype pattern implementation.
Ensure that configuration objects can be cloned successfully, and that the registry functions as expected.
'''

import copy
from distutils.command.register import register


class prototype:

    def clone_object(self):
        """
        This method should be implemented by subclasses to create a clone of the object.
        """
        raise NotImplementedError("Subclasses must implement this method.")

class Configuration(prototype):

    def __init__(self, app_name: str, version: str, settings: dict):
        self.app_name = app_name
        self.version = version
        self.settings = settings

    def clone_object(self):
        return copy.deepcopy(self)

class ConfigurationPrototypeRegistry:

    def add(self, config: Configuration):
        """
        Adds a configuration prototype to the registry.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def get(self, app_name: str)-> Configuration:
        """
        Retrieves a configuration prototype by its app name.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def clone(self,app_name: str):
        """
        Clones a configuration prototype.
        """
        raise NotImplementedError("Subclasses must implement this method.")

class ConfigurationPrototypeRegistryImpl(ConfigurationPrototypeRegistry):

    def __init__(self):
        self.registry = {}

    def add(self, config: Configuration):
        """
        Adds a configuration prototype to the registry.
        """
        self.registry[config.app_name] = config

    def get(self, app_name: str) -> Configuration:
        return self.registry[app_name]

    def clone(self, app_name: str):
        if app_name in self.registry:
            return self.get(app_name).clone_object()
        else:
            raise ValueError(f"No configuration found with app name: {app_name}")





if __name__ == "__main__":
    config1 = Configuration(app_name='app1', version='1.0', settings={'setting1': 'value1'})
    register = ConfigurationPrototypeRegistryImpl()
    register.add(config1)
    config2 = register.clone('app1')
    config2.app_name = "app2"
    config2.version = "2.0"
    config2.settings['setting2'] = 'value2'
    register.add(config2)
    print(register.get('app1'), register.get('app2'))



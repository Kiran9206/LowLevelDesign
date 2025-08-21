'''
Builder Pattern Implementation for Building Queries
Problem Statement
You are tasked with developing a database management system that involves creating and executing SQL queries. Queries can
vary in complexity, involving different SELECT clauses, JOIN operations, WHERE conditions, and more. The current approach
of constructing queries using concatenated strings has proven to be error-prone, difficult to read, and challenging to modify.
You should implement the Builder pattern to create instances of query objects with various configurations, resulting in more
maintainable and flexible code.

Assignment
Your task is to implement the Builder pattern to construct query objects with different configurations. The Builder pattern
facilitates the step-by-step construction of complex objects while keeping the creation process separate from the main object.

The usage of your builder should look like this:

query = QueryBuilder()\
    .with_select('name', 'age')\
    .with_from('users')\
    .with_where('age > 18')\
    .build()
Implementing the Builder Pattern
Review the original class and the builder interface - You have been provided with a class that represents the query data Query.
 The class has a number of properties that are used to create the query object. The class extends from the Builder interface
 which has a method build() that returns an instance of the class. Your task is to implement the Builder pattern to create
 instances of a class with the same properties. You have to complete the implementation of the build method.

Implement the setter methods - The idea of the builder method to have a mutable instance of the Query class in the builder
class and expose methods to set the properties of the class. Once the properties have been set, the build method is called to
 create an immutable instance of the class. You need to implement the setter methods for the properties of the Query class in
 the builder class. Methods like with_select, with_from, with_where, etc. should be implemented so that the user can use the
 builder instance to set the properties of the Query class.

Implement the build method - The build method is responsible for creating an instance of the Query class. The method should
return an instance of the Query class with the properties set by the user using the builder instance.

Test your implementation - A test case has been provided for you to test your implementation. Run the test case to ensure
that your implementation is correct.

Instructions
Clone this repository to your local machine.
Open the Query class and implement the setter methods in the QueryBuilder class.
Implement the build method in the QueryBuilder class.
Run the provided test cases in the TestQueryBuilder class to verify the correctness of your implementation.
'''
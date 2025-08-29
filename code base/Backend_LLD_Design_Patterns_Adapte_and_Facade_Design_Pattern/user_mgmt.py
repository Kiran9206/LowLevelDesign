'''
Flyweight Pattern for Chess User Optimization
Problem Statement
You are developing a chess game application where you need to represent individual chess users with various attributes like name, age, gender, email, and more. One user can play multiple games simultaneously. At the moment, you create a new user object for each game. Each user object consumes memory, and you want to optimize the memory usage by only keeping one copy of fields that do not change.

You need to implement the Flyweight pattern to efficiently manage and reuse shared attributes while keeping individual user-specific data separate.

Assignment
Your task is to implement the Flyweight pattern to optimize the memory usage of chess user objects in your application. The Flyweight pattern aims to share common intrinsic state between multiple objects to reduce memory consumption while keeping extrinsic state (variable and context-dependent) separate for each object. Look closely at the ChessUser class and identify which fields are going to be different amongst different games and which ones will be the same.

Task 1 - Intrinsic and Extrinsic State Separation
In the Flyweight pattern, objects are split into intrinsic state (shared and independent of the context) and extrinsic state (variable and dependent on the context). Your task is to refactor the initial ChessUser class into two separate classes: UserIntrinsicState and UserExtrinsicState.

UserIntrinsicState class:

Complete the class named UserIntrinsicState with appropriate fields to represent the intrinsic state of a chess user. You have been given an empty class.
Do not change the name of the fields as the test cases depend on the field names.
UserExtrinsicState class:

Complete the class named UserExtrinsicState with appropriate fields to represent the extrinsic state of a chess user. You have been given an empty class.
Make sure to add a reference called intrinsic_state to the UserIntrinsicState class in the UserExtrinsicState class.
Do not change the name of the fields as the test cases depend on the field names.
Task 2 - Implementing the registry pattern
To make the storage and usability of the flyweight easier, implement the registry pattern

The interface called FlyweightRegistry has been provided. You need to implement these methods in the FlyweightRegistryImpl class.
The class should store the flyweight and fetch the relevant flyweight based on the type.
Instructions
Implement the UserIntrinsicState and UserExtrinsicState by breaking the original class into intrinsic and extrinsic state.
Ensure that the names of the fields in the UserIntrinsicState and UserExtrinsicState classes are not changed.
Implement the registry interface's FlyweightRegistry to add and get flyweight methods.
Run the provided test cases in the UserTest class to verify the correctness of your implementation. You are not required to edit the test cases themselves.
'''
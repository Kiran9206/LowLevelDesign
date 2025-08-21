'''
Prototype Pattern for Efficient Invoice Generation
Problem Statement
You are tasked with creating an API for invoice generation and testing. While testing, generating invoices from scratch by fetching data from a
database is time-consuming, as retrieving a single invoice already takes several seconds. When you need to generate many invoices for testing purposes,
this approach becomes impractical. To optimize the testing process, you decide to implement the Prototype pattern. This pattern allows you to create
prototype invoice objects and efficiently clone them as needed, significantly reducing the time and resources required for invoice generation during testing.

Assignment
Your task is to implement the Prototype pattern to create prototype objects for invoice management. There is a Cloneable interface that contains the
clone method, which should be implemented by invoice objects. Additionally, you need to implement a InvoicePrototypeRegistry interface that provides
methods for adding and retrieving invoice prototypes and for cloning invoice objects. The goal is to simplify the process of creating invoice with specific
attributes.

Implementing the Prototype Pattern
Review the Cloneable interface: Have a look at the interface named Cloneable with a single method, clone_object(), that returns a cloned copy of the
implementing object.

Implement the clone_object() method: Review the Invoice class with attributes for the app. Implement the clone_object() from the Cloneable interface.
Your method should create a new Invoice object and copy the attribute values from the original object to the new object. Return the new object as the
cloned copy. You can either implement the cloning logic or use a library like copy clone the object. You can use any of shallow or deep cop.

Review the InvoicePrototypeRegistry interface: See the interface named InvoicePrototypeRegistry that includes methods for adding prototypes, retrieving
prototypes by type, and cloning invoice objects.

Complete the registry implementation: A class that inherits from the InvoicePrototypeRegistry interface is present in the codebase. However, the methods
are not implemented. You need to implement the methods to manage invoice prototypes and perform cloning operations. In this class, manage a collection of
invoice prototypes and provide methods to add prototypes, retrieve prototypes by type, and clone invoice objects based on their type.

Instructions
Clone this repository to your local machine.
Implement the Prototype pattern by completing the clone_object() method in the Invoice class.
Implement the InvoicePrototypeRegistry interface to manage invoice prototypes and perform cloning operations. Complete the methods in the
InvoicePrototypeRegistryImpl class.
Run the provided test cases in the TestInvoicePrototypeRegistryImpl class to validate the correctness of your prototype pattern implementation.
Ensure that invoice objects can be cloned successfully, and that the registry functions as expected.
'''
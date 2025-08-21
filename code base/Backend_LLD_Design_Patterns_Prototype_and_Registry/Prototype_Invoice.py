'''
Prototype Pattern for Efficient Invoice Generation
Problem Statement
You are tasked with creating an API for invoice generation and testing. While testing, generating invoices from scratch by fetching data from a
database is time-consuming, as retrieving a single invoice already takes several seconds. When you need to generate a large number of invoices for
testing purposes, this approach becomes impractical. To optimize the testing process, you decide to implement the Prototype pattern. This pattern
allows you to create prototype invoice objects and efficiently clone them as needed, significantly reducing the time and resources required for
invoice generation during testing.

Assignment
Your assignment is to implement the Prototype pattern to create prototype invoice objects for efficient testing. You should define an ObjectClonable
 interface that contains the clone method, which should be implemented by invoice objects. Additionally, you need to create an InvoicePrototypeRegistry
 interface that provides methods for adding and retrieving invoice prototypes and for cloning invoice objects. The primary objective is to streamline
 the process of generating invoices for testing, making it faster and more resource-efficient.

Implementing the Prototype Pattern
Define the ObjectClonable interface: Create an interface named ObjectClonable with a single method, clone(), that returns a cloned copy of the
implementing object.

Implement the invoice object: Implement the Invoice class with attributes like invoiceId, customerName, amount, dueDate, and invoiceType.
Ensure that the Invoice class implements the ObjectClonable interface by providing a proper clone method that creates a deep copy of the invoice object.

Define the InvoicePrototypeRegistry interface: Create an interface named InvoicePrototypeRegistry that includes methods for adding prototypes,
retrieving prototypes by type, and cloning invoice objects.

Create the registry implementation: Implement a class that adheres to the InvoicePrototypeRegistry interface. In this class, manage a collection
of invoice prototypes and provide methods to add prototypes, retrieve prototypes by type, and clone invoice objects based on their type.

Test your implementation: Write test cases to ensure that the Invoice class correctly implements the ObjectClonable interface and that the registry
class properly manages prototypes and performs cloning operations. Verify that cloning an invoice object results in a new object with the same
attribute values but is not the same object in memory.
'''
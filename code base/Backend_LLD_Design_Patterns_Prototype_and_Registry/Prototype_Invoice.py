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

import copy

class ObjectClonable:

    def clone(self):
        raise NotImplementedError

class Invoice(ObjectClonable):
    def __init__(self,invoiceId: int, customerName: str, amount: float, dueDate: str,invoiceType: str):
        self.invoiceId = invoiceId
        self.customerName = customerName
        self.amount = amount
        self.dueDate = dueDate
        self.invoiceType = invoiceType

    def clone(self):
        return copy.deepcopy(self)

    def __repr__(self):
        return (f"Invoice(invoiceId={self.invoiceId}, customerName='{self.customerName}', "
                f"amount={self.amount}, dueDate='{self.dueDate}', invoiceType='{self.invoiceType}')")

class InvoicePrototypeRegistry:
    def add_prototype(self, invoice_type: str, prototype: ObjectClonable):
        raise NotImplementedError

    def get_prototype(self, invoice_type: str) -> ObjectClonable:
        raise NotImplementedError

    def clone_invoice(self, invoice_type: str) -> ObjectClonable:
        raise NotImplementedError

class InvoicePrototypeRegistryImpl(InvoicePrototypeRegistry):

    def __init__(self):
        self.registry = {}

    def add_prototype(self, invoice_type: str, prototype: ObjectClonable):
        if not isinstance(prototype, ObjectClonable):
            raise TypeError("Prototype must implement ObjectClonable interface")
        self.registry[invoice_type] = prototype

    def get_prototype(self, invoice_type: str) -> ObjectClonable:
        if invoice_type not in self.registry:
            raise KeyError(f"No prototype found for type: {invoice_type}")
        return self.registry[invoice_type]

    def clone_invoice(self, invoice_type: str) -> ObjectClonable:
        if invoice_type in self.registry:
            return self.get_prototype(invoice_type).clone()
        raise KeyError(f"No prototype found for type: {invoice_type}")


if __name__ == "__main__":

    invoice1 = Invoice(
        invoiceId=1,
        customerName="John Doe",
        amount=100.0,
        dueDate="2023-10-01",
        invoiceType="Standard"
    )
    registry = InvoicePrototypeRegistryImpl()
    registry.add_prototype(invoice1.invoiceType, invoice1)
    invoices = []
    for idx in range(5):
        invoices.append(registry.clone_invoice(invoice1.invoiceType))
        invoices[idx].invoiceId = idx + 1

    for item in invoices:
        print(item)

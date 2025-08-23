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

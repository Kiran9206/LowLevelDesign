'''
Abstract Factory Pattern for Document Processing
Problem Statement
You are designing a document processing application. Depending on the type of document (e.g., text, spreadsheet, presentation), different
processing routines are required. These routines involve multiple steps, such as parsing, formatting, and exporting, which need to be coordinated
to ensure correct document processing. You want to create instances of these processing steps without explicitly specifying their classes and
ensure that the steps within the same family are compatible.

Assignment
Your task is to implement the Abstract Factory pattern to create document processors in the document processing application. The Abstract Factory
pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes, allowing for easy
addition of new document processor types and ensuring compatibility within families.

Task 1 - Adding the factory methods to the abstract factory
The abstract factory class DocumentFactory has been created for you. You will need to add the factory methods to create document parsers, printers
and processors to the abstract factory class. The methods to be implemented are:

create_document_parser
create_document_processor
create_document_printer
supports_format
Task 2 - Implementing the Abstract Factory
Now that you have the abstract factory class, you will need to implement the abstract factory for different types of documents such as TextDocument,
SpreadsheetDocument, and PresentationDocument. Two classes have been created for you: TextDocumentFactory and SpreadsheetDocumentFactory. You will
need to implement the methods to create compatible document parsers, processors, and printers. Ensure that the created components are compatible
within the same format family.

Instructions
Complete the DocumentFactory interface with methods to create document parsers, processors, and printers, and to check if the factory supports a
specific document format. Methods to be implemented are:
create_document_parser
create_document_processor
create_document_printer
supports_format
Complete the concrete implementations of the DocumentFactory interface for text, spreadsheet, and presentation document formats. Implement the
methods to create compatible document parsers, processors, and printers. The classes to be implemented are:
TextDocumentFactory
SpreadsheetDocumentFactory
Run the provided test cases in the DocumentFactoryTest class to verify the correctness of your implementation. The tests will check if all
document components have a common parent class, and if the factory classes can correctly create document parsers, processors, and printers based
on the document format.
'''

from abc import ABC, abstractmethod

from mypy.errorcodes import ABSTRACT


class DocumentParser(ABC):
    @abstractmethod
    def parse(self, document):
        pass
class DocumentProcessor(ABC):
    @abstractmethod
    def process(self):
        pass
class DocumentPrinter(ABC):
    @abstractmethod
    def print_document(self):
        pass

class DocumentFactory(ABC):

    @abstractmethod
    def create_document_parser(self):
        pass

    @abstractmethod
    def create_document_processor(self):
        pass

    @abstractmethod
    def create_document_printer(self):
        pass

    @abstractmethod
    def supports_format(self, doc_type):
        pass
# ---------------------------------------------------
class TextDocumentParser(DocumentParser):
    def parse(self, document):
        # Implementation for parsing text documents
        return f"Parsing text document: {document}"
class TextDocumentProcessor(DocumentProcessor):
    def process(self):
        return f'Processing text document'
class TextDocumentPrinter(DocumentPrinter):
    def print_document(self):
        return f"printing text document"

class TextDocumentFactory(DocumentFactory):

    def create_document_parser(self):
        return TextDocumentParser()

    def create_document_processor(self):
        return TextDocumentProcessor()

    def create_document_printer(self):
        return TextDocumentPrinter()

    def supports_format(self, format_type):
        return format_type == "text"
# ------------------------------------------------------------
class SpreadsheetDocumentParser(DocumentParser):
    def parse(self, document):
        return f"parsing spreadsheet document:{document}"

class SpreadsheetDocumentProcessor(DocumentProcessor):
    def process(self):
        return f"processing spreadsheet document"

class SpreadsheetDocumentPrinter(DocumentPrinter):
    def print_document(self):
        return f"printing spreadsheet document"
class SpreadsheetDocumentFactory(DocumentFactory):

    def create_document_parser(self):
        return SpreadsheetDocumentParser()
    def create_document_processor(self):
        return SpreadsheetDocumentProcessor()
    def create_document_printer(self):
        return SpreadsheetDocumentPrinter()
    def supports_format(self, format_type):
        return format_type == "spreadsheet"
# -------------------------------------------------------------
class PresentationDocumentParser(DocumentParser):
    def parse(self, document):
        return f"parsing presentation document: {document}"

class PresentationDocumentProcessor(DocumentProcessor):
    def process(self):
        return f"processing presentation document"

class PresentationDocumentPrinter(DocumentPrinter):
    def print_document(self):
        return f"printing presentation document"

class PresentationDocumentFactory(DocumentFactory):
    def create_document_parser(self):
        return PresentationDocumentParser()
    def create_document_processor(self):
        return PresentationDocumentProcessor()
    def create_document_printer(self):
        return PresentationDocumentPrinter()
    def supports_format(self, format_type):
        return format_type == "presentation"
# -------------------------------------------------------------------

class DocumentFactoryTest:

    @staticmethod
    def test_document_factory(doc_type:str, factory: DocumentFactory):
        if not factory.supports_format(doc_type):
            raise ValueError(f"Factory does not support format: {doc_type}")

        parser = factory.create_document_parser()
        processor = factory.create_document_processor()
        printer = factory.create_document_printer()

        assert isinstance(parser, DocumentParser), "Parser is not an instance of DocumentParser"
        assert isinstance(processor, DocumentProcessor), "Processor is not an instance of DocumentProcessor"
        assert isinstance(printer, DocumentPrinter), "Printer is not an instance of DocumentPrinter"

        print(parser.parse("Sample Document"))
        print(processor.process())
        print(printer.print_document())


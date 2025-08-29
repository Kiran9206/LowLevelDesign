'''
Adapter Pattern for Language Translation Integration
Problem Statement
You are developing a language translation tool that needs to integrate with different translation services like Google Translate, Microsoft Translator, and Yandex.Translate. Each service offers its own API and response format, making integration complex. To simplify this process and ensure consistency in the codebase, you decide to implement the Adapter pattern. This pattern allows you to create adapter classes for different translation services, converting their APIs into a common format that your application can work with.

Assignment
Your task is to implement the Adapter pattern to create adapter classes for different translation service APIs. These adapters should adhere to the TranslationAdapter interface, which defines common methods for translation and fetching supported languages. The goal is to abstract away the differences in APIs and data formats, providing a unified interface for your language translation tool.

Implementing the Adapter Pattern
Review the existing APIs: Study the APIs and data formats of the translations platforms you need to integrate. Understand the differences in their APIs and how they interact with their respective systems. You will find the external API classes in the services.py file and look at the GoogleTranslateApi and MicrosoftTranslateApi classes.

Implement the adapter interface: You have been provided with a TranslationAdapter interface. Your task is to add common methods of the APIs to the interface, implement this interface in different adapter classes, each corresponding to a different translation platform. The adapters should adapt the provider-specific APIs into a format that matches the TranslationAdapter interface.

Use composition: Create adapter classes that internally use instances of the actual translation platform APIs. You should not modify the platform APIs directly. Instead, create methods in the adapter classes that map to the platform APIs and perform the necessary transformations.

Test your implementation: Run the provided test cases in the TranslationAdapterTest class to ensure that your adapter classes work correctly. These test cases will check if your adapters have the required methods and if they interact with the platform APIs properly.

Instructions
Add methods to the TranslationAdapter interface that match the common functionality of the translation platforms. You will implement this interface in the adapter classes for Google and Microsoft. These classes should adapt the platform-specific APIs into a common format.
Implement the Adapter pattern by creating adapter classes that implement the TranslationAdapter interface and adapt the APIs of different translation platforms. The classes MicrosoftTranslationAdapter and GoogleTranslationAdapter are provided as placeholders. You need to complete these classes to adapt the Google and Microsoft APIs to the common TranslationAdapter interface.
Run the provided test cases in the TranslationAdapterTest class to verify the correctness of your adapter pattern implementation. Make sure your adapters have the expected methods and interact with the platform APIs as required.
'''
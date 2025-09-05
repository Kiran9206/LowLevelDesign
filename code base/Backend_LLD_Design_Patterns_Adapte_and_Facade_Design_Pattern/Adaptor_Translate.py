'''
Adapter Pattern for Language Translation Integration
Problem Statement
You are developing a language translation tool that needs to integrate with different translation services like Google
Translate, Microsoft Translator, and Yandex.Translate. Each service offers its own API and response format, making
integration complex. To simplify this process and ensure consistency in the codebase, you decide to implement the Adapter
pattern. This pattern allows you to create adapter classes for different translation services, converting their APIs into
a common format that your application can work with.

Assignment
Your task is to implement the Adapter pattern to create adapter classes for different translation service APIs.
These adapters should adhere to the TranslationProviderAdapter interface, which defines common methods for translation
and fetching supported languages. The goal is to abstract away the differences in APIs and data formats, providing a
unified interface for your language translation tool.

Implementing the Adapter Pattern
Review the existing translation services: Study the APIs and response formats of the translation services you need to
integrate with. Understand how each service's API works and the data it provides.

Implement the adapter interface: You have been provided with a TranslationProviderAdapter interface. Your task is to
create adapter classes for each translation service that implements this interface. These adapters should adapt the
specific translation service's API into a format that matches the methods defined in the TranslationProviderAdapter.

Use composition: Create adapter classes that internally use instances of the actual translation service APIs, such as
GoogleTranslateApi and MicrosoftTranslateApi. Avoid modifying the provider APIs directly; instead, create methods in
the adapter classes that map to the provider APIs and perform the necessary data transformations.

Additional method: Apart from the translate method, you should implement another method as required by the assignment.

Test your implementation: Execute the provided test cases in the TranslationProviderAdapterTest class to validate the
correctness of your adapter classes. These test cases will ensure that your adapters have the required methods and
interact with the provider APIs properly.
'''

# flow
'''
(CLIENT)
┌───────────────────────┐
│  Translation Tool App │
└───────────────────────┘
           │
           ▼
(TARGET INTERFACE)
┌────────────────────────────────────────────┐
│        TranslationProviderAdapter          │
├────────────────────────────────────────────┤
│ + translate(text: str, to_lang: str)       │
│ + get_supported_languages()                │
└────────────────────────────────────────────┘
           ▲                     ▲                    ▲
           │                     │                    │
           │                     │                    │
┌──────────────────┐   ┌──────────────────────┐   ┌──────────────────┐
│ GoogleAdapter     │   │ MicrosoftAdapter     │   │ YandexAdapter     │
├──────────────────┤   ├──────────────────────┤   ├──────────────────┤
│ + translate(...)  │   │ + translate(...)      │   │ + translate(...)  │
│ + get_supported.. │   │ + get_supported..     │   │ + get_supported.. │
└──────────────────┘   └──────────────────────┘   └──────────────────┘
        ▲                       ▲                       ▲
        │ uses                  │ uses                  │ uses
        ▼                       ▼                       ▼
┌──────────────────┐   ┌──────────────────────┐   ┌──────────────────┐
│ GoogleTranslateApi│   │ MicrosoftTranslateApi│   │ YandexTranslateApi│
├──────────────────┤   ├──────────────────────┤   ├──────────────────┤
│ + fetchTranslation│   │ + runTranslation     │   │ + doTranslate     │
│ + listLangs       │   │ + getAvailableLangs  │   │ + supportedLangs  │
└──────────────────┘   └──────────────────────┘   └──────────────────┘
'''

# step1: define a common interface / Target interface ie: TranslationProviderAdapter
from abc import ABC, abstractmethod

class TranslationProviderAdapter(ABC):

    @abstractmethod
    def translate(self, text: str, to_lang: str) -> str:
        pass

    @abstractmethod
    def get_supported_languages(self) -> list:
        pass

# -----------------------------------------------------------------------------

# step2: check the adaptee which your going to integrate in your application...

class GoogleTranslateApi:

    def __init__(self):
        self.google_supported_languages = [
    "en", "es", "fr", "de", "it", "pt", "ru", "zh", "ja", "ko", "ar", "hi", "bn", "pa", "mr", "gu", "ta", "te",
    "ml", "kn", "th", "tr", "pl", "ro", "sv", "nl", "cs", "el", "he", "uk", "id", "vi", "ms", "tl", "sr", "hr", "bs",
    "lt", "lv", "sq", "no", "fi", "da", "sk", "hu", "et", "bg", "sl", "mt", "is", "ca", "eu", "gl", "hi", "mr", "gu"
    ]

    def fetchTranslation(self, text: str, target_language: str) -> str:
        # Simulate fetching translation from Google Translate API
        return f"Google Translated '{text}' to '{target_language}'"

    def listLangs(self)-> list:
        return self.google_supported_languages


class MicrosoftTranslateApi:

    def __init__(self):
        self.microsoft_supported_languages = [
    "en", "es", "fr", "de", "it", "pt", "ru", "zh", "ja", "ko", "ar", "hi", "bn", "mr", "pa", "gu", "ta", "ml", "kn",
    "te", "th", "tr", "pl", "ro", "sv", "nl", "cs", "el", "uk", "id", "vi", "ms", "tl", "sr", "hr", "bs", "lt", "lv",
    "sq", "no", "fi", "da", "sk", "hu", "et", "bg", "sl", "mt", "is", "ca", "eu", "gl", "hi", "mr", "gu"
    ]

    def runTranslation(self, text: str, lang_code: str)-> str:
        return f"Microsoft Translated '{text}' to '{lang_code}'"

    def getAvailableLangs(self)-> list:
        return self.microsoft_supported_languages

class YandexTranslateApi:

    def __init__(self):
        self.yandex_supported_languages = [
    "en", "es", "fr", "de", "it", "pt", "ru", "zh", "ja", "ko", "ar", "hi", "bn", "pa", "mr", "gu", "ta", "te", "ml",
    "kn", "th", "tr", "pl", "ro", "sv", "nl", "cs", "el", "he", "uk", "id", "vi", "ms", "tl", "sr", "hr", "bs", "lt",
    "lv", "sq", "no", "fi", "da", "sk", "hu", "et", "bg", "sl", "mt", "is", "ca", "eu", "gl", "ht", "af", "ne", "cy",
    "zh-cn", "zh-tw", "ka", "kk", "uz", "ky", "mr", "gu", "te", "pa"
    ]

    def doTranslate(self, txt: str, to: str)-> str:
        return f"Yandex Translated '{txt}' to '{to}'"

    def supportedLangs(self)->list:
        return self.yandex_supported_languages

# ---------------------------------------------------------------------------------------------------------------------

# step3: create a adapter which should fit with the translation API service provider

class GoogleAdapter(TranslationProviderAdapter):

    def __init__(self, provider: GoogleTranslateApi):
        self.provider = provider

    def translate(self, text: str, to_lang: str) -> str:
        return self.provider.fetchTranslation(text,to_lang)

    def get_supported_languages(self) -> list:
        return self.provider.listLangs()

class MicrosoftAdapter(TranslationProviderAdapter):

    def __init__(self, provider: MicrosoftTranslateApi):
        self.provider = provider

    def translate(self, text: str, to_lang: str) -> str:
        return self.provider.runTranslation(text, to_lang)

    def get_supported_languages(self) -> list:
        return self.provider.getAvailableLangs()

class YandexAdapter(TranslationProviderAdapter):

    def __init__(self, provider: YandexTranslateApi):
        self.provider = provider

    def translate(self, text: str, to_lang: str) -> str:
        return self.provider.doTranslate(text, to_lang)

    def get_supported_languages(self) -> list:
        return self.provider.supportedLangs()

class TranslationProviderAdapterTest:

    @staticmethod
    def test(adapter: TranslationProviderAdapter):
        translation = adapter.translate("Hello, world!", "es")
        print(translation)
        languages = adapter.get_supported_languages()
        print(languages)
        assert isinstance(translation, str)
        assert isinstance(languages, list)
        assert len(languages) > 0
        print("All tests passed!")

if __name__ == "__main__":
    google_api = GoogleTranslateApi()
    google_adapter = GoogleAdapter(google_api)
    TranslationProviderAdapterTest.test(google_adapter)

    microsoft_api = MicrosoftTranslateApi()
    microsoft_adapter = MicrosoftAdapter(microsoft_api)
    TranslationProviderAdapterTest.test(microsoft_adapter)

    yandex_api = YandexTranslateApi()
    yandex_adapter = YandexAdapter(yandex_api)
    TranslationProviderAdapterTest.test(yandex_adapter)
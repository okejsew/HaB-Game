import json


class Locale:
    current_locale: dict[str, str] = {}

    @staticmethod
    def load(lang: str):
        with open(f'resources/locales/{lang}.json', 'r', encoding='utf-8') as file:
            Locale.current_locale = json.load(file)

    @staticmethod
    def get(code: str):
        try:
            return Locale.current_locale[code]
        except KeyError:
            return 'Locale Not Found'

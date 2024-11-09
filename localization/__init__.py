import json5


class Locale:
    current_locale: dict[str, str] = {}

    @staticmethod
    def load(lang: str):
        with open(f'resources/locales/{lang}.json5', 'r', encoding='utf-8') as file:
            Locale.current_locale = json5.load(file)

    @staticmethod
    def get(code: str):
        try:
            return Locale.current_locale[code]
        except KeyError:
            return 'Locale Not Found'

Locale.load('ru')

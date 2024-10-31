import importlib.util
import os
import re
import sys

from game.localization import Locale
from tui import Tui, BaseElement


class TuiFabric:
    element_classes = {}

    @staticmethod
    def load_element_classes():
        elements_dir = os.path.join(os.path.dirname(__file__), 'elements')

        for filename in os.listdir(elements_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                module_path = os.path.join(elements_dir, filename)

                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)

                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if isinstance(attr, type) and issubclass(attr, BaseElement) and attr is not BaseElement:
                        TuiFabric.element_classes[attr_name] = attr

    @staticmethod
    def load(path: str):
        if not TuiFabric.element_classes:
            TuiFabric.load_element_classes()

        tui = Tui()
        current_element = None
        element_pattern = re.compile(r'(\w+):')
        attr_pattern = re.compile(r'(\w+)\s*=\s*(.+)')

        with open(path, 'r', encoding='UTF-8') as file:
            for line in file:
                line = line.strip()

                element_match = element_pattern.match(line)
                if element_match:
                    element_type = element_match.group(1)
                    element_class = TuiFabric.element_classes.get(element_type)

                    if element_class:
                        current_element = element_class()
                        tui.add(current_element)
                    continue

                attr_match = attr_pattern.match(line)
                if attr_match and current_element:
                    attr_name, attr_value = attr_match.groups()

                    # Обработка значений атрибутов
                    if attr_value.startswith("'") and attr_value.endswith("'"):
                        attr_value = attr_value[1:-1]
                        if attr_value.startswith('@'):
                            attr_value = Locale.get(attr_value.strip('@'))
                    elif attr_value.isdigit():
                        attr_value = int(attr_value)
                    elif attr_value in ['True', 'False']:
                        attr_value = attr_value == 'True'

                    setattr(current_element, attr_name, attr_value)
        return tui

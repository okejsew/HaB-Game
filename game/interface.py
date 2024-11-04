from game import Game, Locale
from game.base.item import ItemContextMenu
from tui import Tui
from tui.elements.button import Button, ButtonStyle
from tui.elements.label import Label
from tui.fabric import TuiFabric


class Menu:
    main: Tui
    inventory: Tui
    item_context: Tui

    @staticmethod
    def setup():
        Menu.inventory = Tui()
        Menu.item_context = Tui()
        Menu.main = TuiFabric.load('resources/ui/main.tui')
        Menu.main.get('btn_exit', Button).click = Game.exit
        Menu.main.get('btn_inventory', Button).click = lambda: (Menu.main.close(), Menu.open_inventory())

    @staticmethod
    def open_inventory():
        Menu.inventory.elements.clear()
        Menu.inventory.add(Label(f'{Locale.get("inventory")} {Game.player.name}:'))

        for item in Game.player.inventory:
            def make_item_handler(item):
                return lambda: Menu.open_item_context(item.context_menu)

            btn = Button(str(item), make_item_handler(item), ButtonStyle.Cursor)
            Menu.inventory.add(btn)

        Menu.inventory.add(Button(Locale.get('back'), lambda: (Menu.inventory.next(Menu.main.show))))
        Menu.inventory.show()

    @staticmethod
    def open_item_context(icm: ItemContextMenu):
        Menu.item_context.elements.clear()
        Menu.item_context.elements += icm.elements
        Menu.item_context.add(Button(Locale.get('back'), lambda: Menu.item_context.next(Menu.open_inventory)))
        Menu.item_context.show()

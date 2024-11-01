import curses

from game.base.entities.player import Player
from game.base.item import BaseItem, ItemContextMenu
from game.base.items.armor import Armor
from game.base.items.usable import Usable
from game.base.items.weapon import Weapon
from game.localization import Locale
from tui import Tui
from tui.elements.button import Button, ButtonStyle
from tui.elements.label import Label
from tui.fabric import TuiFabric


class Menu:
    main: Tui
    inventory: Tui

    @staticmethod
    def setup():
        Menu.inventory = Tui()
        Menu.main = TuiFabric.load('game/resources/ui/main.tui')
        Menu.main.get('btn_exit', Button).click = HaB.exit
        Menu.main.get('btn_inventory', Button).click = lambda: (Menu.main.close(), Menu.open_inventory())

    @staticmethod
    def open_inventory():
        Menu.inventory.elements.clear()
        Menu.inventory.add(Label(f'{Locale.get("inventory")} {HaB.player.name}:'))
        for item in HaB.player.inventory:
            Menu.inventory.add(Button(str(item),
                                      lambda: Menu.open_item_context(item.context_menu),
                                      ButtonStyle.Cursor))
        Menu.inventory.add(Button(Locale.get('back'), lambda: (Menu.inventory.next(Menu.main.show))))
        Menu.inventory.show()



    @staticmethod
    def open_item_context(icm: ItemContextMenu):
        tui = Tui()
        tui.elements += icm.elements
        tui.add(Button(Locale.get('back'), lambda: tui.next(Menu.open_inventory)))
        tui.show()

class HaB:
    player: Player = Player()

    @staticmethod
    def exit():
        curses.endwin()
        Tui.end()
        exit()

    @staticmethod
    def add_item(item: BaseItem):
        if item not in HaB.player.inventory:
            HaB.player.inventory.append(item)
            item.owner = HaB.player

    @staticmethod
    def init():
        Locale.load('ru')
        HaB.add_item(BaseItem())
        HaB.add_item(Weapon())
        HaB.add_item(Armor())
        HaB.add_item(Usable())
        Menu.setup()

    @staticmethod
    def start():
        Menu.main.show()

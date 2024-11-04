from game import Game
from utils.dialog import DialogFabric

Game.init()
dialog = DialogFabric.load('greeting')
dialog.start()
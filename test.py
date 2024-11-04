from game.base.dialogue import Phrase, Dialog

dialog = Dialog()
dialog.phrases.append(Phrase('Trevor 1: Hello, my name is trevor, whats your?\n'))
dialog.phrases.append(Phrase('Trevor 2: Hello, my name is trevor, im good, and you?\n'))
dialog.phrases.append(Phrase('Trevor 3: Im good too, goodbye!\n'))
dialog.start()
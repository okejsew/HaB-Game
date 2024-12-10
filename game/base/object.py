class Object(object):
    __uid = 0
    objects = []

    def __init__(self, name: str):
        self.name = name
        self.uid = Object.__uid
        Object.__uid += 1

    def __repr__(self):
        return f'{self.name[:10].ljust(10)} [UID={self.uid}]'+ f'[{self.__class__.__name__}]'[:10].ljust(10)
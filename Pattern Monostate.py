class Monostate:
    __shared_attrs__ = {
        'name': 'mono_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs__

# need run this code in console
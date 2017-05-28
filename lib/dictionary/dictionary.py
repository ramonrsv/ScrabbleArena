import abc


class Dictionary(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def valid_word(self, word):
        return True

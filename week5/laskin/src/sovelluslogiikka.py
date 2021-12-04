class ApplicationLogic:
    def __init__(self, value=0):
        self.value: int = value
        self.__previous = value

    def subtract(self, arvo):
        self.__previous = self.value
        self.value = self.value - arvo

    def add(self, arvo):
        self.__previous = self.value
        self.value = self.value + arvo

    def zero(self, _ = 0):
        # _ is to simply all functions have equal arguments
        self.value = 0

    def set_value(self, value):
        self.value = value

    def undo(self, _ = 0):
        # _ is to simply all functions have equal arguments
        self.value = self.__previous

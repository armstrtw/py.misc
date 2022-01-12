from abc import ABC, abstractmethod

class Cat(ABC):
    @abstractmethod
    def talk(self, meow_type):
        pass

class BlackCat(Cat):
    pass

black_cat = BlackCat()

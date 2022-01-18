from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass


class Piano(Instrument):
    def play(self):
        print("Chopin")

class Guitar(Instrument):
    def play(self):
        print("I've got friends in low places.")

piano_instance = Piano()
piano_instance.play()

guitar = Guitar()
guitar.play()

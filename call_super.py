class Base:
    def __init__(self,name):
        self.name = name

class Child(Base):
    def __init__(self,number,name):
        super().__init__(name)
        self.number = number


c = Child(2,"Bob")
print(c.number)
print(c.name)

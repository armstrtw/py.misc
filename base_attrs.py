class Base:
    base_name = "I am groot"
    other_name = "base"
    def __init__(self):
        self.something = "from base"


class Child(Base):
    child_name = "I am twig"
    other_name = "child"
    def __init__(self):
        self.something = "from child"
        super().__init__()

c = Child()
print(c.something)
print(c.child_name)
print(c.base_name)
print(c.other_name)
for k, v in c.__dict__.items():
    print(k, v)
#assert c.something == "from base"
#assert c.something_else == "from child"
#assert c.__dict__["something"] == "from base"

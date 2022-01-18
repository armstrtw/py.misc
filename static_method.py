class Cat:
    def __init__(self,name):
        self.name = name

    @staticmethod
    def meow():
        print("meow")
        ## needs self param to access members, which is not passed automatically when invoked
        ## this will fail with: NameError: name 'self' is not defined
        ##print(self.name)



cat = Cat("Hercules")
print(f"{cat.name}, says hi")
cat.meow()

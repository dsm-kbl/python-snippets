class car:
    name = "Ford"
    color = "white"
    model = 2020

    def display1(self):
        print(self.name)
        print(self.color)
        print(self.model)


c = car()
print(getattr(c, "name"))
print(hasattr(c, "name"))
print(setattr(c, "name", "BM1"))
print(setattr(c, "name", "BM2"))
print(getattr(c, "name"))
print(delattr(c, "name"))
print(c.name, c.model, c.color)

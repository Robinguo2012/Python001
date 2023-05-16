
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

class Dog:
    classTrick = ["four feet", "tail"]

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)
    

dannie = Dog("dannie")
ana = Dog("ana")
dannie.add_trick("jump")
ana.add_trick("run")

print(dannie.tricks)
print(dannie.classTrick)

print(ana.tricks)
print(ana.classTrick)

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


mapping = Mapping([1,2,3])
print(mapping)


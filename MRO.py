class Animal:
    print("animals")


class Mammals(Animal):
    print("Mammals")


class Reptiles(Animal):
    print("Reptiles")


class Dog(Mammals):
    print("Dog")


class Cat(Mammals):
    def show(self):
        print("Cat")


c = Cat()
c.show()

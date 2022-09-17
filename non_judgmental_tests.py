import inspect

class Animal:
    def hi(self):
        print('hi animal')

class Dog(Animal):
    def __init__(self) -> None:
        print(len(inspect.getmembers(Dog, predicate=inspect.isfunction)) == len(inspect.getmembers(Animal, predicate=inspect.isfunction))+1)

    def hi(self):
        print('hi from dog')




dog = Dog()
dog.hi()

class Animal():
    
    def __init__(self):
        print("Animal Created")
    
    def whom_am_i(self):
        print("I am an animal")
    
    def eat(self):
        print("I am eating")

class Dog(Animal):

    def __init__(self):
        super().__init__()
        print("Dog Created")

    def whom_am_i(self):
        print("I am a dog")
    
    def eat(self):
        print("I am a dog and eating")

dog = Dog()
dog.eat()
dog.whom_am_i()
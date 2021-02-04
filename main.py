class Animal():
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):

    def speak(self):
        return self.name + " says woof!"


# Polymorphism 

class Cat(Animal):

    def speak(self):
        return self.name + " says meow!"
    

biggie = Dog("biggie")
felix = Cat("felix")

def pet_speak(pet):
    print(pet.speak())

pet_speak(felix)
pet_speak(biggie)





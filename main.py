class Dog():

    species = 'mammal'

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self):
        print(f"woof my name is {self.name}.")
    

    

d = Dog(breed="Lab", name="KIA", spots=False)
d.bark()
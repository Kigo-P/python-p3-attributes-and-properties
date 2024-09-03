#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="fido", breed="Mastiff"):
        self.name = name
        self.breed = breed
    
    #creating a getter method
    def get_name(self):
        return self._name
    
    #creating a setter method
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else: 
            print("Name must be string between 1 and 25 characters.")
    
    #creating a property for getter and setter methods
    name = property(get_name, set_name)

    #creatig getter method for breed
    def get_breed(self):
        return self._breed
    
    #creating a setter method
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds." )
    
    #creating a property for getter and setter method:
    breed = property(get_breed, set_breed)
    pass



peter = Dog("Peter","Mastiff")
print(peter.name)
peter.name = "A very long name that is way too long"
print(peter.name)

peter = Dog("Peter","Mastiff")
peter = Dog("Peter","chiwawa")
#!/bin/python3

def my_pets(animal_type, name):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {name.title()}")
    
my_pets('dog', 'lilly')

my_pets(animal_type='dog', name='lilly')

def my_pet_defaulted(name, animal_type='cat'):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {name.title()}")

my_pet_defaulted('alf')



#!/bin/python3

dogs = ['ruby', 'winnie', 'lilly', 'amos', 'andy']

print(dogs)

print(dogs[0].title())
print(dogs[-1].upper())

print(f"My dog {dogs[2].title()} is laying beside me.")

#dogs[0] = 'shorty'
dogs.append('toby')

dogs.insert(0, 'shorty')

del dogs[0]

print(dogs)

popped_dogs = dogs.pop()
print(f"The brown dog, {popped_dogs.title()} passed away several years ago.")
print(f"The white dog, {dogs.pop(2).title()} is sleeping on the bed.")

dogs.remove('amos')

print(dogs)


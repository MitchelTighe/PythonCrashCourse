#!/bin/python3

#user_input = input("Taking your input\n")

#print(user_input)
#print(input("Test\n"))

name = input("Tell me your name: ")
print(f"Hello {name.title()}")

age = input("How old are you? ")

if int(age) < 18:
    print("There is still time")
else: 
    print(f"Dang, {int(age)}?")



#!/bin/python3

def greetings(names):
    for person in names:
        hello = print(f"Hello {person.title()}!")
        print(hello)

users = ['greg', 'james', 'nate', 'robert']
greetings(users)



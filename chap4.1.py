#!/bin/python3

workers = ['nate', 'chance', 'james', 'greg', 'tyler', 'robert']

for worker in workers[2:4]:
    print(worker.title())

for employee in workers[:3]:
    print(f"Hi there, {employee.title()}")
    print("Welcome to work!")

for value in range(1,10):
    print(value)

numbers = list(range(1,10))
print(numbers)

employee = workers[:]

print(employee)



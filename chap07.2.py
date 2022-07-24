#!/bin/python3

rental_cars = {
        'subaru': 'impreza',
        'mazda': 'x3',
        'toyota': 'carolla',
        'chevy': 'malibu',
        'nissan': 'altima',
        'hyundai': 'sonata'
        }

# print(rental_cars)

choice = input("What brand of car would you like? ")
formatted = choice.lower()

for car_choice in rental_cars.keys():
    if car_choice == formatted:
        print(f"Check if we have a {choice.title()} in stock.")
    else:
        print(f"I'm sorry, we don't have any {choice.title()}s in stock")
# There is a better way to do this


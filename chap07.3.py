#!/bin/python3

number = 1

while number < 5:
    print("number is " + str(number))
    number += 1

while True:
    city = input("Tell me your favorite city, or enter q to quit\n")

    if city == 'q':
        break
    else:
        print(f"I'd love to visit {city.title()}\n")


unconfirmed = ['mike', 'james', 'jack', 'greg']
confirmed = []

while unconfirmed:
    current = unconfirmed.pop()

    print(f"Verifing user: {current.title()}")
    confirmed.append(current)
    

print(confirmed)



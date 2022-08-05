#!/bin/python3

country_nums = { 
        'china': 13.5,
        'austraila': 3.2,
        'united states of america': 14,
        'argentina': 2.4,
        'india': 9.8,
        }

print(country_nums)

country_nums['austraila'] = 6

print(country_nums)

del country_nums['argentina']

print(country_nums)

for key, value in country_nums.items():
    print(f"\nKey: {key.title()}")
    print(f"Value: {value}\n")

for c in country_nums.keys():
    print(c.title())




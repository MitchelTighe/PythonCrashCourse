#!/bin/python3

country_nums = {
        'china': 13.5,
        'austraila': 3.2,
        'united states of america': 14,
        'argentina': 2.4,
        'india': 9.8,
        'norway': 4.1,
        'canada': 4.7,
        'colombia': 2.1,
        'chile': 2.3,
        'peru': 2.4,
        }


for c, n in country_nums.items():
    #print(f"The rating for {c.title()} is {n}")
    if n < 3:
        print(f"The countries with ratings lower than 3 are: {c.title()} with a rating of {n}")
    else:
        print(f"The countries with ratings greater than 3 are: {c.title()} with a rating of {n}")



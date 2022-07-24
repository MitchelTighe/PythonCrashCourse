#!/bin/python3

def format_cities(city, country):
    name = f"{city.title()}, {country.title()}"
    return name.title()

cities_name = format_cities('Washington DC', 'United States of America')
print(cities_name)

def city_dict(city, country):
    formatted = {'city': city.title(), 'country': country.title()}
    return formatted

test_build = city_dict('boulder', 'united states of america')
print(test_build)


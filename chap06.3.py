#!/bin/python3

donkeys = []

for donkey in range(30):
    new_donkey = {'color': 'white', 'value': 5, 'speed': 'medium'}
    donkeys.append(new_donkey)

for donkey_five in donkeys[:5]:
    print(donkey_five)
print("...")

print(f"Total: {len(donkeys)}")

monies = { 
        'stocks': ['VOO', 'SOXL', 'SPY'],
        'crypto': ['ROSE', 'AVAX', 'BTC']
        }

print(monies)

user_data = {
        'mitchel': {
            'first': 'mitchel',
            'last': 'tighe',
            'location': 'fairmont'
            }, 
        'mike': {
            'first': 'mike',
            'last': 'jones',
            'location': 'princeton',
            },
        }



print(user_data)
        



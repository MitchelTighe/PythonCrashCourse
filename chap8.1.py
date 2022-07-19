#!/bin/python3

def user_greeting():
    user = input("Get user's name")
    print(f"Hello {user.title()}")

def specific_user_greeting(username):
    print(f"Hello, {username.title()}!")

specific_user_greeting('mitchel')

def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book('All quiet on the western front')


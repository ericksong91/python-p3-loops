#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    
    print("Happy New Year!")

def square_integers(int_list):
    square_ints = [element * element for element in int_list]
    return square_ints

def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 != 0):
            print("Fizz")
        elif (i % 5 == 0) and (i % 3 != 0):
            print("Buzz")
        elif i % 15 == 0:
            print("FizzBuzz")
        else:
            print(i)
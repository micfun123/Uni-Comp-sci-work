import math


def speed_calculator():
    distance = int(input("How far have you traveled: "))
    duration = int(input("What was duration: "))
    print(f"Your going a {distance/duration} km/h")

def circumference_of_circle():
    radius = int(input("Enter the radius: "))
    print(f"The circumference is {2 * math.pi * radius}")

def cost_of_pizza():
    dim = int(input("Enter the diameter: "))
    area = (dim/2) ** 2 * math.pi
    cost_in_pence = area*3.5
    cost_pounds = cost_in_pence / 100
    print(f"The cost is {round(cost_pounds,2)} pounds")

def slope_of_line():
    x_1 = int(input("Enter x_1: "))
    y_1 = int(input("Enter y_1: "))
    x_2 = int(input("Enter x_2: "))
    y_2 = int(input("Enter y_2: "))
    print(f"the gradent is {(y_2-y_1)/(x_2-x_1)}")

def distance_between_points():
    x_1 = int(input("Enter x_1: "))
    y_1 = int(input("Enter y_1: "))
    x_2 = int(input("Enter x_2: "))
    y_2 = int(input("Enter y_2: "))
    print(f"The distance is {math.sqrt((x_2 - x_1) **2 + (y_2 - y_1) **2)}")

def travel_statistics():
    speed = int(input("Please enter a speed: "))
    duration = int(input("Please enter a duration: "))
    distance = speed * duration
    fuel = distance / 5
    print(f"You are going to go {distance} and use {fuel} fuel")

def sum_of_squares():
    n  = int(input("How many places do we go: "))
    total = 0
    for i in range(n):
        total = total + ((n+1)**2)
    print(total)

def average_of_numbers():
    amount = int(input("Enter the amount of numbers you want to avrage: "))
    total = 0
    for i in range(amount):
        total = total + int(input("Enter a number: "))
    print(f"the average is {total / amount}")

def fibonacci():
    place = int(input("What place of the fibonacci do you want to go up to: "))
    a = 0
    b = 1
    z = 1
    for i in range(place):
        print(z)
        z = a + b
        a = b
        b = z  
    print(z)
                 
def select_coins ():
    pence = int(input("Enter the amount of pence: "))
    pound2 = pence // 200
    pence = pence % 200
    pound1 = pence // 100
    pence = pence % 100
    pence50 = pence // 50
    pence = pence % 50
    pence20 = pence // 20
    pence = pence % 20
    pence10 = pence // 10
    pence = pence % 10
    pence5 = pence // 5
    pence = pence % 5
    pence2 = pence // 2
    pence = pence % 2
    print(f"You have {pound2} * £2, {pound1} * £1, {pence50} * £0.50, {pence20} * £0.20, {pence10} * £0.10, {pence5} * £0.05, {pence2} *  £0.02, {pence} *  £0.01")
    
    
    

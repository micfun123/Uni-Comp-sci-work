
def square_pizza():
    topping_region_length = int(input("Please Enter the length in cm for the topping area of the pizza: "))
    crust_width = int(input("Please Enter the width of the crust of the pizza in cm: "))
    
    total_length = crust_width + topping_region_length
    topping_region_area = topping_region_length * topping_region_length
    total_area = total_length * total_length
    crust_area = total_area - topping_region_area
    amount_of_toppings = topping_region_area // 40
    
    print(f"The total topping area is {topping_region_area} cm^2")
    print(f"The total length side size is {total_length} cm")
    print(f"The crust region area is {crust_area}")
    print(f"The amount of toppings are {amount_of_toppings}")
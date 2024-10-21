def biscuitCutting():
    amount_biscuits = int(input("How many biscuits do you want to make? "))
    radius_biscuits = int(input("What is the radius of the biscuits? "))
    diamitor_biscuit = radius_biscuits * 2
    length_mixture = diamitor_biscuit * amount_biscuits
    print(f"The width is {diamitor_biscuit} and the mixture is {length_mixture} long")


def say_name(name :str):
    print(f"Hello {name}")

def say_hello_2():
    print("hello")
    print("name")


def dollars_to_pounds(dollars :float):
    print(f"You have {dollars / 1.35} pounds")



def sum_and_difference():
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    print(f"The sum of your two numbers is {num1 + num2}")
    print(f"The Diffence between your two numbers is {num1 - num2}")



def change_counter():
    one_pence = int(input("How many one pence do you have: "))
    two_pence = int(input("How many two pence do you have: "))
    five_pence = int(input("How many five pence do you have: "))
    print(f"You have a toatl of {one_pence + two_pence *2 + five_pence * 5} pence")

change_counter()

def ten_hellos():
    #print("Hello World \n" * 10)
    for i in range(0,10):
        print("Hello World")



def zoom_zoom():
    zoomamount = int(input("How many zooms: "))
    for i in range(1,zoomamount+1):
        print(f"Zoom {i}")



def count_to():
    amount = int(input("How many do you want to count to"))
    for i in range(1,amount+1):
        print(i)

def count_from_to():
    startnum = int(input("Where do you want to start counting from"))
    endnum = int(input("where do you want to stop counting from"))
    for i in range(startnum,endnum+1):
        print(i)


def weights_table():
    start = 0
    for i in range(0,100,10):
        start += 10
        print(f"{start} | {start * 35.274}")
        

weights_table()

def future_value():
    inv_amt = float(input("How much do you want to invest for: "))
    years = int(input("How many years are you investing for: "))
    for i in range(0,years):
        inv_amt = inv_amt*1.035
        print(f"At end of {i+1} you will have {round(inv_amt,2)}")

future_value()
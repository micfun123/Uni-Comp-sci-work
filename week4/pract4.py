import os
from graphix import Window, Point, Circle, Line, Rectangle, \
                    Polygon, Text, Entry

def student_info():
    course = input("What's your course? ")
    student_id = input("What's your ID number? ")
    print("Welcome to:\t" + course)
    print("\n" * 2 + "Your ID number is:\t" + student_id[2:])


def personal_details():
    name = input("What's your name? ")
    age = int(input("What's your age? "))
    height = float(input("What's your height? "))
    # print("name:\t{:>10}\nage:\t{:>10}\nheight:\t{:>10.2f}".format(name, age, height))
    print(f"name:\t{name:>10}\nage:\t{age:>10}\nheight:\t{height:>10.2f}")


def read_quote():
    print("Current directory:\t" + os.getcwd())
    print("Files in current directory:\t" + str(os.listdir()))
    # Change directory to the folder containing quotation.txt
    os.chdir("text_files")
    # Checking if quotation.txt is in the current directory:
    print("Current directory:\t" + os.getcwd())
    print("Files in current directory:\t" + str(os.listdir()))

    input_file = open("quotation.txt", "r")

    # You can use `read()` to read the whole file into a single string
    content = input_file.read()
    print(content)


def write_quote():
    os.chdir("text_files")
    output_file = open("my_quotation.txt", "w")

    # You can use `write()` to write a single string
    print("I love Python!", file=output_file)
    print("(Matthew Poole)", file=output_file)

    # Or write both lines in one go separated by a newline character ('\n')
    # content = "I love Python!\n(Matthew Poole)"
    # output_file.write(content)



def personal_greeting():
    name = input("What's your name? ")
    print(f"Hello {name}! How are you today?")

def formal_name():
    first_name = input("What's your first name? ")
    last_name = input("What's your last name? ")
    print(f"Your formal name is {first_name[0]}. {last_name.upper()}")
    
def kilos_to_ounces():
    kilo = float(input("Enter a weight in kilograms: "))
    ounces = kilo * 35.274
    print(f"{kilo:.2f} kilograms is equal to {ounces:.2f} ounces")
    

def generate_email():
    last_name = input("Enter your last name: ")
    first_name = input("Enter your first name: ")
    year = input("Enter the year you started at the university: ")
    print(f"Your university email is {last_name.lower()[:4]}.{first_name.lower()[:1]}.{year[2:]}@myport.ac.uk")
    

def grade_test():
    mark = int(input("Enter your mark: "))
    grades = "FFFFCCBBAAA"
    print(f"Your grade is {grades[mark]}")
    
def graphic_letters():
    word = input("Enter a word: ")
    win = Window()
    for i in range(len(word)):
        mouseclick = win.get_mouse()
        text = Text(mouseclick, word[i])
        text.draw(win)
        

def sing_a_song():
    word = input("Enter a word: ")
    amount_of_lines = int(input("How many lines do you want: "))
    words_per_line = int(input("How many words per line: "))    
    word = word + ' '
    for i in range(amount_of_lines):
        print(word * words_per_line)
        
def exchange_table():
    for i in range(21):
        print(f" €{i}| £{i/1.75:.2f}")
        print("_" * 15)

def make_initialism():
    phrase = input("Please Enter a phrase: ")
    result = ""
    for i in phrase.split():
        result=result + i.upper()[0]
    print(result)
    
def file_in_caps():
    filename = input("Please Enter the file name: ") 
    text_file = open(filename,'r')
    print(text_file.read().upper())
    

def total_spending():
    text_file = open("spending.txt",'r')
    total = 0
    for i in text_file.readlines():
        total = total + float(i)
    print(f"Your total is {total}")

def name_to_number():
    name = input("Please Enter a name: ")
    total = 0
    for i in name:
        total = total + ord(i)
    print(f"The value of the name is {total}")

def rainfall_chart():
    text_file = open("rainfall.txt",'r')
    for i in text_file.readlines():
        amount_of_rain = int(i.split()[1])
        city_name = i.split()[0]
        print(f"{city_name} | {amount_of_rain * '*'}")

def wc():
    file_name = input("Please Enter the file name: ")
    text_file = open(file_name,'r')
    lines = 0
    words = 0
    characters = 0
    for i in text_file.readlines():
        lines += 1
        words += len(i.split())
        characters += len(i)
    print(f"There is {lines} lines, There are {words} Words, There are {characters}") 
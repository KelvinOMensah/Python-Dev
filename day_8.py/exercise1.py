# Creating functions

def my_function():
    print("Hello")
    print("Good morning")
    print("Welcome")

my_function()

# functions with one input

def greet(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet("Kellyy")

# functions with more than one input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How is it like in {location}?")

greet_with("Kel", "Accra")

# functions with keyword arguments

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How is it like in {location}?")

greet_with(name = "Kel", location = "Accra")
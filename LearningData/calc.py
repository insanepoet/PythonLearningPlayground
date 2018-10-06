

# Python Calculator
import re

print("My Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True
equation = ""


def do_maths():
    global run
    global previous
    global equation

    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    if equation == "quit":
        print("Goodbye !")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.)_:" "]', '', equation)  # Strip possible code injection

        if previous == 0:
            previous == eval(equation)  # If this is the first run lets do math on the equation
        else:
            previous = eval(str(previous) + equation)  # If we have done other math have the option to include


while run:
    do_maths()

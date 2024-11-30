
def simple_calculator( ):
    num1 = float(input("enter num1"))
    num2 = float(input("enter num2"))

    print ("enter an option")
    print ("1. Add")
    print ("2. Sub")
    print ("3.Multiply")
    print ("4.Divide")

    operation = int(input("enter an operation"))
    if (operation == 1):
        print (f"result = {num1 + num2}")
    elif (operation == 2):
        print (f"result = {num1 - num2}")
    elif (operation == 3):
        print (f"result = {num1 * num2}")
    elif (operation == 4):
        print (f"result = {num1 / num2}")
    else:
        print ("operation invalid enter option 1/2/3/4")

simple_calculator()
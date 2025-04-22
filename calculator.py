def calculate(op,num1,num2):
    if op == '+':
        return num1 + num2

    elif op == '-':
       return num1 - num2

    elif op == '*':
        return num1 * num2

    elif op == '/':
        if num2 == 0:
            print("A number can't be divided by zero")
        else:
            return num1 / num2

     



op= input("Select an operator: ")
num1 = float(input("First number: "))
num2 = float(input("Second number: "))



print(f"Your answer is {calculate(op,num1,num2)}")
print("Thank you for using the calculator")
print("Welcome to the basic calculator!")
num1 = (float(input("Enter your first number: ")))
num2 = (float(input("Enter your second number: ")))
operator = input(" Please add your own operator( +, -, /, *): ")
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "error!"
else:
    result = "Invalid operator"
print("result=", result)
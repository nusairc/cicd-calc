class Calculator:

    def add(self,x, y):
        return x + y

    def subtract(self,x, y):
        return x - y

    def multiply(self,x, y):
        return x * y

    def divide(self,x, y):
        if y == 0:
            return "Error: Division by zero"
        else:
            return x / y

# print(" operations choice:")
# print("+. Add")
# print("-. Subtract")
# print("*. Multiply")
# print("/. Divide")

# while True:
#     choice = input("Enter operation: ")

#     # Check if choice is one of the four options
#     if choice in ('+', '-', '*', '/'):
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             continue

#         if choice == '+':
#             print(num1, "+", num2, "=", Calculator.add(num1, num2))
#         elif choice == '-':
#             print(num1, "-", num2, "=", Calculator.subtract(num1, num2))
#         elif choice == '*':
#             print(num1, "*", num2, "=", Calculator.multiply(num1, num2))
#         elif choice == '/':
#             print(num1, "/", num2, "=", Calculator.divide(num1, num2))

#         next_calculation = input("Let's do the next calculation? (yes/no): ")
#         if next_calculation.lower() == "no":
#             break
#     else:
#         print("Invalid Input")

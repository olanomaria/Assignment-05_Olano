#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 15:38:27 2024

@author: maritaolano
"""
class BasicMathOperations:
    def greet_user(self, first, last): 
        # Set variable fullname to get arguments' first and last name together 
        full_name = first + " " + last 
        # display results
        print(f"Hello, {full_name}!") 
    
    def add_numbers(self, first, second):
        # Computes the sum of two numbers 
        sum = first + second 
        # Displays results 
        print(f"The total sum is: {sum}") 
        
    def perform_operation(self, num1, num2, op):
            # Conditioners to set and compute operation 
            if op == "+":
                ans = num1 + num2
            elif op == "-":
                ans = num1 - num2
            elif op == "*":
                ans = num1 * num2
            elif op == "/":
                if num2 != 0: # If denominator in division = 0 then print "Invalid" 
                    ans = num1 / num2
                else:
                    print("Invalid: Division not allowed.")
                    return
            else:
                print("Invalid operator. Try again!")
                return None
            # Display results 
            print(f"Result of {num1} {op} {num2} is: {ans}")
            return 
    
    def square_num(self, num):
        # Compute operation to square a number
        square = num * num
        # Displays results
        print(f"The square of {num} is: {square}")
        
    def factorial(self, num):
        result = 1
        if num >= 0: # if number is greater or equal to 0 
            # start loop for in a range from 2 to the given number
            for i in range(2, num + 1):
                # set variable 'result' to multiply number by all numbers in corresponding range 
                result *= i 
            # Display results 
            print(f"The factorial of {num} is: {result}")
            return result
        else: # error sintax 
            print("Invalid operation.")
            return
    
    def counting(self, start, end):
        # makes sure that start number is less than end number
        if start < end:
            # starts loop to print the numbers in given range 
            for i in range(start, end + 1):
                # displays result
                print(i, end=" ")
        else:
            print("Invalid range. Try again!") # error sintax
            
    def calculateSquare(self, num):
        # computes the square of a given number 
        square = num * num
        # displays result 
        return square 

    def calculateHypotenuse(self, base, per):
        # calculate the sum of the squares of base and perpendicular sides
        hypo = self.calculateSquare(base) + self.calculateSquare(per)
        # calculate the hypotenuse (square it)
        result = self.calculateSquare(hypo)
        # display result 
        print(f"\nThe hypotenuse is: {result}")
        return
    
    def areaofrectangle_values(self, width, height):
        # Calculate the area using the provided width and height
        area = width * height
        # Display the results 
        print(f"The area is: {area}")
        return 

    def areaofrectangle_variables(self):
        # Get user input for width and height
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        # Calculate the area using the user-provided width and height
        area = width * height
        # Display the results
        print(f"The area is: {area}")
        return
    
    def powerofnumber(self, base, exp):
        # Calculate the power 
        power = base ** exp 
        # Display the results
        print(f"{base} raised to the power of {exp} is: {power}")
        return 
    
    def typeofargument(self, arg):
        # gets the data type of the argument
        arg_type = type(arg)
        # Displays results 
        print(f"The type of the argument {arg} is: {arg_type}")
        return
    
def main():
    # Set an instance of the BasicMathOperations class
    math_operations = BasicMathOperations()
    # Display the menu of operations 
    print("1. Greet User")
    print("2. Add Numbers")
    print("3. Perform Operation")
    print("4. Square a Number")
    print("5. Factorial")
    print("6. Counting")
    print("7. Calculate Hypotenuse")
    print("8. Area of Rectangle (Values)")
    print("9. Area of Rectangle (Variables)")
    print("10. Power of a Number")
    print("11. Type of Argument")
    print("0. EXIT")
    # Prompt user to choose a task 
    choice = input("Choose your task 1-11: ")
    
    # Computes the selected task 
    if choice == "1":
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        math_operations.greet_user(first_name, last_name)
    elif choice == "2":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        math_operations.add_numbers(num1, num2)
    elif choice == "3":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        op = input("Enter the operation (+, -, *, /): ")
        math_operations.perform_operation(num1, num2, op)
    elif choice == "4":
        num = float(input("Enter a number: "))
        math_operations.square_num(num)
    elif choice == "5":
        num = int(input("Enter a non-negative integer: "))
        math_operations.factorial(num)
    elif choice == "6":
        start = int(input("Enter the start number: "))
        end = int(input("Enter the end number: "))
        math_operations.counting(start, end)
    elif choice == "7":
        base = float(input("Enter the base of the triangle: "))
        per = float(input("Enter the perpendicular of the triangle: "))
        math_operations.calculateHypotenuse(base, per)
    elif choice == "8":
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        math_operations.areaofrectangle_values(width, height)
    elif choice == "9":
        math_operations.areaofrectangle_variables()
    elif choice == "10":
        base = float(input("Enter the base: "))
        exp = float(input("Enter the exponent: "))
        math_operations.powerofnumber(base, exp)
    elif choice == "11":
        argument = input("Enter an argument: ")
        math_operations.typeofargument(argument)
    elif choice == "0":
        print("Goodbye!")
    else:
        print("Try again! Choose your task 1-11")

main()


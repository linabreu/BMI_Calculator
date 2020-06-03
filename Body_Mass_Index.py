#!/usr/bin/env python3

#basic procedural program. Gets user entry and performs calculations

print("Welcome to the Body Mass Index Caclulator")
print()

print("Please note this BMI calculator uses the American System")
print()

height = int(input("Please enter your height in inches: "))
weight = int(input("Please enter your weight in pounds: "))
print()


BMI = round(float((weight/height/height) * 703),2)
print("Your BMI is: ", BMI)

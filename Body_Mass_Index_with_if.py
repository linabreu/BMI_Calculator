#!/usr/bin/env python3

#extension of BMI program
#adds if clause to print body weight classification based on calculated BMI

print("Welcome to the Body Mass Index Caclulator")
print()

print("Please note this BMI calculator uses the American System")
print()

height = int(input("Please enter your height in inches: "))
weight = int(input("Please enter your weight in pounds: "))
print()


BMI = round(float((weight/height/height) * 703),2)
print("Your BMI is: ", BMI)

if BMI < 18.5:
    print("You are considered underweight")
elif BMI >= 18.5 and BMI < 25:
    print ("You are considered normal weight")
elif BMI >= 25 and BMI < 30:
    print ("You are considered overweight")
else:
    print ("You are considered obese")
    
print()
print("Thank you for using the BMI Calculator")






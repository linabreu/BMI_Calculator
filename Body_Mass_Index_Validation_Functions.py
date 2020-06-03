#!/usr/bin/env python3

##extension of BMI program with validation added to get_height and get_weight functions

#function to get users height
def get_height():
    valid_height = False
    
    height = int(input("Please enter your height in inches: "))
    print()
    while height <= 0:
            print ("Error. Height cannot be less than or equal to 0")
            height = int(input("Please reenter height in inches: "))
            print()
            if height > 0:
                valid_height = True
                return height

#function to get users weight
def get_weight():
    valid_weight = False
    
    weight = int(input("Please enter your weight in pounds: "))
    print()
    while weight <= 0:
            print ("Error. weight cannot be less than or equal to 0")
            weight = int(input("Please reenter weight in pounds: "))
            print()
            if weight > 0:
                valid_weight = True
                return weight
      

def main():
#display welcome message
    print("Welcome to the Body Mass Index Caclulator")
    print()

    print("Please note this BMI calculator uses the American System")
    print()

#set boolean to true so the program starts by entering the loop
    answer = "y"

#use while loop to allow for repeated entries
    while answer == "y" or answer.upper()== "Y": #so answer isnt case sensitive


    #get user input
        height = get_height()
        weight = get_weight()
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
    

    #give chance to exit loop or go again
        print()
        answer = input("Do you want to perform another BMI calculation? Type Y or Q to quit:  ")
        print()

    print("Thank you for using the BMI Calculator")

if __name__ == "__main__": main()




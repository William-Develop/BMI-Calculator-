
print("Hello, welcome to the BMI calculator!")
print("*"*40)
print("Enter your weight and height.")
print("*"*40)
height = input("What is your height in inches? ")
weigth = input("What is your weight in pounds? ")

if  len(height) == 0:
    print("Please enter your height.")
    exit()

if len(weigth) == 0:
    print("please enter your weight.")
    exit()

BMI = (float(weigth)* 703) / (float(height)*float(height))
BMI = round(BMI, 2)

if BMI < 16.0:
    print("*"*40)
    print(f"Your BMI is {BMI}, you are severly underweight.")
elif BMI >= 16.0 and BMI <= 18.4:
    print("*"*40)
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI >= 18.5 and BMI <= 24.9:
    print("*"*40)
    print(f"Your BMI is {BMI}, you have an average weight.")
elif BMI >= 25.0 and BMI <= 29.9:
    print("*"*40)
    print(f"Your BMI is {BMI}, you are moderately overweight.")
elif BMI >= 30.0 and BMI <= 34.9:
    print("*"*40)
    print(f"Your BMI is {BMI}, you are severly overweight.")
else:
    print("*"*40)
    print(f"Your BMI is {BMI}, you need to practice excersice and go on a diet.")
print("*"*40)
print("Thank you for using the BMI calculator!")
exit()
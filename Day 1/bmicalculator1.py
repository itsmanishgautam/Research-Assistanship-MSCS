# Write a program that calculates the Body Mass Index (BMI) and tells the user their BMI category (Underweight, Normal, Overweight, Obese).

print("Welcome to BMI Calculator")
Weight = int(input("Enter your Weight in Kg  "))
Height = float(input("Enter your Height in ft  "))

def BMI(x,y):
    heightmeter = y*0.3048
    bmivalue= (x/heightmeter**2)
    return bmivalue

bmivalue = BMI(Weight, Height)
print("Your BMI is", bmivalue)

if bmivalue<18.5:
    print("You are Underweight")
elif 18.5<=bmivalue<25:
    print("You are Normal Weight")
elif 25<=bmivalue<30:
    print("You are Overweight")
elif bmivalue>30:
    print("You are Obese")
else:
    print("Error")

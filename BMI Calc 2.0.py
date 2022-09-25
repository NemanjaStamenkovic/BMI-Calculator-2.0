from telnetlib import BM


print("Welcome to BMI Calculator")

height = float(input("Enter Your Height: "))
weight = int(input("Enter Your Weight: "))

BMI = round(weight / (height ** 2))

if BMI < 18.5:
    print(f"Your BMI is {int(BMI)}, you are underweight.")
elif BMI > 18.5  and BMI < 25:
    print(f"Your BMI is {int(BMI)}, you have a normal weight.")
elif BMI > 25 and BMI < 30:
    print(f"Your BMI is {int(BMI)}, you are slightly overweight.")
elif BMI > 30 and BMI < 35: 
    print(f"Your BMI is {int(BMI)}, you are obese.")
else:
    print(f"Your BMI is {int(BMI)}, you are clinically obese.")


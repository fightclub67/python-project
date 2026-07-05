print("welcome to BMI calculator!")
weight = float(input("how much do you weigh?: "))
height = float(input("how tall are you?: "))
BMI = weight/height**2
print("your BMI is:", BMI)
if BMI < 18.5:
    print("underweight")

elif 18.5 <= BMI < 25:
    print("normal weight")

elif 25 <= BMI < 30:
    print("overweight")

else:
    print("obese")
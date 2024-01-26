"""height=float(input("what is your height?"))
weight=int(input("what is you weight?"))
weight_as_int=int(weight)
height_as_float=float(height)
bmi=weight_as_int / height_as_float ** 2
bmi_as_int=int(bmi)
print(bmi_as_int)
"""

height=float(input("whats your height?"))
weight=float(input("what is your weight?"))
bmi=weight/(height*height)
if bmi <18:
    print(f"your BMI is {bmi}, you are underweight")
elif bmi <25:
    print(f"your BMI is {bmi}, you have normal weight")
elif bmi <30:
    print(f"your BMI is {bmi},you are slightly overweight")
elif bmi<35:
    print(f"your BMI is {bmi},you are obese")
else:
    print(f"your BMI is {bmi},you are clinically obese")
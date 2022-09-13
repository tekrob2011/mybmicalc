# 🚨 Don't change the code below 👇
heightft = int(input("enter your height in feet: "))
inches = int(input("pick 0-11 inches.: "))
weight = input("enter your weight in lbs.: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height = (heightft * 12) + inches
bmi = (int(weight) / (int(height **2))) * 703
bmi_as_int = int(bmi)
print(bmi_as_int)
if(bmi>0):
    if(bmi<=16):
        print(f"Your bmi is {bmi_as_int}.You are very underweight")
    elif(bmi<=18):
        print(f"Your bmi is {bmi_as_int}.You are underweight")
    elif(bmi<=25):
        print(f"Your bmi is {bmi_as_int}.You are Healthy")
    elif(bmi<=30):
        print(f"Your bmi is {bmi_as_int}.You are obese")
    else: 
        print(f"Your bmi is {bmi_as_int}.You are Clinically obese")

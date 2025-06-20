#This Python Program determines a user's BMI standing by using the official BMI formula 
# to calculate if they are underweight, normal, overweight or obese.
# Author: Thimna Shushu
# email: thimnashushu@gmail.com

print("Enter Your Height in cm: ")
height = int(input())
print("Enter Your Weight in kg: ")
weight=int(input())
print("Enter Your Age: ")
age=int(input())
print("Enter Your Gender (Male/Female): ")
gender=input()

#BMI Formula:

bmi = weight//(height**2)

category = ""
feedback=""
ageCat=0
threshold=0
if age>=19:
    
    def ageCategory(age):
        
        if age>20 and age<40:
            return  "20-39"
        elif age>39 and age<60:
            return "40-59"
        elif age>59:
            return "60+"
    
    ageCat = ageCategory(age) 
    categories={
        "20-39":{
            "male":   [(18.5, "Underweight"), (25, "Normal"), (30, "Overweight"), (float('inf'), "Obese")],
            "female": [(18.5, "Underweight"), (25, "Normal"), (30, "Overweight"), (float('inf'), "Obese")]
        },
        "40-59":{
            "male": [(20, "Underweight"), (27, "Normal"), (31, "Overweight"), (float('inf'), "Obese")],
            "female": [(20, "Underweight"), (28, "Normal"), (31, "Overweight"), (float('inf'), "Obese")]
            
        },
            
        "60+":{
            "male": [(22, "Underweight"), (28, "Normal"), (31, "Overweight"), (float('inf'), "Obese")],
            "female": [(22, "Underweight"), (29, "Normal"), (31, "Overweight"), (float('inf'), "Obese")]
            
        }
        
    }
    
    thresholds = categories[ageCat][gender.lower()]
   
    for threshold, category in thresholds:
            if bmi < threshold:
                feedback = category
    #Output
    print("============================")
    print("Your BMI Information:")
    print("Gender: ",gender,"\nAge: ",age,"\nBMI:",feedback)
    print("============================")
    
    



else:
    print("Your age is less than 19 years old.\nFor better advice, please consult with a medical proffessional.")
    

    

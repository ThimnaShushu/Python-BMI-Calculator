#This Python Program determines a user's BMI standing by using the official BMI formula 
# to calculate if they are underweight, normal, overweight or obese.
# Author: Thimna Shushu
# email: thimnashushu@gmail.com

import plotly.graph_objects as go

#from plotly_speedometer import SpeedometerController

print("Enter Your Height in cm: ")
height = float(input())
print("Enter Your Weight in kg: ")
weight=float(input())
print("Enter Your Age: ")
age=int(input())
print("Enter Your Gender (Male/Female): ")
gender=input()

#BMI Formula:
height = height / 100
bmi = weight/(height**2)


    

category = ""
feedback=""
ageCat=0
threshold=0
if age>=19:
    
    def ageCategory(age):
        
        if age>=20 and age<40:
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
                break
    #Output
    print("============================")
    print("Your BMI Information:")
    print("Gender: ",gender,"\nAge: ",age,"\nHeight: ", height*100, "\nWeight: ",weight, "\nBMI:",feedback)
    print("============================")
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=bmi,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': f"BMI: {feedback}", 'font': {'size': 24}},
        #delta={'reference': 25, 'increasing': {'color': "red"}, 'decreasing': {'color': "green"}},
        gauge={
            'axis': {'range': [None, 40], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 18.5], 'color': 'lightblue'},      # Underweight
                {'range': [18.5, 25], 'color': 'lightgreen'},    # Normal
                {'range': [25, 30], 'color': 'yellow'},          # Overweight
                {'range': [30, 40], 'color': 'lightcoral'}       # Obese
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': bmi
            }
        }
    ))
    
    # Update layout for better appearance
    fig.update_layout(
        paper_bgcolor="violet",
        height=400,
        font={'color': "darkblue", 'family': "Arial"}
    )
    
    fig.show()



else:
    print("Your age is less than 19 years old.\nFor better advice, please consult with a medical proffessional.")
    

    

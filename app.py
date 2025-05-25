import joblib
from flask  import Flask, request, app, jsonify, render_template
import pandas as pd
import numpy as np
import json

app=Flask(__name__)

# Here we laod our model and required files.
model=joblib.load(r"C:\Users\ACER\Documents\Downloads\ensemble_model.pkl")
encoder=joblib.load(r"C:\Users\ACER\Documents\Downloads\_disease_Lebel_encoder")

file1=open(r"C:\Users\ACER\Documents\Downloads\precaution_dict.json")
prec_dict=json.load(file1)

file2=open(r"C:\Users\ACER\Documents\Downloads\disease_weight_dict.json")
disease_weight_dict=json.load(file2)

file3=open(r"C:\Users\ACER\Documents\Downloads\desp_dataset_dict.json")
desp_dict=json.load(file3)


all_symptoms=list(disease_weight_dict.keys())



#This will triger our Home.html file.
@app.route('/')
def home():
    print("Home page loaded!")
    return render_template("home.html")


#Here we made a method which is used when our user use the API for sending the input and model predict the output. 
@app.route("/predict_api",methods=['GET','POST'])
def predict_api():
    data=request.json["data"]
    print("Received JSON data:", data)
    if request.method == 'POST':
        print("Form submitted!")
    lst=[]
    for i in data:
        lst.append(disease_weight_dict.get(data[i],0))
        print(lst)
    while len(lst)<17:
        lst.append(0)
        print(lst)
    #data=np.array(lst).reshape(1,-1)
    input_df=pd.DataFrame([lst],
    columns=["Symptom_1","Symptom_2","Symptom_3","Symptom_4","Symptom_5","Symptom_6","Symptom_7","Symptom_8","Symptom_9","Symptom_10","Symptom_11","Symptom_12","Symptom_13","Symptom_14","Symptom_15","Symptom_16","Symptom_17"])
    print(input_df)
    output=model.predict(input_df)[0]
    prediction=encoder.inverse_transform([output])[0]
    description = desp_dict.get(prediction, "No description available.")
    precautions = prec_dict.get(prediction, ["No precautions found"])
    return jsonify({
        "predicted_disease": prediction,
        "description": description,
        "precautions": precautions
    })
    


# Here we made a method for the user which directly give data from the website.   
@app.route("/predict" ,methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        return render_template("predict.html", symptoms=all_symptoms)
    selected_symptoms=[]
    for i in range(1,6):
        symptom=request.form.get(f"symptom{i}")
        if symptom:
            weight=disease_weight_dict.get(symptom,0)
            selected_symptoms.append(weight)
    while len(selected_symptoms)<17:
        selected_symptoms.append(0)
    input_df=pd.DataFrame([selected_symptoms],columns=["Symptom_1","Symptom_2","Symptom_3","Symptom_4","Symptom_5","Symptom_6","Symptom_7","Symptom_8","Symptom_9","Symptom_10","Symptom_11","Symptom_12","Symptom_13","Symptom_14","Symptom_15","Symptom_16","Symptom_17"])
    output=model.predict(input_df)[0]
    disease=encoder.inverse_transform([output])[0]
    precautions = prec_dict.get(disease, ["No precautions found"])
    description = desp_dict.get(disease, "No description available.")
    return render_template("predict.html",
    prediction_text=f"Predicted Disease: {disease}",
    precautions=precautions,
    description=description)
                
if __name__=="__main__":
    app.run(debug=True)
    
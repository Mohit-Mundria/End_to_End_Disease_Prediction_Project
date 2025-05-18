import joblib
from flask  import Flask, request, app, jsonify, url_for, render_template, redirect, flash, session
import pandas as pd
import numpy as np
import json

app=Flask(__name__)
model=joblib.load(r"C:\Users\ACER\Documents\Downloads\ensemble_model.pkl")
encoder=joblib.load(r"C:\Users\ACER\Documents\Downloads\_disease_Lebel_encoder")

file1=open(r"C:\Users\ACER\Documents\Downloads\precaution_dict.json")
prec_dict=json.load(file1)

file2=open(r"C:\Users\ACER\Documents\Downloads\disease_weight_dict.json")
disease_weight_dict=json.load(file2)

file3=open(r"C:\Users\ACER\Documents\Downloads\desp_dataset_dict.json")
desp_dict=json.load(file3)



@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    lst=[]
    for i in dict(data):
        lst.append(disease_weight_dict.get(i))
    while len(data)<=17:
        data.append(0)
    data=np.aarray(list(lst.values())).reshape(1,-1)
    input_df=pd.DataFrame([data],
    columns=["Symptom_1","Symptom_2","Symptom_3","Symptom_4","Symptom_5","Symptom_6","Symptom_7","Symptom_8","Symptom_9","Symptom_10","Symptom_11","Symptom_12","Symptom_13","Symptom_14","Symptom_15","Symptom_16","Symptom_17"])
    
    output=model.predict(input_df)[0]
    prediction=encoder.inverse_transform([output])
    print(f"The predicted Disease is:  {prediction} acoording to the given symptoms.")
    print("Thnx for using this Disease Prediction Project.")
    
    
    if __name__=="__main__":
        main.run(debug=True)
    
    


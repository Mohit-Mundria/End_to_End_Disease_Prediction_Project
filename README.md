# End_to_End_Disease_Prediction_Project
This project is an AI/ML-powered **Disease Prediction Web App** that allows users to input symptoms and receive a prediction of a possible disease along with relevant precautions and descriptions.

It combines **Ensemble Learning** techniques with a lightweight **Flask** backend for model deployment. Users can interact with the model via a simple HTML interface.

---

## 🚀 Features

- 🔬 Predicts diseases based on user-input symptoms.
- 🧠 Uses an ensemble machine learning model trained on symptom-disease datasets.
- 🗂️ Includes:
  - Disease descriptions
  - Suggested precautions
- 🌐 Web interface built with Flask + HTML (template-based)

---

## 📌 Technologies Used

- **Python**
- **Pandas**, **NumPy**
- **Scikit-learn** (for training the ML models)
- **Flask** (for serving the model as an API)
- **Joblib** (for loading trained models)
- **HTML/CSS** (template-based frontend)



**Note:** The HTML/CSS frontend is adapted from open templates and was not created from scratch. My focus was on machine learning and model deployment.

{This project teach me lot of things about logic building of backend. I firstly made a single Index.html but the rendering part give error every time. After lot of try I decide to make two different files, Home.html and predict.html. And from home.html I triger the predict.html, and finally it work.}

**Approach**
1. Collect the data from kaggle.
2. Do Data Preprocessing and train 2 classification algorithms.
3. Use the Ensemble Learning using those algrithms.
4. Make a virtual Environmnet in VS Code for further Project development.
5. Create flask app that control the Backend Logic of the web application and add pipelines.
6. Create html+css files for the frontend.
7. Add procfile to give command to the Render Software.
8. Add Dockerfile and deploy the project on Render.
9. Complete End TO End project.


🙋‍♂️ Author
Mohit Mundria
BCA Student | Aspiring AI/ML Engineer
📧 mundriamohit100@gmail.com
🔗 linkedin.com/in/mohit-mundria-31631a322
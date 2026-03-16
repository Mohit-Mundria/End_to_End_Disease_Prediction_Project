<h1 align="center">
  <br>
  <img src="https://img.icons8.com/nolan/256/heart-health.png" alt="Health Prediction Logo" width="120">
  <br>
  End-to-End AI Disease Prediction web App
  <br>
</h1>

<h4 align="center">A state-of-the-art AI/ML-powered diagnostic tool with a premium glassmorphism UI.</h4>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#technologies-used">Technologies Used</a> •
  <a href="#how-it-works">How it Works</a> •
  <a href="#deployment">Deployment</a> •
  <a href="#author">Author</a>
</p>

## Overview
This project bridges the gap between raw data science and practical application. It allows users to input their symptoms and instantly receive a highly accurate disease prediction. To make the output actionable, the system cross-references medical dictionaries to provide detailed disease descriptions and immediate recommended precautions.

Recently, the frontend was completely overhauled from basic HTML to a visually stunning **Glassmorphism UI**, perfectly suited to showcase the power of the backend ML pipeline to recruiters and users alike. 

## ✨ Features

- 🔬 **Accurate Predictions**: Predicts diseases based on combinations of up to 5 user-input symptoms.
- 🧠 **Ensemble Learning Engine**: Powered by an advanced Ensemble classification algorithm (Adaboost + Random Forest) trained on extensive Kaggle symptom-disease datasets.
- 🗂️ **Actionable Details**: Returns not just a diagnosis, but also simple, understandable descriptions and actionable medical precautions.
- 🎨 **Premium UI/UX**: 
  - Stunning animated landing page detailing the project architecture.
  - Frost-glass style UI components.
  - Responsive layout for desktop and mobile.
- ⚡ **Lightweight & Fast**: Driven by a highly optimized Flask backend API serving real-time inferences from serialized `.pkl` models.

## 📌 Technologies Used

### Machine Learning & Backend
- **Python 3**
- **Pandas & NumPy** (Data processing and array manipulation)
- **Scikit-Learn** (Training the Ensemble Machine Learning models)
- **Joblib** (Model serialization and loading)
- **Flask** (API and Web Server routing)

### Frontend
- **Note** I use the open source template for the frontend, as my main focus was on the machine learning and model/project development and deployment.
- **HTML5 & CSS3** (Vanilla implementation)
- **Vanilla JavaScript** (Interactivity, DOM manipulation, form states)
- **Glassmorphism Architecture** (Modern UI trends via styling variables)

## 🏗️ How It Works (The Approach)

1. **Data Preprocessing**: Sourced comprehensive datasets from Kaggle, cleaned the data, and encoded the arrays for training.
2. **Model Training**: Trained multiple distinct classification models (e.g., Random Forest, Adaboost) and combined their logic using Ensemble Learning for robust accuracy and reduced bias.
3. **Environment Setup**: Established a Python virtual environment to manage dependencies securely.
4. **Flask API Integration**: Wrote `app.py` to handle routing, mapping JSON/Form inputs to NumPy data frames, and processing them through the model predicting logic.
5. **Modern Frontend Integration**: Linked CSS styles and JavaScript to render highly responsive HTML templates, seamlessly fetching and displaying output metrics.

## 🚀 Deployment

This project is fully prepared for containerized deployment (e.g., AWS EC2, Render, Railway). 

It includes:
- `requirements.txt` / `uv.lock` for environments.
- `Procfile` for simple web hosting integration.
- `Dockerfile` for easy container deployment on AWS.

### Running it Locally
1. Clone the repository: `git clone https://github.com/Mohit-Mundria/End_to_End_Disease_Prediction_Project.git`
2. Change into the directory: `cd End_to_End_Disease_Prediction_Project`
3. Install dependencies: `pip install -r requirements.txt` (or use `uv run`)
4. Start the Flask server: `python app.py`
5. Open your browser and navigate to `http://127.0.0.1:5000/`. Let the sleek UI guide you!

## 🙋‍♂️ Author

**Mohit Mundria**  
*BCA Student | Aspiring AI/ML Engineer*

"This project taught me the real-world application of Machine Learning and the fundamental logic of backend development. It allowed me to overcome styling challenges by designing structured, multi-page HTML and integrating diverse endpoints into a unified user experience."

- 📧 [mundriamohit100@gmail.com](mailto:mundriamohit100@gmail.com)
- 🔗 [LinkedIn Profile](https://linkedin.com/in/mohit-mundria-31631a322)
- 💻 [GitHub Repository](https://github.com/Mohit-Mundria/End_to_End_Disease_Prediction_Project.git)

---

<p align="center">
  <b>Disclaimer:</b> This project's predictions are based on machine learning probabilities and should not serve as a substitute for professional medical advice.
</p>
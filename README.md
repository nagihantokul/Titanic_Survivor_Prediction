# 🛳️ Titanic Survival Prediction Model  
A Machine Learning Web App Built with Python, Streamlit & Scikit-Learn  

This project predicts whether a passenger would have survived the *Titanic* disaster using demographic and travel-related features. It uses a trained machine learning model deployed through a lightweight web application (`titanicapp.py`) and packaged with all necessary dependencies.

## 📦 Project Structure
```
titanicapp.py
titanicpickle.pkl
requirements.txt
img.png
titanicimage/
```

## 🧠 Model Overview
- Trained on Kaggle Titanic dataset
- Features: Pclass, Sex, Age, SibSp, Parch, Fare, Embarked
- Preprocessing: cleaning, encoding, scaling
- Model stored as pickle

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run titanicapp.py
```

## 🖥 App Preview
See img.png for UI.

## 📈 Future Improvements
- Add model explainability (SHAP)
- Deploy online
- Add more engineered features

# Fake News Detection Using AI & Machine Learning (with Streamlit Interface)

## 👤 Project By
KOTHAPALLI VENKANNABABU



## 🗂️ Project Description
This project aims to identify and classify news articles as **Real** or **Fake** using machine learning techniques. It includes data preprocessing, feature extraction, model training, evaluation, and deployment via a user-friendly Streamlit web interface.


## 🚀 Features
 Data cleaning and preprocessing
 TF-IDF vectorization of news text
 Logistic Regression classifier
 Model evaluation (accuracy, precision, recall, F1-score)
 Interactive web app built with Streamlit
 User can input news text and get Real/Fake prediction in real time



## 📑 Problem Statement
Fake news spreads quickly online, making it difficult for readers to discern truth from misinformation. The objective of this project is to build an AI-powered system that automatically detects and flags fake news, improving online information reliability.


## ✅ Proposed Solution
**Data Collection**: Kaggle datasets with labeled fake/real news articles.
**Preprocessing**: Clean text, remove noise, stopwords, punctuation.
**Feature Engineering**: TF-IDF vectorization.
 **Model**: Logistic Regression for binary classification.
 **Deployment**: Streamlit web app for easy user interaction.
 **Evaluation**: Accuracy, precision, recall, F1-score.


## 🛠️ Tech Stack
**Language**: Python
**Libraries**:
   pandas, numpy
   scikit-learn
   nltk, re
   joblib
   Streamlit



## 📈 Algorithm Details
 **Model**: Logistic Regression
 **Input**: News text (headline and body)
 **Process**:
   Preprocessing (lowercase, stopwords removal)
   TF-IDF transformation
   Train-test split (80/20)
   Model training and evaluation
**Output**: Real or Fake classification

---

## 🎨 Streamlit App
- User-friendly interface for predictions
- Text input for news content
- Real-time prediction of Real/Fake
- Deployed locally or on cloud (Streamlit Sharing/Heroku)


## 📊 Results
Achieved ~94% accuracy on test data
Confusion matrix and classification report generated
Visualizations for evaluation


## 🌟 Future Scope
Use advanced NLP models like BERT or RoBERTa
Multi-language support
Browser extensions for live checking
Social media stream integration
Continuous model retraining with new data



## 📎 References
Kaggle Dataset: : https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset
GitHub Repository : https://github.com/Venky-43/Fake-News-Detection



## 🙏 Acknowledgements
Thanks to open-source communities and Kaggle for providing datasets that make projects like this possible.

---

## 💻 How to Run
1. Clone the repo
2. Install requirements
    ```
    pip install -r requirements.txt
    ```
3. Run the Streamlit app
    ```
    streamlit run app.py
    ```
4. Enter news text in the app and get the prediction (Real/Fake)

---

## 📬 Contact
For any questions or feedback:  
**venkannababukothapalli3@gmail.com**


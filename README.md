# Twitter Sentiment Analysis ML App

This project is an end-to-end Machine Learning web application that predicts the sentiment of tweets using Natural Language Processing and a trained ML model.

## Features
- Text preprocessing and TF-IDF vectorization
- Logistic Regression model for sentiment classification
- Flask backend for serving predictions
- Simple HTML/CSS frontend

## Tech Stack
- Python
- Flask
- Scikit-learn
- Pandas, NumPy
- HTML, CSS

## Project Structure
App/        → Flask backend & frontend  
Model/      → Trained ML model files  
Notebooks/  → Model training & experimentation  

## How to Run Locally
1. Clone the repository
2. Create and activate virtual environment
3. Install dependencies  
   `pip install -r requirements.txt`
4. Run the Flask app  
   `cd App`  
   `python app.py`
5. Open browser at  
   `http://127.0.0.1:5000`

## Output
The app takes a tweet as input and displays whether the sentiment is Positive or Negative.

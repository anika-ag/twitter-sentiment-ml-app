from flask import Flask, request, render_template
import pickle
import os
app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "Model", "model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "..", "Model", "vectorizer.pkl")

model = pickle.load(open(MODEL_PATH, "rb"))
vectorizer = pickle.load(open(VECTORIZER_PATH, "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        text = request.form["tweet"]

        # Convert text to vector
        vector = vectorizer.transform([text])

        # Predict sentiment
        result = model.predict(vector)[0]

        prediction = "Positive 😊" if result == 1 else "Negative 😞"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# ---------- SPAM DETECTION MODEL ----------
texts = [
    "Win money now",
    "Free recharge offer",
    "Claim your prize today",
    "Hello how are you",
    "Let's meet tomorrow",
    "Are you coming to class"
]

labels = [1, 1, 1, 0, 0, 0]   # 1 = Spam, 0 = Not Spam

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

# ---------- ROUTES ----------
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    data = vectorizer.transform([message])
    prediction = model.predict(data)

    result = "🚫 Spam Message" if prediction[0] == 1 else "✅ Not Spam"
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(debug=True)

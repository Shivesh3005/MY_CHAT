from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)


with open("faqs.json", "r") as f:
    faqs = json.load(f)

def get_response(user_input):
    user_input = user_input.lower()
    for question, answer in faqs.items():
        if question in user_input:
            return answer
    return "Sorry, I don't have info about that. Please ask seniors or faculty."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.json["message"]
    response = get_response(user_input)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)

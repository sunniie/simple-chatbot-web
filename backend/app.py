from flask import Flask, render_template, request, jsonify, send_from_directory
from model.chatbot_model import Chatbot

app = Flask(__name__, template_folder='../frontend')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    chatbot = Chatbot()
    response = chatbot.get_response(user_input)
    return jsonify({"response": response})

@app.route('/<path:path>')
def send_report(path):
    return send_from_directory('../frontend', path)


if __name__ == "__main__":
    app.run(debug=True)
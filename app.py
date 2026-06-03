from flask import Flask, render_template, request
from intelligence import responder

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.form["message"]
    return responder(msg)

if __name__ == "__main__":
    app.run(debug=True)
    
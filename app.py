from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Yo this is completely new, hopefully this is automated! YET AGAIN"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


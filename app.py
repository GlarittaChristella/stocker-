from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Stocker - Cloud Stock Trading Application"

if __name__ == "__main__":
    app.run(debug=True)
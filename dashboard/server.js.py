from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/background")
def background():
    return render_template("./background/background.html")

@app.route("/background-functions")
def background_functions():
    return render_template("./background/backgroundfunctions.html")

if __name__ == "__main__":
    app.run(debug=True)
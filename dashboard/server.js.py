from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/html")
def html_home():
    return render_template("html/html-home.html")

@app.route("/css")
def css_home():
    return render_template("css/css-home.html")


@app.route("/background")
def background():
    return render_template("./css/background/background.html")

@app.route("/background-functions")
def background_functions():
    return render_template("./css/background/backgroundfunctions.html")


@app.route("/display")
def display():
    return render_template("./css/display/display.html")
if __name__ == "__main__":
    app.run(debug=True)
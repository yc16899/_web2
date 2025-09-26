from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/courses")
def courses():
    return render_template("courses.html")

@app.route("/experience")
def experience():
    return render_template("experience.html")

if __name__ == "__main__":
    app.run(debug=True)
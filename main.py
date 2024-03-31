from flask import *


app = Flask(__name__)
@app.route("/")
def index():

    return render_template("index.html")

@app.route("/notebooks")
def notebooks_page():
    return render_template("notebooks.html")

@app.route("/Golovna")
def Golovna_page():
    return render_template("Golovna.html")

@app.route("/Computer")
def Computer_page():
    return render_template("Computer.html")

@app.route("/Mouse")
def Mouse_page():
    return render_template("Mouse.html")

@app.route("/Headphones")
def Headphones_page():
    return render_template("Headphones.html")


app.run(debug=True)
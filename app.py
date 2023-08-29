from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hoi")
def hoimethode():
    return "<p>Totaal iets anders</p>"

@app.route("/optellen/<getal1>")
def hoimethode2(getal1):
    totaal = int(getal1) + int(getal1)
    totaal = str(totaal)
    print("hij doet het")
    return "<p>opgeteld: </p>" + totaal
from flask import Flask, render_template, request
from model import RockVsMine

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("model.html")


@app.route('/home/')
def home():
    return render_template('model.html')


@app.route('/test_model/')
def testModel():
    return render_template('test_model.html')


@app.route('/predict', methods=['POST'])
def predict():
    sng = request.form.get('signals')  # receive signals in the form of string
    if (sng == ""):
        return "Please enter valid signals."
    t1 = tuple(sng.split(","))  # convert signals string to tuple
    t2 = tuple(map(float, t1))  # Now convert string signals to float signals
    result = RockVsMine(t2)
    if (result == 'R'):
        result = "It's a Rock"
    else:
        result = "It's a Mine"
    return result


if __name__ == "__main__":
    app.run(debug=True)

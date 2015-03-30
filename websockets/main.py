__author__ = 'Linus'

from flask import Flask, render_template, request, jsonify
from drawings import drawings

app = Flask("__name__")


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/calc")
def calc():
    if drawings.__len__() != 0:
        print(drawings)
        return jsonify(result=drawings)
    else:
        return jsonify(result="NULL")


@app.route("/add", methods=['POST'])
def add_drawing():
    encoded_drawing = request.data
    drawing = encoded_drawing.decode('UTF-8')
    drawings.append(drawing)
    return drawing


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
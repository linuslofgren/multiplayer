__author__ = 'Linus'

from flask import Flask, render_template, request, jsonify
from datetime import date

app = Flask("__name__")


@app.route("/")
def hello():
    return render_template('index.html', time=date.today())


@app.route("/calc")
def calc():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a+b)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
__author__ = 'Linus'

from flask import Flask, render_template, request, jsonify
from players import add, players

app = Flask("__name__")


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/calc")
def calc():
    add()
    return jsonify(result=[i.serialize() for i in players])


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
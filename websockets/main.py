__author__ = 'Linus'

from flask import Flask, render_template, request, jsonify
from players import add, players
import threading

app = Flask("__name__")


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/calc")
def calc():
    if players.__len__() != 0:
        return jsonify(result=[i.serialize() for i in players])
    else:
        return jsonify(result="None")


@app.route("/add")
def add_player():
    add()
    return jsonify(result=players[-1].serialize())


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def move():
    for i in players:
        i.yPos += 1


set_interval(move, 10)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
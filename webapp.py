from flask import Flask, url_for, render_template, request
import os
app = Flask(__name__)

@app.route("/page1")
def render_main():
    return render_template('page1.html')


@app.route("/page2")
def render_page2():
    return render_template('page2.html')


@app.route("/page3")
def render_page3():
    return render_template('page3.html')


@app.route("/page4")
def render_page4():
    return render_template('page4.html')

if __name__=="__main__":
    app.run(debug=True, port=66666)

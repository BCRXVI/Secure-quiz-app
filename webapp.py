from flask import Flask, url_for, render_template, request
import os
app = Flask(__name__)

@app.route("/")
def render_main():

if __name__=="__main__":
    app.run(debug=True, port=66666)

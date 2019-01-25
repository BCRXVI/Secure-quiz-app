from flask import Flask, url_for, render_template, request

app = Flask(__name__)

if __name__=="__main__":
    app.run(debug=True, port=66666)

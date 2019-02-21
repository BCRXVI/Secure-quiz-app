from flask import Flask, url_for, render_template, request
import os
app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('page1.html')

@app.route("/page1")
def render_page1():
    if(request.form["buildings"] = "burj khalifa"):
        session["question1"] = "correct"
    else:
        session["question1"] = "incorrect"
    return render_template('page2.html')

@app.route("/page2")
def render_page2():
    if(request.form["numbers"] = "33"):
        session["question2"] = "correct"
    else:
        session["question2"] = "incorrect"
    return render_template('page3.html')

@app.route("/page3")
def render_page3():
    if(request.form["capitals"] = "washington d.c."):
        session["question3"] = "correct"
    else:
        session["question3"] = "incorrect"
    return render_template('page4.html')
       
@app.route("/page4")
def render_page4():
    numcorrect == 0
    if(session["question1"] == "correct")
        numcorrect + 1
    else:
        numcorrect + 0
    if(session["question2"] = "correct")
        numcorrect + 1
    else:
        numcorrect + 0
    if(session["question3"] = "correct")
        numcorrect + 1
    else:
        numcorrect + 0
       return render_template("page4.html", numcorrect == numcorrect)

if __name__=="__main__":
    app.run(debug=True, port=66666)

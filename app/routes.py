from app import app
from flask import render_template,url_for,json,request
from app.search import output


@app.route('/')
def dictionary():  

    return render_template("layout.html",title='Dictionary')

@app.route('/', methods=['POST'])
def my_form_post(): 
    text = request.form['word']
    display = output(text)
    return render_template('layout.html',output=display,text=text)




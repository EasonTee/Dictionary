from app import app
from flask import render_template,url_for,redirect,request,abort
from app.form import input_form
from app.match_word import Dictionary


@app.route('/',methods=['GET'])
def dictionary(): 
    form = input_form()
    return render_template("submit_output.html",title='Dictionary',form=form)

meaning = 'Meaning:'


@app.route('/',methods=['POST'])
def match():
    form = input_form()
    dictionary = Dictionary(r'E:\Dictionary\app\static\data.json') 
    
    if form.validate_on_submit():
    	#user input with capital letter
        if dictionary.find_key(form.word.data) == form.word.data.lower():
            output = dictionary.match(dictionary.find_key(form.word.data))
            return render_template("submit_output.html",title='Dictionary',form=form,output=output,meaning=meaning)

    	#user input without capitalize, eg country name 
        elif dictionary.find_key(form.word.data) == form.word.data.capitalize():
            output = dictionary.match(dictionary.find_key(form.word.data))
            reminder = form.word.data.capitalize()+' :Name should be capitalized' 
            return render_template("submit_output.html",title='Dictionary',form=form,output=output,meaning=meaning,reminder=reminder)
    	
        else:
            try:
                test = dictionary.close_match(form.word.data)[0]
                test_2 = dictionary.match(test)
                return redirect(url_for('suggest',form=form.word.data))

            except:
                error = 'This is not an English word. Please try again!'
                return render_template("submit_output.html",title='Dictionary',form=form,error=error)


 

@app.route('/suggest',methods=['GET'])
def suggest():
    try:
        word = request.args.get('form')
        dictionary = Dictionary(r'E:\Dictionary\app\static\data.json') 
        output = dictionary.close_match(word)
        return render_template("radio_button.html",title='Dictionary',word=word,output=output)

    except:
        return abort(404)

@app.route('/suggest',methods=['POST'])
def display():
    word = request.args.get('form')
    dictionary = Dictionary(r'E:\Dictionary\app\static\data.json') 
    output = dictionary.close_match(word) 
    if request.method =='POST':
        if 'press_submit' in request.form:
            suggest= request.form['suggest']
            display = dictionary.match(dictionary.find_key(suggest))
            return render_template("radio_button.html",title='Dictionary',word=word,output=output,display=display)








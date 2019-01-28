from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class input_form(FlaskForm):

    word = StringField('Enter a word',validators=[DataRequired()])
    submit = SubmitField('Submit')



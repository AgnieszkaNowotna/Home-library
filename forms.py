from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField, FileField, SelectField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    release_year = DateField('year', format='%Y', validators=[DataRequired()])
    genre = SelectField('genre', choices = ['Dramat', 'Komedia', 'Obyczajowa', 'Poiweść dystopijna'], coerce=str)
    description = StringField('description')
    readed = BooleanField('readed')
    cover = FileField('Image File')
"""
class CommentForm(FlaskForm):
    comment = StringField('title')
    score = radio
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField,IntegerField, BooleanField, FileField, SelectField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    author = StringField('Autor', validators=[DataRequired()])
    release_year = DateField('Data wydania', format='%Y', validators=[DataRequired()])
    genre = SelectField('Gatunek', choices = ['Dramat', 'Komedia', 'Obyczajowa', 'Poiweść dystopijna'], coerce=str)
    description = StringField('Opis')
    readed = BooleanField('Czy przeczytana')
    cover = FileField('Okładka książki')
    comment = StringField('Komentarz')
    score = IntegerField('Ocena')

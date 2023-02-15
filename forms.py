from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField,IntegerField, BooleanField, FileField, SelectField
from wtforms.validators import DataRequired

choices = ['Dramat', 'Komedia','Krminał', 'Thriller','Biograficzna', 'Historyczna','Romans','Sci-Fi','Fantastyka','Fantasy','Horror','Obyczajowa','Powieść dystopijna']

class BookForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    author = StringField('Autor', validators=[DataRequired()])
    release_year = IntegerField('Data wydania')
    genre = SelectField('Gatunek', choices = choices, coerce=str)
    description = TextAreaField('Opis')
    readed = BooleanField('Czy przeczytana')
    cover = FileField('Okładka książki')
    reviev = TextAreaField('Recenzja')
    score = IntegerField('Ocena')
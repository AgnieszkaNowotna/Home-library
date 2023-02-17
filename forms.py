from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,IntegerField, BooleanField, FileField, SelectField
from wtforms.validators import DataRequired, NumberRange, Optional

choices = ['-','Dramat','Komedia','Krminał','Thriller','Biograficzna', 'Historyczna','Romans','Sci-Fi','Fantastyka','Fantasy','Horror','Obyczajowa','Powieść dystopijna']

class BookForm(FlaskForm):
    title = StringField('Tytuł', validators = [DataRequired(message = "Pole wymagane")])
    author = StringField('Autor', validators = [DataRequired(message = "Pole wymagane")])
    release_year = IntegerField('Data wydania', validators=[Optional(), NumberRange( min = 1000, max = 2023, message = "Podaj liczbę w zakresie od 1000 do 2023")])
    genre = SelectField('Gatunek', choices = choices, coerce = str, validators = [Optional()])
    description = TextAreaField('Opis', default = "-", validators = [Optional()])
    readed = BooleanField('Czy przeczytana', validators = [Optional()])
    cover = FileField('Okładka książki', validators = [Optional()])
    reviev = TextAreaField('Recenzja', default = "-", validators = [Optional()])
    score = IntegerField('Ocena', validators =[Optional(), NumberRange( min = 0, max = 10, message = "Podaj liczbę w zakresie od 0 do 10")])
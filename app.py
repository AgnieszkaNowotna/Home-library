from flask import Flask, request, render_template, redirect, url_for, redirect
from forms import BookForm
from models import book

app = Flask(__name__)
app.config["SECRET_KEY"] = "kdfjkldsfl"

@app.route('/book/')
def home():
    return render_template("book.html", book = book.all())

@app.route('/book/add/', methods = ["GET", "POST"])
def add():
    form = BookForm()
    error=""
    if request.method == 'POST':
        if form.validate_on_submit():
            data = book.image(form, app, (form.data))
            print(data)
            book.create(data)
            book.save_all()
        return redirect(url_for('home'))

    return render_template("add.html", form = form, error = error)

@app.route('/book/reviev/<string:book_title>', methods = ["GET", "POST"])   
def reviev(book_title):
    title = book_title
    book_id = book.get_id(title)
    position = book.get(book_id)
    form = BookForm(data = position)

    if request.method == "POST":
        if form.validate_on_submit():
            book.update(book_id, form.data)
        return redirect(url_for('home'))

    return render_template("reviev.html", form = form,  book_title = book_title)

if __name__ == "__main__":
    app.run(debug = False) 

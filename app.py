from flask import Flask, request, render_template, redirect, url_for, redirect
from forms import BookForm
from models import book

app = Flask(__name__)
app.config["SECRET_KEY"] = "kdfjkldsfl"

@app.route('/book/')
def home():
    return render_template('library.html', book = book.all())

@app.route('/book/add/', methods = ['GET','POST'])
def add():
    form = BookForm()
    error =""
    if request.method == "POST":
        if form.validate_on_submit():
            book.create(form.data)
            book.save_all("books.json")
        return redirect (url_for("home"))
    return render_template("form.html", form=form, error=error)

@app.route('/book/show/')
def show():
    return render_template('library.html', book = book.all())

@app.route('/book/reviev/<book_title>')   
def reviev(book_title):
    book_id = book.get_id(book_title)
    position = book.get(book_id)
    form = BookForm(data = position)

    if request.method == "POST":
        if form.validate_on_submit():
            book.update(book_id, form.data)
        return redirect(url_for("show"))

    return render_template("form.html", form = form, book_id = book_id)

if __name__ == "__main__":
    app.run(debug = False)


from flask import Flask, request, render_template, redirect, url_for, redirect
from forms import BookForm
from models import book

app = Flask(__name__)
app.config["SECRET_KEY"] = "kdfjkldsfl"

@app.route('/book')
def home():
    return render_template("home.html")

@app.route('/book/add/', methods = ['GET','POST'])
def add():
    form = BookForm()
    error =""
    if request.method == "POST":
        if form.validate_on_submit():
            book.create(form.data)
            book.save_all
        return redirect (url_for("home"))
    return render_template("form.html", form=form, error=error)

@app.route('/book/show')
def show():
    return render_template('library.html', book = book.all())

@app.route('/book/comment')
def comment():
    return redirect (url_for("home"))

if __name__ == "__main__":
    app.run(debug = False)


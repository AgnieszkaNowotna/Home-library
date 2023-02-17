from flask import Flask, jsonify, abort, make_response, request
from models import books

app = Flask(__name__)
app.config["SECRET_KEY"] = "kdfjkldsfl"
app.config['JSON_AS_ASCII'] = False

@app.route("/api/v1/books/", methods = ['GET'])
def books_list_api_v1():
    return jsonify(books.all())

@app.route("/api/v1/books/<int:book_id>", methods = ["GET"])
def get_book(book_id):
    book = books.get(book_id)
    if not book:
        abort(404)
    return jsonify({"book":book})

@app.route("/api/v1/books/", methods=['POST'])
def create_book():
    if not request.json or not ('title' and 'author') in request.json:
        abort(400)
    book = {
            'id':len(books.all())+1,
            'title':request.json['title'],
            'author':request.json['author'],
            'release_year':request.json.get('release_year', ""),
            'genre':request.json.get('genre', ""),
            'description':request.json.get('description', ""),
            'readed': False,
            'cover':request.json.get('cover', "brak_okładki.jpg"),
            'reviev':request.json.get('reviev', ""),
            'score':request.json.get('score', ""),
            },
    books.create(book)
    return jsonify({'book':book}),201

@app.route("/api/v1/books/<int:book_id>", methods = ['DELETE'])
def delete_book(book_id):
    result = books.delete(book_id)
    if not result:
        abort(404)
    return jsonify({'result':result})

@app.route("/api/v1/books/<int:book_id>", methods =["PUT"])
def update_book(book_id):
    book = books.get(book_id)
    if not book:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'author' in data and not isinstance(data.get('author'), str),
        'release_year' in data and not isinstance(data.get('release_year'), int),
        'genre' in data and not isinstance(data.get('author'), str),
        'description' in data and not isinstance(data.get('description'), str),
        'readed' in data and not isinstance(data.get('readed'), bool),
        'cover' in data and not isinstance(data.get('cover'), str),
        'reviev' in data and not isinstance(data.get('reviev'), str),
        'score' in data and not isinstance(data.get('release_year'), int),
    ]):
        abort(400)
    book = {
        'id':book_id,
        'title': data.get('title', book['title']),
        'author': data.get('author', book['author']),
        'release_year': data.get('release_year', book['release_year']),
        'genre': data.get('genre', book['genre']),
        'description': data.get('description', book['description']),
        'readed': data.get('readed', book['readed']),
        'cover': data.get('cover', book['cover']),
        'reviev': data.get('reviev', book['reviev']),
        'score': data.get('score', book['score']),
    }
    books.update(book_id, book)
    return jsonify({'book':book})

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error':'Bad request','status_code':400}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found', 'status_code': 404 }), 404)

if __name__ =="__main__":
    app.run(debug=True)
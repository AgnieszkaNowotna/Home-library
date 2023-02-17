import json

class Books:
    def __init__(self):
        try:
            with open ("books.json", "r", encoding = "UTF-8") as f:
                self.library = json.load(f)
        except FileNotFoundError:
            self.library = []

    def all(self):
        return self.library

    def get(self,id):
        book = [book for book in self.all() if book['id'] == id]
        if book:
            return book[0]
        return []
    
    def create(self, data):
        self.library.append(data)
        self.save_all()

    def save_all(self):
        with open("books.json", "w", encoding="UTF-8")as f:
            json.dump(self.library, f, ensure_ascii=False)

    def delete(self, id):
        book = self.get(id)
        if book:
            self.library.remove(book)
            self.save_all()
            return True
        return False    

    def update(self, id, data):
        book = self.get(id)
        if book:
            index = self.library.index(book)
            self.library[index] = data
            self.save_all()
            return True
        return False

books = Books()
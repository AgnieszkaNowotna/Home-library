import json

class Book:
    def __init__(self):
        try:
            with open ("books.json", "r", encoding = "UTF-8") as f:
                self.library = json.load(f)
        except FileNotFoundError:
            self.library = []
    
    def all(self):
        return self.library
    
    def get(self,id):
        return self.library[id]
    
    def create(self, data):
        data.pop('csrf_token')
        self.todos.append(data)

    def save_all(self, filename, collection_name):
        with open(filename, "w", encoding="UTF-8")as f:
            json.dump(collection_name,f, ensure_ascii=False)

    def update(self, id, data):
        data.pop('csrf_token')
        self.todos[id] = data
        self.save_all()

book = Book()

def save_to_json(filename, value):
    with open(filename, "w", encoding="UTF-8")as f:
        json.dump(value,f, ensure_ascii=False)

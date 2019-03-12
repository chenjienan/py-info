from flask import Flask, jsonify, request


app = Flask(__name__)

books = [
    {
        'name': "A",
        'price': 7.99,
        'isbn': 1234
    },
    {
        'name': "B",
        'price': 10.99,
        'isbn': 23432
    },
]

@app.route('/')
def main():
    return 'Hello World!'

@app.route('/books')
def get_books():
    return jsonify(books)

@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book['isbn'] == isbn:
            return_value = {
                'name': book['name'],
                'price': book['price']
            }
    return jsonify(return_value)

@app.route('/books', methods=['POST'])
def add_book():
    return jsonify(request.get_json())

app.run(debug=True)
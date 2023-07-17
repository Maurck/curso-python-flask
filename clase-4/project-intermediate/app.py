from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de libros disponibles
books = [
    {"id": 1, "title": "Libro 1", "author": "Autor 1", "price": 20.50},
    {"id": 2, "title": "Libro 2", "author": "Autor 2", "price": 15.75},
    {"id": 3, "title": "Libro 3", "author": "Autor 3", "price": 12.00}
]

# Carrito de compras
cart = []


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/books')
def book_list():
    return render_template('book_list.html', books=books)


@app.route('/books/<int:book_id>')
def book_details(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return render_template('book_details.html', book=book)
    return "Libro no encontrado."


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    book_id: int = int(request.form['book_id'])
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        cart.append(book)
    return redirect(url_for('book_list'))


@app.route('/cart')
def view_cart():
    return render_template('cart.html', cart=cart)


if __name__ == '__main__':
    app.run(debug=True)
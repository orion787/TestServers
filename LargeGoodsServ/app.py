# server_http_flood.py
from flask import Flask, render_template, jsonify
import random
import time

app = Flask(__name__)

products = [
    {'id': i, 'name': f'Product {i}', 'price': random.randint(100, 1000)} 
    for i in range(1000)
]

@app.route('/')
def index():
    # Имитация сложного рендеринга
    time.sleep(0.1)
    return render_template('ecommerce.html', products=products)

@app.route('/search')
def search():
    # Ресурсоёмкий поиск
    query = request.args.get('q', '')
    results = [p for p in products if query.lower() in p['name'].lower()]
    return render_template('search_results.html', results=results)

@app.route('/product/<int:id>')
def product(id):
    # Генерация сложной страницы
    product = next((p for p in products if p['id'] == id), None)
    if product:
        return render_template('product.html', 
               product=product,
               recommendations=random.sample(products, 12))
    return "Product not found", 404

if __name__ == '__main__':
    app.run(threaded=True)

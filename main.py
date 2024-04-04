from flask import Flask, jsonify, make_response
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

data = {
    '1': {'name': 'Coxinha', 'price': 10.99},
    '2': {'name': 'Torta', 'price': 19.99},
    '3': {'name': 'Biscoito', 'price': 5.99},
}

@app.route('/api/produtos')
@cache.cached(timeout=60)  # Cache válido por 60 segundos
def get_products():
    return jsonify(data)

@app.route('/api/produtos/<id>')
@cache.cached(timeout=60)  # Cache válido por 60 segundos
def get_product(id):
    return jsonify(data.get(id, {}))

@app.route('/api/produtos/public')
def public_cache():
    data = {'message': 'Dados cacheados com public'}
    response = make_response(jsonify(data))
    response.headers['Cache-Control'] = 'public'
    return response

@app.route('/api/produtos/private')
def private_cache():
    data = {'message': 'Dados cacheados com private'}
    response = make_response(jsonify(data))
    response.headers['Cache-Control'] = 'private'
    return response

@app.route('/api/produtos/no-cache')
def no_cache_cache():
    data = {'message': 'Dados cacheados com no-cache'}
    response = make_response(jsonify(data))
    response.headers['Cache-Control'] = 'no-cache'
    return response

@app.route('/api/produtos/no-store')
def no_store_cache():
    data = {'message': 'Dados cacheados com no-store'}
    response = make_response(jsonify(data))
    response.headers['Cache-Control'] = 'no-store'
    return response

@app.route('/api/produtos/max-age')
def max_age_cache():
    data = {'message': 'Dados cacheados com max-age'}
    response = make_response(jsonify(data))
    response.headers['Cache-Control'] = 'max-age=3600'  # Cache válido por 3600 segundos (1 hora)
    return response

if __name__ == '__main__':
    app.run(debug=True)

### Explorando o cache de HTTP em aplicações REST

Neste tutorial, vamos aprender como implementar cache em uma aplicação REST usando Python e Flask. Utilizaremos a extensão Flask-Caching para configurar o cache e demonstraremos como aplicá-lo em rotas específicas para melhorar o desempenho da nossa aplicação.

## 1 - Instalação do Flask

Neste tópico, estamos utilizando o pip, que é o gerenciador de pacotes do Python, para instalar duas bibliotecas necessárias para o nosso projeto: Flask e Flask-Caching. Flask é um framework web em Python, enquanto Flask-Caching é uma extensão que nos permite facilmente adicionar funcionalidades de caching à nossa aplicação.

```
pip install Flask
pip install Flask-Caching
```

## 2 - Configuração do Flask e Flask-Caching

Aqui estamos importando o Flask e Flask-Caching e configurando-os para a nossa aplicação. Estamos utilizando o tipo de cache "simple", que é uma implementação de cache simples em memória. Essa configuração básica nos permite começar a usar o caching em nossa aplicação.

```
from flask import Flask, jsonify
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Dados de exemplo
data = {
    '1': {'name': 'Coxinha', 'price': 10.99},
    '2': {'name': 'Torta', 'price': 19.99},
    '3': {'name': 'Biscoito', 'price': 5.99},
}
```

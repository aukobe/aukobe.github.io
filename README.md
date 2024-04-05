#Integrantes: Augusto Koshiyama Bento e Gabriel Moreira Cabral

# Explorando o cache de HTTP em aplicações REST

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
from flask import Flask, jsonify, make_response
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

data = {
    '1': {'name': 'Coxinha', 'price': 10.99},
    '2': {'name': 'Torta', 'price': 19.99},
    '3': {'name': 'Biscoito', 'price': 5.99},
}
```

## 3 - Definição de Rotas e Funções da API

Neste tópico, estamos definindo as rotas da nossa API e as funções associadas a elas. Temos duas rotas principais: /api/produtos para obter todos os produtos e /api/produtos/<id> para obter um produto específico pelo seu ID. Ambas as rotas estão decoradas com o decorator @cache.cached, indicando que o resultado dessas funções deve ser armazenado em cache por 60 segundos.

```
@app.route('/api/produtos')
@cache.cached(timeout=60)  # Cache válido por 60 segundos
def get_products():
    return jsonify(data)

@app.route('/api/produtos/<id>')
@cache.cached(timeout=60)  # Cache válido por 60 segundos
def get_product(id):
    return jsonify(data.get(id, {}))
```

Comando para executar:

```
curl -i http://localhost:5000/api/produtos
```
```
curl -i http://localhost:5000/api/produtos/1
```
```
curl -i http://localhost:5000/api/produtos/2
```
```
curl -i http://localhost:5000/api/produtos/3
```

## 4 - Utilizando as estratégias de cache

### Public

Com essa estratégia, os recursos podem ser armazenados em cache tanto pelo navegador quanto pelos servidores intermediários. Isso significa que, uma vez que um recurso seja armazenado em cache, ele pode ser reutilizado por outros usuários que solicitarem o mesmo recurso. Essa estratégia é útil para recursos que não contêm informações privadas ou sensíveis e que podem ser compartilhados entre vários usuários.

```
@app.route('/api/produtos/public')
def public_cache():
    data = {'message': 'Dados cacheados com public'}
    response = make_response(jsonify(data))
    response.headers['Cache-Control'] = 'public'
    return response
```

Comando para executar:

```
curl -i http://localhost:5000/api/produtos/public
```

### Private

Com a estratégia private, os recursos podem ser armazenados em cache apenas pelo navegador do usuário e não por servidores intermediários. Isso significa que, embora o navegador possa armazenar em cache o recurso para uso futuro, os servidores intermediários não podem fazer o mesmo. Essa estratégia é útil para recursos que contêm informações privadas ou sensíveis e que não devem ser compartilhadas entre vários usuários.

```
@app.route('/api/produtos/private')
def private_cache():
    data = {'message': 'Dados cacheados com private'}
    response = make_response(jsonify(data))
    response.headers['Cache-Control'] = 'private'
    return response
```

Comando para executar:

```
curl -i http://localhost:5000/api/produtos/private
```

### No-cache

Com essa estratégia, o cache é permitido, mas os recursos precisam ser validados antes de serem reutilizados. Isso significa que, embora o cache possa ser usado para armazenar temporariamente os recursos, o navegador ou servidor intermediário precisa verificar com o servidor de origem se a versão armazenada em cache ainda é válida. Se for, o recurso em cache é utilizado; caso contrário, uma nova versão é solicitada ao servidor de origem.

```
@app.route('/api/produtos/no-cache')
def no_cache_cache():
    data = {'message': 'Dados cacheados com no-cache'}
    response = make_response(jsonify(data))
    response.headers['Cache-Control'] = 'no-cache'
    return response
```

Comando para executar:

```
curl -i http://localhost:5000/api/produtos/no-cache
```

### No-store

Com essa estratégia, o cache é desabilitado completamente. Isso significa que nenhum cache, seja ele em cache do navegador ou cache do servidor intermediário, será utilizado. Cada vez que um recurso é solicitado, ele precisa ser obtido diretamente do servidor de origem, garantindo que sempre tenhamos a versão mais atualizada dos dados.

```
@app.route('/api/produtos/no-store')
def no_store_cache():
    data = {'message': 'Dados cacheados com no-store'}
    response = make_response(jsonify(data))
    response.headers['Cache-Control'] = 'no-store'
    return response
```

Comando para executar:

```
curl -i http://localhost:5000/api/produtos/no-store
```

### Max-age

Com essa estratégia, os recursos podem ser armazenados em cache por um período de tempo específico, determinado pela diretiva max-age no cabeçalho Cache-Control. Isso permite que o recurso seja reutilizado pelo navegador ou servidor intermediário sem precisar verificar com o servidor de origem se a versão armazenada em cache ainda é válida. Se o tempo máximo de idade do cache expirar, o recurso será revalidado com o servidor de origem para garantir que ainda esteja atualizado.

```
@app.route('/api/produtos/max-age')
def max_age_cache():
    data = {'message': 'Dados cacheados com max-age'}
    response = make_response(jsonify(data))
    response.headers['Cache-Control'] = 'max-age=3600'  # Cache válido por 3600 segundos (1 hora)
    return response
```

Comando para executar:

```
curl -i http://localhost:5000/api/produtos/max-age
```

## 5 - Executando a aplicação

Este trecho de código verifica se o script está sendo executado diretamente (não importado como um módulo) e, nesse caso, inicia o servidor Flask com a opção debug=True. Isso permite que a aplicação seja reiniciada automaticamente sempre que houver alterações no código, facilitando o desenvolvimento e depuração.

```
if __name__ == '__main__':
    app.run(debug=True)
```

## Impactos, Benefícios e Limitações do uso de cache

### Impactos

O cache ajuda a reduzir a carga no servidor, diminuindo o número de solicitações e consultas ao banco de dados. Isso pode levar a uma utilização mais eficiente dos recursos do servidor e uma melhor escalabilidade da aplicação.

### Limitações

O cache pode levar à inconsistência dos dados se não for gerenciado corretamente. Se os dados em cache não forem atualizados com frequência suficiente, os usuários podem receber informações desatualizadas, o que pode levar a problemas de integridade e confiabilidade dos dados.

### Benefícios

Uma das maiores vantagens do uso de cache em aplicações REST é a melhoria significativa no desempenho. Ao armazenar em cache recursos frequentemente acessados, reduzimos a necessidade de consultas repetitivas ao servidor, o que resulta em tempos de resposta mais rápidos e uma experiência de usuário mais ágil.

## Contribuições

**Augusto Koshiyama Bento**: leitura dos artigos; auxílio na implementação do código e das rotas dos produtos; criação e composição do tutorial

**Gabriel Moreira Cabral**: implementação do código e das estratégias de cache; auxílio na composição do tutorial.




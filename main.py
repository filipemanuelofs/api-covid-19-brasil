import json
from flask import Flask
app = Flask('app')


NOMENCLATURA_PADRAO = 'covid-19-br.json'


def get_nome_arquivo_historico(data):
    data = data.replace('-', '')
    return NOMENCLATURA_PADRAO.replace('.json', '-' + data + '.json')


def get_dados(dados = 'covid-19-br.json'):
    f = open(dados, 'r')
    return json.loads(f.read())


@app.route('/')
def get_brasil():
    return get_dados()['brasil']


@app.route('/regioes')
def get_por_regioes():
    return get_dados()['regioes']


@app.route('/regioes/<regiao>')
def get_por_estado(regiao):
    dados = get_dados()
    return dados['regioes'][regiao]


@app.route('/historicos/<data>')
def get_por_historicos(data):
    nome_arquivo = get_nome_arquivo_historico(data)
    return get_dados(nome_arquivo)


@app.route('/historicos/<data>/brasil')
def get_por_historico_brasil(data):
    nome_arquivo = get_nome_arquivo_historico(data)
    dados = get_dados(nome_arquivo)
    return dados['brasil']


@app.route('/historicos/<data>/regioes')
def get_por_historico_estados(data):
    nome_arquivo = get_nome_arquivo_historico(data)
    dados = get_dados(nome_arquivo)
    return dados['regioes']




app.run(host='0.0.0.0', port=8080)
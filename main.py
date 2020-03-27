import os
import json
from datetime import datetime
from flask import Flask, jsonify
app = Flask('app')


NOMENCLATURA_PADRAO = 'covid-19-br.json'


def validar_data(data):
    try:
        return datetime.strptime(data, '%Y%m%d')
    except ValueError:
        raise ValueError('Formato da data incorreto, deve ser YYYYMMDD.')


def get_nome_arquivo_historico(data):
    data = data.replace('-', '')
    return './dados/' + NOMENCLATURA_PADRAO.replace('.json', '-' + data + '.json')


def get_dados(dados = './dados/covid-19-br.json'):
    try:
        f = open(dados, 'r')
        return json.loads(f.read())
    except:
        raise Exception('Não foi encontrado nenhum registro com os parâmetros solicitados')


@app.route('/')
def get_brasil():
    try:
        return get_dados()['brasil']
    except Exception as e:
        return jsonify(erro=True, mensagem=str(e))


@app.route('/regioes')
def get_por_regioes():
    try:
        return get_dados()['regioes']
    except Exception as e:
        return jsonify(erro=True, mensagem=str(e))


@app.route('/regioes/<regiao>')
def get_por_estado(regiao):
    try:
        dados = get_dados()
        return dados['regioes'][regiao]
    except Exception as e:
        return jsonify(erro=True, mensagem=str(e))


@app.route('/historicos/<data>')
def get_por_historicos(data):
    try:
        nome_arquivo = get_nome_arquivo_historico(data)
        return get_dados(nome_arquivo)
    except Exception as e:
        return jsonify(erro=True, mensagem=str(e))


@app.route('/historicos/<data>/brasil')
def get_por_historico_brasil(data):
    try:
        nome_arquivo = get_nome_arquivo_historico(data)
        dados = get_dados(nome_arquivo)
        return dados['brasil']
    except Exception as e:
        return jsonify(erro=True, mensagem=str(e))


@app.route('/historicos/<dataInicio>/<dataFim>/brasil')
def get_por_historico_inicio_fim_brasil(dataInicio, dataFim):
    try:
        if validar_data(dataFim) > validar_data(dataInicio):
            nome_arquivo_inicio = get_nome_arquivo_historico(dataInicio)
            dados_inicio = get_dados(nome_arquivo_inicio)
            brasil_inicio = dados_inicio['brasil']

            nome_arquivo_fim = get_nome_arquivo_historico(dataFim)
            dados_fim = get_dados(nome_arquivo_fim)
            brasil_fim = dados_fim['brasil']

            return jsonify(
                confirmados_inicio=brasil_inicio['confirmados'],
                confirmados_fim=brasil_fim['confirmados'],
                qnt_novos_casos=int(brasil_fim['confirmados']) - int(brasil_inicio['confirmados']),
                porcentagem=str(int(int(int(brasil_fim['confirmados']) * 100) / int(brasil_inicio['confirmados']))) + "%"
            )
        else:
            return jsonify(erro=True, mensagem="A data fim deve ser maior que a data início.")
    except Exception as e:
        return jsonify(erro=True, mensagem=str(e))


@app.route('/historicos/<data>/regioes')
def get_por_historico_estados(data):
    try:
        nome_arquivo = get_nome_arquivo_historico(data)
        dados = get_dados(nome_arquivo)
        return dados['regioes']
    except Exception as e:
        return jsonify(erro=True, mensagem=str(e))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
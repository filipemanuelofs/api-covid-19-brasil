import os
import json
from flask import Flask, jsonify, render_template
from util import formatar_data, validar_data


app = Flask('app')
NOMENCLATURA_PADRAO = 'covid-19-br.json'


# -------------------------------------------------------------
# Gráfico Casos confirmados nos estados

def get_regioes_para_grafico_2():
    historicos = get_dados()['regioes']
    for historico in historicos:
        return list(historico)[1:]


def get_confirmados_para_grafico_2():
    historicos = get_dados()['regioes']
    confirmados = []
    for historico in historicos:
        confirmados.append(historico['norte']['total'])
        confirmados.append(historico['nordeste']['total'])
        confirmados.append(historico['sudeste']['total'])
        confirmados.append(historico['centro-oeste']['total'])
        confirmados.append(historico['sul']['total'])
        break
    return confirmados


# -------------------------------------------------------------
# Gráfico Casos confirmados no Brasil

def get_datas_para_grafico_1():
    historicos = get_dados_historicos_arquivo()
    datas = []
    for historico in historicos:
        datas.append(formatar_data(historico['brasil']['atualizado_em']))
    return datas


def get_confirmados_para_grafico_1():
    historicos = get_dados_historicos_arquivo()
    confirmados = []
    for historico in historicos:
        confirmados.append(historico['brasil']['confirmados'])
    return confirmados

# -------------------------------------------------------------


def get_historicos_datas():
    historicos = get_dados_historicos_arquivo()
    datas = []
    for historico in historicos:
        datas.append(formatar_data(historico['brasil']['atualizado_em']))
    return datas


def get_historicos_casos_confirmados():
    historicos = get_dados_historicos_arquivo()
    confirmados = []
    for historico in historicos:
        confirmados.append(historico['brasil']['confirmados'])
    return confirmados


def get_dados_historicos_arquivo():
    historicos = []
    dados_filesystem = os.listdir('./dados/')
    dados_filesystem.sort()
    for dados in dados_filesystem:
        if dados.startswith('covid-19-br-2020'):
            f = open('./dados/' + dados, 'r')
            dados = json.loads(f.read())
            historicos.append(dados)
    return historicos


def get_nome_arquivo_historico(data):
    data = data.replace('-', '')
    return './dados/' + NOMENCLATURA_PADRAO.replace('.json', '-' + data + '.json')


def get_dados(dados='./dados/covid-19-br.json'):
    f = None
    try:
        f = open(dados, 'r')
        return json.loads(f.read())
    except:
        raise Exception(
            'Não foi encontrado nenhum registro com os parâmetros solicitados')
    finally:
        f.close()


def get_casos_confirmados():
    return get_dados()['brasil']['confirmados']


def get_primeiro_caso_confirmado():
    historicos = get_dados_historicos_arquivo()
    for historico in historicos:
        if int(historico['brasil']['confirmados']) == 1:
            return formatar_data(historico['brasil']['atualizado_em'])


def get_informacoes_pior_dia():
    historicos = get_dados_historicos_arquivo()
    historicos.reverse()
    num_confirmados = 0
    num_confirmados_aux = 0
    for index, historico in enumerate(historicos):
        num_confirmados = int(int(
            historico['brasil']['confirmados']) - int(historicos[index+1]['brasil']['confirmados']))
        if num_confirmados > num_confirmados_aux:
            num_confirmados_aux = num_confirmados
        else:
            return formatar_data(historicos[index-2]['brasil']['atualizado_em']), num_confirmados_aux


def get_pior_dia():
    return get_informacoes_pior_dia()[0]


def get_casos_pior_dia():
    return get_informacoes_pior_dia()[1]


def get_obitos_brasil():
    return get_dados()['brasil']['mortes']

# API
# -------------------------------------------------------------


@app.route('/')
def get_index():
    return render_template('index.html',
                           confirmados_brasil=get_casos_confirmados(),
                           primeiro_caso_confirmado=get_primeiro_caso_confirmado(),
                           pior_dia=get_pior_dia(),
                           data_pior_dia=get_informacoes_pior_dia()[0],
                           casos_pior_dia=get_informacoes_pior_dia()[1],
                           obitos_brasil=get_obitos_brasil(),
                           datas_grafico_1=get_datas_para_grafico_1(),
                           confirmados_grafico_1=get_confirmados_para_grafico_1(),
                           regioes_grafico_2=get_regioes_para_grafico_2(),
                           confirmados_grafico_2=get_confirmados_para_grafico_2())


@app.route('/tudo')
def get_todas_informacoes():
    try:
        return get_dados()
    except Exception as e:
        return jsonify(erro=True, mensagem=str(e))


@app.route('/brasil')
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


@app.route('/historicos')
def get_todos_historicos():
    try:
        historicos = get_dados_historicos_arquivo()
        return jsonify(historicos)
    except Exception as e:
        return jsonify(erro=True, mensagem=str(e))


@app.route('/historicos/brasil')
def get_todos_historicos_brasil():
    historicos = []
    f = None
    try:
        for dados in os.listdir('./dados/'):
            if dados.startswith('covid-19-br-'):
                f = open('./dados/' + dados, 'r')
                dados = json.loads(f.read())
                historicos.append(dados['brasil'])
        return jsonify(historicos)
    except Exception as e:
        return jsonify(erro=True, mensagem=str(e))
    finally:
        f.close()


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
                qnt_novos_casos=int(
                    brasil_fim['confirmados']) - int(brasil_inicio['confirmados']),
                porcentagem_novos_casos=str(int(int(
                    int(brasil_fim['confirmados']) * 100) / int(brasil_inicio['confirmados']))) + "%",
                mortes_inicio=brasil_inicio['mortes'],
                mortes_fim=brasil_fim['mortes'],
                qnt_novas_mortes=int(
                    brasil_fim['mortes']) - int(brasil_inicio['mortes']),
                porcentagem_novas_mortes=str(
                    int(int(int(brasil_fim['mortes']) * 100) / int(brasil_inicio['mortes']))) + "%",
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

import os
from flask import Flask, render_template
from dado_atual import DadoAtual
from dado_historico import DadoHistorico

app = Flask('app')


@app.route('/')
def get_index():
    dado_historico = DadoHistorico()
    dado_atual = DadoAtual()
    return render_template('index.html',
                           confirmados_brasil=dado_atual.get_casos_confirmados_brasil(),
                           primeiro_caso_confirmado=dado_historico.get_primeiro_caso_confirmado(),
                           data_pior_dia=dado_historico.get_data_pior_dia(),
                           casos_pior_dia=dado_historico.get_casos_confirmados_pior_dia(),
                           obitos_brasil=dado_atual.get_obitos_brasil(),
                           datas_grafico_1=dado_historico.get_datas(),
                           confirmados_grafico_1=dado_historico.get_confirmados(),
                           regioes_grafico_2=dado_atual.get_regioes(),
                           confirmados_grafico_2=dado_atual.get_casos_confirmados_por_regiao())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

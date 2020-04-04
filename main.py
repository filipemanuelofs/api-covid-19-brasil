import os
import logging
from flask import Flask, render_template
from dado_atual import DadoAtual
from dado_historico import DadoHistorico
from grafico import Grafico

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
                           grafico_acumulado_brasil_periodo=Grafico.CasosAcumuladosBrasil().get_periodo(),
                           grafico_acumulado_brasil_casos=Grafico.CasosAcumuladosBrasil().get_casos(),
                           grafico_acumulado_brasil_obitos=Grafico.CasosAcumuladosBrasil().get_obitos(),
                           grafico_regioes_regioes=Grafico.Regioes().get_regioes(),
                           grafico_regioes_casos=Grafico.Regioes().get_casos(),
                           # Norte
                           grafico_estados_periodo_ac=list(
                               Grafico.Estados().get_confirmados_uf('norte', 'AC').keys()),
                           grafico_estados_casos_ac=list(
                               Grafico.Estados().get_confirmados_uf('norte', 'AC').values()),

                           grafico_estados_periodo_am=list(
                               Grafico.Estados().get_confirmados_uf('norte', 'AM').keys()),
                           grafico_estados_casos_am=list(
                               Grafico.Estados().get_confirmados_uf('norte', 'AM').values()),

                           grafico_estados_periodo_pa=list(
                               Grafico.Estados().get_confirmados_uf('norte', 'PA').keys()),
                           grafico_estados_casos_pa=list(
                               Grafico.Estados().get_confirmados_uf('norte', 'PA').values()),

                           grafico_estados_periodo_ro=list(
                               Grafico.Estados().get_confirmados_uf('norte', 'RO').keys()),
                           grafico_estados_casos_ro=list(
                               Grafico.Estados().get_confirmados_uf('norte', 'RO').values()),

                           grafico_estados_periodo_rr=list(
                               Grafico.Estados().get_confirmados_uf('norte', 'RR').keys()),
                           grafico_estados_casos_rr=list(
                               Grafico.Estados().get_confirmados_uf('norte', 'RR').values()),

                           grafico_estados_periodo_to=list(
                               Grafico.Estados().get_confirmados_uf('norte', 'TO').keys()),
                           grafico_estados_casos_to=list(
                               Grafico.Estados().get_confirmados_uf('norte', 'TO').values()),

                           # Nordeste
                           grafico_estados_periodo_al=list(
                               Grafico.Estados().get_confirmados_uf('nordeste', 'AL').keys()),
                           grafico_estados_casos_al=list(
                               Grafico.Estados().get_confirmados_uf('nordeste', 'AL').values()),

                           grafico_estados_periodo_ba=list(
                               Grafico.Estados().get_confirmados_uf('nordeste', 'BA').keys()),
                           grafico_estados_casos_ba=list(
                               Grafico.Estados().get_confirmados_uf('nordeste', 'BA').values()),

                           grafico_estados_periodo_ce=list(
                               Grafico.Estados().get_confirmados_uf('nordeste', 'CE').keys()),
                           grafico_estados_casos_ce=list(
                               Grafico.Estados().get_confirmados_uf('nordeste', 'CE').values()),

                           grafico_estados_periodo_ma=list(
                               Grafico.Estados().get_confirmados_uf('nordeste', 'MA').keys()),
                           grafico_estados_casos_ma=list(
                               Grafico.Estados().get_confirmados_uf('nordeste', 'MA').values()),

                           grafico_estados_periodo_pb=list(
                               Grafico.Estados().get_confirmados_uf('nordeste', 'PB').keys()),
                           grafico_estados_casos_pb=list(
                               Grafico.Estados().get_confirmados_uf('nordeste', 'PB').values()),

                           grafico_estados_periodo_pe=list(
                               Grafico.Estados().get_confirmados_uf('nordeste', 'PE').keys()),
                           grafico_estados_casos_pe=list(
                               Grafico.Estados().get_confirmados_uf('nordeste', 'PE').values()),

                           grafico_estados_periodo_pi=list(
                               Grafico.Estados().get_confirmados_uf('nordeste', 'PI').keys()),
                           grafico_estados_casos_pi=list(
                               Grafico.Estados().get_confirmados_uf('nordeste', 'PI').values()),

                           grafico_estados_periodo_rn=list(
                               Grafico.Estados().get_confirmados_uf('nordeste', 'RN').keys()),
                           grafico_estados_casos_rn=list(
                               Grafico.Estados().get_confirmados_uf('nordeste', 'RN').values()),

                           grafico_estados_periodo_se=list(
                               Grafico.Estados().get_confirmados_uf('nordeste', 'SE').keys()),
                           grafico_estados_casos_se=list(
                               Grafico.Estados().get_confirmados_uf('nordeste', 'SE').values()),

                           # Sudeste
                           grafico_estados_periodo_es=list(
                               Grafico.Estados().get_confirmados_uf('sudeste', 'ES').keys()),
                           grafico_estados_casos_es=list(
                               Grafico.Estados().get_confirmados_uf('sudeste', 'ES').values()),

                           grafico_estados_periodo_mg=list(
                               Grafico.Estados().get_confirmados_uf('sudeste', 'MG').keys()),
                           grafico_estados_casos_mg=list(
                               Grafico.Estados().get_confirmados_uf('sudeste', 'MG').values()),

                           grafico_estados_periodo_rj=list(
                               Grafico.Estados().get_confirmados_uf('sudeste', 'RJ').keys()),
                           grafico_estados_casos_rj=list(
                               Grafico.Estados().get_confirmados_uf('sudeste', 'RJ').values()),

                           grafico_estados_periodo_sp=list(
                               Grafico.Estados().get_confirmados_uf('sudeste', 'SP').keys()),
                           grafico_estados_casos_sp=list(
                               Grafico.Estados().get_confirmados_uf('sudeste', 'SP').values()),

                           # Centro-Oeste
                           grafico_estados_periodo_df=list(
                               Grafico.Estados().get_confirmados_uf('centro-oeste', 'DF').keys()),
                           grafico_estados_casos_df=list(
                               Grafico.Estados().get_confirmados_uf('centro-oeste', 'DF').values()),

                           grafico_estados_periodo_go=list(
                               Grafico.Estados().get_confirmados_uf('centro-oeste', 'GO').keys()),
                           grafico_estados_casos_go=list(
                               Grafico.Estados().get_confirmados_uf('centro-oeste', 'GO').values()),

                           grafico_estados_periodo_ms=list(
                               Grafico.Estados().get_confirmados_uf('centro-oeste', 'MS').keys()),
                           grafico_estados_casos_ms=list(
                               Grafico.Estados().get_confirmados_uf('centro-oeste', 'MS').values()),

                           grafico_estados_periodo_mt=list(
                               Grafico.Estados().get_confirmados_uf('centro-oeste', 'MT').keys()),
                           grafico_estados_casos_mt=list(
                               Grafico.Estados().get_confirmados_uf('centro-oeste', 'MT').values()),

                           # Sul
                           grafico_estados_periodo_pr=list(
                               Grafico.Estados().get_confirmados_uf('sul', 'PR').keys()),
                           grafico_estados_casos_pr=list(
                               Grafico.Estados().get_confirmados_uf('sul', 'PR').values()),

                           grafico_estados_periodo_sc=list(
                               Grafico.Estados().get_confirmados_uf('sul', 'SC').keys()),
                           grafico_estados_casos_sc=list(
                               Grafico.Estados().get_confirmados_uf('sul', 'SC').values()),

                           grafico_estados_periodo_rs=list(
                               Grafico.Estados().get_confirmados_uf('sul', 'RS').keys()),
                           grafico_estados_casos_rs=list(
                               Grafico.Estados().get_confirmados_uf('sul', 'RS').values()),
                           )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)

from dado_historico import DadoHistorico
from dado_atual import DadoAtual


class Grafico:

    #def __init__(self):
    #    self.historico = DadoHistorico()
    #    self.atual = DadoAtual()

    class CasosAcumuladosBrasil:
        def __init__(self):
            self.historico = DadoHistorico()

        def get_periodo(self):
            return self.historico.get_datas()

        def get_casos(self):
            return self.historico.get_confirmados()

        def get_obitos(self):
            return self.historico.get_obitos()

    class Regioes:
        def __init__(self):
            self.atual = DadoAtual()

        def get_regioes(self):
            return self.atual.get_regioes()

        def get_casos(self):
            return self.atual.get_casos_confirmados_por_regiao()

    class Estados:
        def __init__(self):
            self.historico = DadoHistorico()

        def get_confirmados_uf(self, regiao, uf):
            return self.historico.get_casos_confirmados_uf(regiao, uf)

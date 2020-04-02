from util import formatar_data, formatar_numeral
import os
import json


class DadoHistorico:
    def __init__(self):
        self.dados = self.__get_dados()

    def __get_dados(self):
        '''
        Retorna uma lista em formato json com os dados históricos
        '''
        historicos = []
        stream = None
        dados_filesystem = os.listdir('./dados/')
        dados_filesystem.sort()
        try:
            for dados in dados_filesystem:
                if dados.startswith('covid-19-br-2020'):
                    stream = open('./dados/' + dados, 'r')
                    dados = json.loads(stream.read())
                    historicos.append(dados)
        except:
            raise Exception('Não possível obter os arquivos históricos')
        finally:
            if stream:
                stream.close()
        return historicos

    def get_primeiro_caso_confirmado(self):
        '''
        Retorna a data, no formato dd/MM, do primeiro caso confirmado.
        '''
        for historico in self.dados:
            if int(historico['brasil']['confirmados']) == 1:
                return formatar_data(historico['brasil']['atualizado_em'])

    def get_datas(self):
        '''
        Retorna uma lista com as datas históricas desde o primeiro caso confirmado.
        '''
        datas = []
        for historico in self.dados:
            datas.append(formatar_data(historico['brasil']['atualizado_em']))
        return datas

    def get_confirmados(self):
        '''
        Retorna uma lista de números de casos confirmados desde o primeiro caso.
        '''
        confirmados = []
        for historico in self.dados:
            confirmados.append(historico['brasil']['confirmados'])
        return confirmados

    def __get_informacoes_pior_dia(self):
        '''
        Retorna uma tupla contendo a data, no formato dd/MM, do pior dia e a quantidade de confirmados neste dia.
        '''
        historicos = self.__get_dados()
        # Chamando a função __get_dados() ao invés
        # do self.dados por conta do .reverse() que modifica o estado da lista
        historicos.reverse()
        num_confirmados = 0
        num_confirmados_aux = 0
        data = None
        for index, historico in enumerate(historicos):
            num_confirmados = int(
                historico['brasil']['confirmados']) - int(historicos[index + 1]['brasil']['confirmados'])
            if num_confirmados > num_confirmados_aux:
                num_confirmados_aux = num_confirmados
                data = historico['brasil']['atualizado_em']
            else:
                return formatar_data(data), num_confirmados_aux

    def get_data_pior_dia(self):
        '''
        Retorna a data do pior dia, que é calculada considerando a diferença entre o valor de confirmados do dia atual e do dia anterior.
        '''
        return self.__get_informacoes_pior_dia()[0]

    def get_casos_confirmados_pior_dia(self):
        '''
        Retorna a quantidade de casos confirmados do pior dia, que é calculada considerando a diferença entre o valor de confirmados do dia atual e do dia anterior.
        '''
        return formatar_numeral(self.__get_informacoes_pior_dia()[1])

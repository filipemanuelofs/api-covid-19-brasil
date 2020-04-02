from util import formatar_numeral
import json


class DadoAtual:
    def __init__(self):
        self.dados = self.__get_dados()

    def __get_dados(self, dados='covid-19-br.json'):
        '''
        Retorna um json a partir de um determinado arquivo de dados, se nenhum for passado, o padrão é o arquivo de dados atuais.
        '''
        stream = None
        try:
            stream = open('./dados/' + dados, 'r')
            return json.loads(stream.read())
        except:
            raise Exception(
                'Não foi encontrado nenhum registro com os parâmetros solicitados')
        finally:
            if stream:
                stream.close()

    def get_regioes(self):
        '''
        Retorna uma lista de regiões na ordem: norte, nordeste, sudeste, centro-oeste e sul.
        '''
        historicos = self.dados['regioes']
        for historico in historicos:
            return list(historico)[1:]

    def get_casos_confirmados_por_regiao(self):
        '''
        Retorna uma lista de casos confirmados por região, seguindo a ordem: norte, nordeste, sudeste, centro-oeste e sul.
        '''
        historicos = self.dados['regioes']
        confirmados = []
        for historico in historicos:
            confirmados.append(historico['norte']['total'])
            confirmados.append(historico['nordeste']['total'])
            confirmados.append(historico['sudeste']['total'])
            confirmados.append(historico['centro-oeste']['total'])
            confirmados.append(historico['sul']['total'])
            break
        return confirmados

    def get_casos_confirmados_brasil(self):
        '''
        Retorna o número de casos confirmados no Brasil.
        '''
        return formatar_numeral(self.dados['brasil']['confirmados'])

    def get_obitos_brasil(self):
        '''
        Retorna o número de óbitos no Brasil.
        '''
        return formatar_numeral(self.dados['brasil']['mortes'])

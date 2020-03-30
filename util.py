from datetime import datetime


def formatar_data(data, padrao='%d/%m'):
    return datetime.strptime(data, '%d/%m/%Y %H:%M').strftime(padrao)


def validar_data(data):
    try:
        return datetime.strptime(data, '%Y%m%d')
    except ValueError:
        raise ValueError('Formato da data incorreto, deve ser YYYYMMDD.')

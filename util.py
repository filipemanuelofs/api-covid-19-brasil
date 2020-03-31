from datetime import datetime


def formatar_data(data, padrao='%d/%m'):
    return datetime.strptime(data, '%d/%m/%Y %H:%M').strftime(padrao)


def validar_data(data):
    try:
        return datetime.strptime(data, '%Y%m%d')
    except ValueError:
        raise ValueError('Formato da data incorreto, deve ser YYYYMMDD.')


def formatar_numeral(numero, separador='.'):
    def reverse(string):
        string = "".join(reversed(string))
        return string

    s = reverse(str(numero))
    count = 0
    result = ''
    for char in s:
        count = count + 1
        if count % 3 == 0:
            if len(s) == count:
                result = char + result
            else:
                result = separador + char + result
        else:
            result = char + result
    return result

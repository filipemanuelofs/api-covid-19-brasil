# API COVID-19 Brasil
API para os casos de COVID-19 no Brasil e regiões

## Endereço
Temporariamente em: https://api-covid-19-brasil.herokuapp.com/

## Endpoints
| Requisição | Descrição | Exemplo |
|--|--|--|
| / | retorna os dados gerais do Brasil | -- |
| /regioes | retorna os dados de todas as regiões do Brasil | -- |
| /regioes/**{regiao}** | retorna os dados da região, onde **{regiao}** => "norte", "nordeste", "sudeste", "centro-oeste" ou "sul" | /regioes/nordeste
| /historicos/**{data}** | retorna os dados históricos gerais de uma determinada data, onde **{data}** => formato YYYYMMDD | /historicos/20200321 |
| /historicos/**{data}**/brasil | retorna os dados históricos gerais do Brasil | /historicos/20200321/brasil |
| /historicos/**{data}**/regioes | retorna os dados históricos gerais das regiões | /historicos/20200321/regioes |

## Fonte
Todos os dados/números são obtidos através do site do [Ministério da Saúde](https://saude.gov.br/) por meio das atualizações diárias que estão sendo postadas.

- Do dia [21/03/2020](https://www.saude.gov.br/noticias/agencia-saude/46571-coronavirus-18-mortes-e-1-128-casos-confirmados) em diante, o Ministério da Saúde passou a informar os casos detalhadamente por região e com os números de infectados, porcentagem e consolidação por UF e região, por isso os datas históricas tem o seu início a partir deste dia.

## Execução
- Unix, Linux, Mac, etc.:
````
	$ pip install requirements.txt
	$ export FLASK_APP=main.py
	$ flask run
````
- Windows 
````
	> C:\Python\python.exe -m pip install
	> set FLASK_APP=main.py
	> flask run
````
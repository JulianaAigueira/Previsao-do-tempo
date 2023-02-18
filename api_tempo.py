# link da API https://openweathermap.org/ você tem que se cadastrar no site. Depois de confirmar o seu cadastro vai gerar a sua chave.

import requests

class api_tempo():
    #API_KY = 'c5249d8f1bf7987cf60914bb9fc50fb3'

    def digitar_cidade(self, cidade):
        #cidade = 'duas barras'
        link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid=c5249d8f1bf7987cf60914bb9fc50fb3&lang=pt_br'
        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        descricao = requisicao_dic['weather'][0]['description']
        temperatura = requisicao_dic['main']['temp'] - 273.15
        print(descricao, f'{temperatura}º C')
        pass
# importar o App, Builder (GUI)
# criar o aplicativo
# criar a função build
# criar sub tela

from kivy.app import App
from kivy.lang import Builder
import requests

# mostra para Builder o arquivo que ele vai ter que ler

#criando o aplicativo( sempre dentro de uma class)
GUI = Builder.load_file('hometempo.kv')
class PrevisaoDoTempo(App):
    #criar a função build
    def build(self):
        return GUI
    def mudar_tela(self, id_tela):
        print(id_tela)
        gerenciador_telas = self.root.ids['screen_manager']
        gerenciador_telas.current = id_tela

    def digitar_cidade(self, cidade):
        link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid=c5249d8f1bf7987cf60914bb9fc50fb3&lang=pt_br'
        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        descricao = requisicao_dic['weather'][0]['description']
        temperatura = requisicao_dic['main']['temp'] - 273.15
        resposta = (descricao, f'{temperatura:.2f}º C')
        self.root.ids['resultempo'].ids.label_resultempo.text = f'{resposta[0]}, {resposta[1]}'


PrevisaoDoTempo().run()

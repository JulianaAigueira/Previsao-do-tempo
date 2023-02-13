# importar o App, Builder (GUI)
# criar o aplicativo
# criar a função build

from kivy.app import App
from kivy.lang import Builder

# mostra para Builder o arquivo que ele vai ter que ler

GUI = Builder.load_file('tela_tempo.kv')

#criando o aplicativo( sempre dentro de uma class)
class PrevisaoDoTempo(App):
    #criar a função build
    def build(self):
        return GUI
PrevisaoDoTempo().run()


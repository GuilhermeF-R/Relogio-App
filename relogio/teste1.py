from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.label import Label
from time import strftime
from kivy.clock import Clock
from time import localtime
from plyer import notification
from threading import Thread  # Importe a biblioteca threading
from playsound import playsound  # Importe a biblioteca playsound
from plyer import vibrator
import time


class hora(BoxLayout):
    def __init__(self, **kwargs):
        super(hora, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.hora_label = Label(text='', font_size="60sp", pos_hint={"center_x": .5})
        self.add_widget(self.hora_label)

    def hora(self, *args):
        self.hora_label.text = strftime("%H: %M: %S")
        self.hora_label.color = (52/255, 47/255, 47/255, 0.65)


class RelogioApp(App):
    def build(self):
        # Define o tamanho da janela
        Window.size = (400, 800)

        layout_principal = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Configurar a cor de fundo do layout principal como cinza
        with layout_principal.canvas.before:
            Color (165/255, 165/255, 165/255, 1)  # Cor cinza (valores iguais para R, G e B)
            self.retangulo_fundo = Rectangle(size=(Window.width, Window.height), pos=layout_principal.pos)

        # Atualize o tamanho do Rectangle quando o tamanho do layout_principal mudar
        layout_principal.bind(size=self.atualizar_tamanho_retangulo)

        # Crie uma instância da classe Tela para exibir a hora
        self.tela = hora()
        layout_principal.add_widget(self.tela)

        # Crie um layout horizontal (BoxLayout) para os botões com tamanho mínimo e espaçamento
        layout_botoes_horizontal = BoxLayout(orientation='horizontal', spacing=20, size_hint=(None, None), size=(250, 120), minimum_size=(0, 0))

        # Adicione um botão à esquerda com uma imagem como fundo
        botao_esquerda = Button(
            background_normal='imagens\documento.png',
            size_hint=(None, None),
            size=(100, 100),
            border=(1, 1, 1, 1)
        )
        botao_esquerda.bind(on_press=self.botao_pressionado)

        # Adicione um botão ao centro com uma imagem como fundo (maior tamanho)
        botao_centro = Button(
            background_normal='imagens\clock.png',
            size_hint=(None, None),
            size=(100, 120),
            border=(1, 1, 1, 1)
        )
        botao_centro.bind(on_press=self.botao_alarme)

        # Adicione um botão à direita com uma imagem como fundo
        botao_direita = Button(
            background_normal='imagens\motivação.png',
            size_hint=(None, None),
            size=(100, 100),
            border=(1, 1, 1, 1)
        )
        botao_direita.bind(on_press=self.botao_pressionado)

        # Adicione os botões ao layout horizontal de botões
        layout_botoes_horizontal.add_widget(botao_esquerda)
        layout_botoes_horizontal.add_widget(botao_centro)
        layout_botoes_horizontal.add_widget(botao_direita)

        # Crie um layout vertical para os botões e ajuste a posição horizontal no centro
        layout_botoes_vertical = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), size=(400, 300))
        layout_botoes_vertical.add_widget(layout_botoes_horizontal)
        layout_botoes_vertical.pos_hint = {"center_x": 0.57}

        # Adicione o layout vertical de botões abaixo da hora
        self.tela.add_widget(layout_botoes_vertical)

        Clock.schedule_interval(self.tela.hora, 1)  # Agende a atualização da hora com um intervalo de 1 segundo

        return layout_principal

    def atualizar_tamanho_retangulo(self, instance, value):
        self.retangulo_fundo.size = (Window.width, Window.height)

    def botao_pressionado(self, instance):
        print(f"Botão '{instance.background_normal}' foi pressionado!")
        
    def botao_alarme(self, instance):
        print(f"Botão '{instance.background_normal}' foi pressionado!")

        
        
 # Pergunte a hora ao usuário
    def botao_addalarme(self, instance):
        print(f"Botão '{instance.background_normal}' foi pressionado!")
    
        H = input("Coloque a HORA: ")
        M = input("Coloque o MINUTO: ")

        while True:
            if localtime().tm_hour == int(H) and localtime().tm_min == int(M):
                print("Acorde!")
                try:
                    vibrator.vibrate(10)  # Vibra por 1 segundo
                    time.sleep(1)       # Aguarda 1 segundo para dar tempo de vibrar
                except NotImplementedError:
                    print("A vibração não está disponível neste dispositivo.")
                # Reproduza um som de alarme
                playsound("LemonJuice.mp3")
                notification.notify(
                    title="Alarme",
                    message="Acorde!",
                    timeout=10
                )
                break

if __name__ == '__main__':
    RelogioApp().run()

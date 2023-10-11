from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.label import Label
from time import strftime
from kivy.clock import Clock

class HoraBox(BoxLayout):
    def __init__(self, **kwargs):
        super(HoraBox, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.hora_label = Label(text='', font_size="60sp", pos_hint={"center_x": .5})
        self.add_widget(self.hora_label)

    def atualizar_hora(self, *args):
        self.hora_label.text = strftime("%H: %M: %S")
        self.hora_label.color = (52/255, 47/255, 47/255, 0.65)

class RelogioApp(App):
    def build(self):
        Window.size = (400, 800)

        screen_manager = ScreenManager()

        # Tela principal
        tela_principal = Screen(name='tela_principal')
        layout_principal = BoxLayout(orientation='vertical', spacing=10, padding=10)

        with layout_principal.canvas.before:
            Color(165/255, 165/255, 165/255, 1)
            self.retangulo_fundo = Rectangle(size=(Window.width, Window.height), pos=layout_principal.pos)

        layout_botoes_horizontal = BoxLayout(orientation='horizontal', spacing=20, size_hint=(None, None), size=(250, 120), minimum_size=(0, 0))

        botao_esquerda = Button(
            background_normal='imagens\documento.png',
            size_hint=(None, None),
            size=(100, 100),
            border=(1, 1, 1, 1)
        )
        botao_esquerda.bind(on_press=self.botao_metas)

        botao_centro = Button(
            background_normal='imagens\clock.png',
            size_hint=(None, None),
            size=(100, 120),
            border=(1, 1, 1, 1)
        )
        botao_centro.bind(on_press=self.botao_alarme)

        botao_direita = Button(
            background_normal='imagens\motivação.png',
            size_hint=(None, None),
            size=(100, 100),
            border=(1, 1, 1, 1)
        )
        botao_direita.bind(on_press=self.botao_motivação)

        layout_botoes_horizontal.add_widget(botao_esquerda)
        layout_botoes_horizontal.add_widget(botao_centro)
        layout_botoes_horizontal.add_widget(botao_direita)

        layout_botoes_vertical = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), size=(400, 300))
        layout_botoes_vertical.add_widget(layout_botoes_horizontal)
        layout_botoes_vertical.pos_hint = {"center_x": 0.57}

        self.tela = HoraBox()
        layout_principal.add_widget(self.tela)
        self.tela.add_widget(layout_botoes_vertical)

        Clock.schedule_interval(self.tela.atualizar_hora, 1)

        tela_principal.add_widget(layout_principal)
        screen_manager.add_widget(tela_principal)

        # Tela alarme
        tela_alarme = Screen(name='tela_alarme')
        layout_vazia = BoxLayout(orientation='vertical')
        botao_voltar = Button(text='Voltar para a tela principal')
        botao_voltar.bind(on_release=self.voltar_para_principal)
        layout_vazia.add_widget(Label(text="Janela Vazia"))
        layout_vazia.add_widget(botao_voltar)
        tela_alarme.add_widget(layout_vazia)
        screen_manager.add_widget(tela_alarme)
        
        # Tela meta
        tela_metas = Screen(name='tela_metas')
        layout_metas = BoxLayout(orientation='vertical')
        botao_voltar = Button(text='Voltar para a tela principal')
        botao_voltar.bind(on_release=self.voltar_para_principal)
        layout_metas.add_widget(Label(text="Janela metas"))
        layout_metas.add_widget(botao_voltar)
        tela_metas.add_widget(layout_metas)
        screen_manager.add_widget(tela_metas)
        
        # Tela motivação
        tela_motivação = Screen(name='tela_motivação')
        layout_motivação = BoxLayout(orientation='vertical')
        botao_voltar = Button(text='Voltar para a tela principal')
        botao_voltar.bind(on_release=self.voltar_para_principal)
        layout_motivação.add_widget(Label(text="Janela motivação"))
        layout_motivação.add_widget(botao_voltar)
        tela_motivação.add_widget(layout_motivação)
        screen_manager.add_widget(tela_motivação)

        return screen_manager
    

    def atualizar_tamanho_retangulo(self, instance, value):
        self.retangulo_fundo.size = (Window.width, Window.height)

    def botao_motivação(self, instance):
        print(f"Botão '{instance.background_normal}' foi pressionado!")
        self.root.current = 'tela_motivação'
        
    def botao_metas(self, instance):
        print(f"Botão '{instance.background_normal}' foi pressionado!")  
        self.root.current = 'tela_metas'  

    def botao_alarme(self, instance):
        print(f"Botão '{instance.background_normal}' foi pressionado!")
        self.root.current = 'tela_alarme'

    def voltar_para_principal(self, instance):
        self.root.current = 'tela_principal'

if __name__ == '__main__':
    RelogioApp().run()

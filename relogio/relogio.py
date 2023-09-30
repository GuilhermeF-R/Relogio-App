from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

class RelogioApp(App):
    def build(self):
        # Define o tamanho da janela
        Window.size = (400, 800)

        layout_principal = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Configurar a cor de fundo do layout principal como cinza
        with layout_principal.canvas.before:
            Color(0.7, 0.7, 0.7, 1)  # Cor cinza (valores iguais para R, G e B)
            self.retangulo_fundo = Rectangle(size=(Window.width, Window.height), pos=layout_principal.pos)

        # Atualize o tamanho do Rectangle quando o tamanho do layout_principal mudar
        layout_principal.bind(size=self.atualizar_tamanho_retangulo)

        # Crie um layout horizontal (BoxLayout) para os botões com tamanho mínimo e espaçamento
        layout_botoes = BoxLayout(orientation='horizontal', spacing=20, size_hint=(None, None), size=(250, 120), minimum_size=(0, 0), pos_hint={'x': 0.055, 'y': 0.5})

        # Adicione um botão à esquerda com uma imagem como fundo
        botao_esquerda = Button(
            background_normal='imagens\documento.png',  # Substitua com o nome da sua imagem à esquerda
            size_hint=(None, None),
            size=(100, 100),
            pos_hint={'x': 0.055, 'y': 0.2},
            border=(1, 1, 1, 1)  # Adicione bordas (largura, cor, raio)
        )
        botao_esquerda.bind(on_press=self.botao_pressionado)

        # Adicione um botão ao centro com uma imagem como fundo (maior tamanho)
        botao_centro = Button(
            background_normal='imagens\clock.png',  # Substitua com o nome da sua imagem no centro
            size_hint=(None, None),
            size=(100, 120),
            pos_hint={'x': 0.055, 'y': 0.10},
            border=(1, 1, 1, 1)  # Adicione bordas (largura, cor, raio)
        )
        botao_centro.bind(on_press=self.botao_pressionado)

        # Adicione um botão à direita com uma imagem como fundo
        botao_direita = Button(
            background_normal='imagens\motivação.png',  # Substitua com o nome da sua imagem à direita
            size_hint=(None, None),
            size=(100, 100),
            pos_hint={'x': 0.055, 'y': 0.2},
            border=(1, 1, 1, 1)  # Adicione bordas (largura, cor, raio)
        )
        botao_direita.bind(on_press=self.botao_pressionado)

        # Adicione os botões ao layout horizontal de botões
        layout_botoes.add_widget(botao_esquerda)
        layout_botoes.add_widget(botao_centro)
        layout_botoes.add_widget(botao_direita)

        # Adicione o layout horizontal de botões ao layout principal
        layout_principal.add_widget(layout_botoes)

        return layout_principal

    def atualizar_tamanho_retangulo(self, instance, value):
        self.retangulo_fundo.size = (Window.width, Window.height)

    def botao_pressionado(self, instance):
        print(f"Botão '{instance.background_normal}' foi pressionado!")

if __name__ == '__main__':
    RelogioApp().run()

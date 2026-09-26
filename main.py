from kivy.app import App
from kivy.uix.label import Label

class HelloWorldApp(App):
    def build(self):
        # Returns a Label widget with the Hello World text and a larger font size
        return Label(
            text="Olá mãe!\nDaqui é o Sérginho\na escrever o seu\nprimeiro programa.",
            halign="center",
            valign="middle",
            font_size='32sp'
        )
label.bind(size=label.setter("text_size"))
if __name__ == '__main__':
    HelloWorldApp().run()

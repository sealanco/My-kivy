from kivy.app import App
from kivy.uix.label import Label

class HelloWorldApp(App):
    def build(self):
        # Returns a Label widget with the Hello World text and a larger font size
        return Label(
            text="Hello, World!",
            font_size='32sp'
        )

if __name__ == '__main__':
    HelloWorldApp().run()

from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout

Window.size = (500, 600)


class TranslatorApp(MDApp):
    def build(self):
        layout = MDRelativeLayout(md_bg_color=(173/255, 181/255, 189/255, 1))

        return layout


if __name__ == '__main__':
    TranslatorApp().run()

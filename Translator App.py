from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout

Window.size = (500, 600)


class TranslatorApp(MDApp):
    def build(self):
        layout = MDRelativeLayout(md_bg_color=(173/255, 181/255, 189/255, 1))


        # Add your layout here
        self.titleLabel = Label(text='Translator App', font_name='Arial',                                font_size=30,
                                pos_hint={'center_x': 0.5, 'center_y': 0.9})
        self.textInput = TextInput(hint_text='Enter text to translate',
                                   pos_hint={'center_x': 0.5, 'center_y': 0.8},
                                   size_hint=(0.8, 0.1))
        self.textInput2 = TextInput(hint_text='Translation',
                                   pos_hint={'center_x': 0.5, 'center_y': 0.6},
                                   size_hint=(0.8, 0.1), readonly=True)

        # Add your widgets here
        layout.add_widget(self.titleLabel)
        layout.add_widget(self.textInput)
        layout.add_widget(self.textInput2)


        return layout



if __name__ == '__main__':
    TranslatorApp().run()

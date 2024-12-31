from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from translate import Translator

Window.size = (500, 600)


class TranslatorApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_button2 = None
        self.main_button = None
        self.dropdown2 = None
        self.dropdown1 = None
        self.choice = None
        self.translateButton = None
        self.textInput2 = None
        self.textInput = None
        self.titleLabel = None

    def translate(self, instance):
        text = self.textInput.text
        if text == '':
            self.textInput.text = 'Please enter text to translate'
            self.textInput.background_color = (1, 1, 0, 1)
            return
        else:
            self.textInput.background_color = (1, 1, 1, 1)
            translator = Translator(from_lang=self.main_button.text.lower(),
                                    to_lang=self.main_button2.text.lower())
            translation = translator.translate(text)
            self.textInput2.text = ""
            self.textInput2.text = translation

    def build(self):
        layout = MDRelativeLayout(md_bg_color=(173 / 255, 181 / 255, 189 / 255, 1))

        # Add your layout here
        self.titleLabel = Label(text='Translator App', font_name='Arial', font_size=30,
                                pos_hint={'center_x': 0.5, 'center_y': 0.95})
        self.textInput = TextInput(hint_text='Enter text to translate',
                                   pos_hint={'center_x': 0.5, 'center_y': 0.68},
                                   size_hint=(0.8, 0.22))
        self.textInput2 = TextInput(hint_text='Translation',
                                    pos_hint={'center_x': 0.5, 'center_y': 0.32},
                                    size_hint=(0.8, 0.22), readonly=True)
        self.translateButton = Button(text='Translate', pos_hint={'center_x': 0.5, 'center_y': 0.1},
                                      size_hint=(0.3, 0.1), on_press=self.translate,
                                      background_color=(52 / 255, 58 / 255, 64 / 255, 1))

        self.choice = ['English', 'Spanish', 'French', 'German', 'Italian',
                       'Russian', 'Chinese', 'Japanese', 'Korean', 'Arabic']

        self.dropdown1 = DropDown()
        self.dropdown2 = DropDown()

        for i in self.choice:
            btn = Button(text='%s' % i, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.dropdown1.select(btn.text))
            self.dropdown1.add_widget(btn)

        for i in self.choice:
            btn = Button(text='%s' % i, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.dropdown2.select(btn.text))
            self.dropdown2.add_widget(btn)

        self.main_button = Button(text='Language', size_hint=(0.3, 0.08),
                                  pos_hint={'center_x': 0.5, 'center_y': 0.85})
        self.main_button.bind(on_release=self.dropdown1.open)
        self.dropdown1.bind(on_select=lambda instance, x: setattr(self.main_button, 'text', x))

        self.main_button2 = Button(text='Language', size_hint=(0.3, 0.08),
                                   pos_hint={'center_x': 0.5, 'center_y': 0.48})
        self.main_button2.bind(on_release=self.dropdown2.open)
        self.dropdown2.bind(on_select=lambda instance, x: setattr(self.main_button2, 'text', x))

        # Add your widgets here
        layout.add_widget(self.titleLabel)
        layout.add_widget(self.textInput)
        layout.add_widget(self.textInput2)
        layout.add_widget(self.translateButton)
        layout.add_widget(self.main_button)
        layout.add_widget(self.main_button2)

        return layout


if __name__ == '__main__':
    TranslatorApp().run()

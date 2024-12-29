from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from googletrans import Translator

Window.size = (500, 600)


class TranslatorApp(MDApp):
    def translate(self, instance):
        text = self.textInput.text
        if text == '':
            self.textInput.text = 'Please enter text to translate'
            self.textInput.hint_text_color = (1, 0, 0, 1)
            return
        else:
            translator = Translator()
            text = self.textInput.text
            translation = translator.translate(text, dest='en')
            self.textInput2.text = translation.text


    def build(self):
        layout = MDRelativeLayout(md_bg_color=(173/255, 181/255, 189/255, 1))

        # Add your layout here
        self.titleLabel = Label(text='Translator App', font_name='Arial',                                font_size=30,
                                pos_hint={'center_x': 0.5, 'center_y': 0.95})
        self.textInput = TextInput(hint_text='Enter text to translate',
                                   pos_hint={'center_x': 0.5, 'center_y': 0.65},
                                   size_hint=(0.8, 0.2))
        self.textInput2 = TextInput(hint_text='Translation',
                                   pos_hint={'center_x': 0.5, 'center_y': 0.25},
                                   size_hint=(0.8, 0.2), readonly=True)
        self.translateButton = Button(text='Translate', pos_hint={'center_x': 0.5, 'center_y': 0.45},
                                      size_hint=(0.3, 0.1), on_press=self.translate)

        self.choice = ['English', 'Spanish', 'French', 'German', 'Italian',
                       'Russian', 'Chinese', 'Japanese', 'Korean', 'Arabic']

        self.dropdown1 = DropDown()
        # self.dropdown2 = DropDown()

        for i in self.choice:
            btn = Button(text='%s' % i, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.dropdown1.select(btn.text))
            # btn.bind(on_release=lambda btn: self.dropdown2.select(btn.text))
            self.dropdown1.add_widget(btn)
            # self.dropdown2.add_widget(btn)

        self.main_button = Button(text='Language', size_hint=(0.3, 0.1),
                                  pos_hint={'center_x': 0.5, 'center_y': 0.85})
        self.main_button.bind(on_release=self.dropdown1.open)
        self.dropdown1.bind(on_select=lambda instance, x: setattr(self.main_button, 'text', x))


        # Add your widgets here
        layout.add_widget(self.titleLabel)
        layout.add_widget(self.textInput)
        layout.add_widget(self.textInput2)
        layout.add_widget(self.translateButton)
        layout.add_widget(self.main_button)

        return layout



if __name__ == '__main__':
    TranslatorApp().run()

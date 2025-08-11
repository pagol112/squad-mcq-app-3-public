from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import json

class MCQApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        with open("questions.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        question = data[0]["question"]
        options = data[0]["options"]
        layout.add_widget(Button(text=question, font_size=24))
        for opt in options:
            layout.add_widget(Button(text=opt, font_size=20))
        return layout

MCQApp().run()
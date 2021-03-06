'''
Notes
=====

Simple application for reading/writing notes.

'''

__version__ = '1.0'

import json
from os.path import join, exists
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import ListProperty, StringProperty, \
        NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

class Calculator(Screen):

    data = ListProperty()

    def args_converter(self, row_index, item):
        return {
            'note_index': row_index,
            'note_content': item['content'],
            'note_title': item['title']}

class NoteApp(App):

    def build(self):
        self.notes = Calculator(name='notes')
        # self.load_notes()

        self.transition = SlideTransition(duration=.35)
        root = ScreenManager(transition=self.transition)
        root.add_widget(self.notes)
        return root

if __name__ == '__main__':
    NoteApp().run()

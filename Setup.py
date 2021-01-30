from kivy.app import App

from kivy.uix.label import Label
class DNDMaster(App):

    def build(self):
        return Label(text="Dungeons and Dragons")

DNDMaster().run()
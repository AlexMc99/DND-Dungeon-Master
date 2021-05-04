from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
    MDBoxLayout:
        orientation: "vertical"

    MDToolbar:
        title: "MDToolbar"

    MDLabel:
        text: "Content"
        halign: "center"
'''

class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

Test().run()
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.scatter import Scatter 
from kivy.uix.label import Label 
from kivy.uix.image import Image 
from kivy.uix.widget import Widget 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from TextScanner import parse
from map import Map
import random

LabelBase.register(name='arcade', 
                   fn_regular='ARCADECLASSIC.TTF')

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
#:import C kivy.utils.get_color_from_hex
<ScreenManagement>:
    MenuScreen:
        id: background
        name: 'background'
        
<MenuScreen>:
    FloatLayout:
        orientation: 'vertical'
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: "background.png"
            Rectangle:
                size: self.width, 200
                pos: self.pos[0], self.pos[1] + self.size[1] - 200
                texture: root.cloud_texture
        Label:
            text: 'Dungeons and Dragons' 
            pos: 10, 30
            font_size: 70
            font_name: "arcade"
            bold: True
        Button:
            text: 'P la y'
            font_size: "40sp"
            pos: 330, 100
            background_color: (1, 1, 1, 1) 
            color: (1, 1, 1, 1)  
            size: (20, 20) 
            size_hint: (.2, .15)
            font_name: "arcade"
            on_release: 
                root.manager.current = 'play'
                
        Button:
            text: 'H o w   to   P la y'
            font_size: "15sp"
            color: (1, 1, 1, 1)  
            size: (10, 10) 
            font_name: "arcade"
            pos: 350, 20
            size_hint: (.15, .1)
            on_release: 
                root.manager.current = 'rules'

""")

#class Backgroud(Widget):
 #   pass

#class MainApp(App):
#     def build(self):
 #       Window.clearcolor = kivy.utils.get_color_from_hex('#87CEEB')
  #      return Backgroud()

#MainApp().run()

class ScreenManagement(ScreenManager):
    pass

class MenuScreen(Screen):
    cloud_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cloud_texture = Image(source="cloud2.png").texture
        self.cloud_texture.wrap = 'repeat'
        self.cloud_texture.uvsize = (Window.width / 1000, -1)
    
    def scroll_texture(self, time_passed):
        self.cloud_texture.uvpos = ((self.cloud_texture.uvpos[0] + time_passed/50.0)%Window.width, self.cloud_texture.uvpos[1])
        texture = self.property('cloud_texture')
        texture.dispatch(self)
    pass


from kivy.clock import Clock
class TestApp(App):

    def on_start(self):
        Clock.schedule_interval(self.root.ids.background.scroll_texture, 1/100.)
    def build(self):
        return ScreenManagement()


if __name__ == '__main__':
    TestApp().run()
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.scatter import Scatter 
from kivy.uix.label import Label  
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from TextScanner import parse
from map import Map

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<ScreenManagement>:
    MenuScreen:
        id: name
        name: 'menu'
        
    RulesScreen:
        id: rules
        name: 'rules'

    PlayScreen:
        id: play
        name: 'play'

    MapScreen:
        id: map
        name: 'map'
        
<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'D&D' 
            font_size: 100
        Button:
            text: 'Play'
            font_size: "22sp"
            background_color: (1, 1, 1, 1) 
            color: (1, 1, 1, 1)  
            size: (20, 20) 
            pos: (300, 250)
            size_hint: (1, .2)
            on_release: 
                root.manager.current = 'play'
                
        Button:
            text: 'How to Play'
            font_size: "20sp"
            background_color: (1, 1, 1, 1) 
            color: (1, 1, 1, 1)  
            size: (20, 20) 
            pos: (400, 350)
            size_hint: (1, .2)
            on_release: 
                root.manager.current = 'rules'

<RulesScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'How To Play'
        Button:
            text: 'Back to menu'
            background_color: (1, 1, 1, 1) 
            color: (1, 1, 1, 1)  
            size: (32, 32) 
            size_hint: (1, .2)
            on_press: root.manager.current = 'menu'

<PlayScreen>:
    last_name_text_input: last_name
    BoxLayout: 
        orientation: 'vertical'
        TextInput:
            id: last_name
            font_size: 50
            size_hint_y: None
            multiline: False
            height: 100
            hint_text: 'Enter Command'
            on_text_validate: root.submit_input()

        Button:
            text: 'View Map'
            background_color: (1, 1, 1, 1) 
            color: (1, 1, 1, 1)  
            size: (32, 32) 
            size_hint: (1, .2)
            on_press: root.manager.current = 'map'

<MapScreen>:
    on_pre_enter: root.map()
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Back'
            width: 100
            allow_stretch: True
            size_hint_y: None
            on_press: root.manager.current = 'play'
        Image:
            id: map
            source: "latestMap.png"
            size: root.size

        
          
""")

class MenuScreen(Screen):
    pass

class PlayScreen(Screen):
    last_name_text_input = ObjectProperty()
    ego = NumericProperty(0)
    userInput = StringProperty('')

    def submit_input(self):
        self.userInput = self.last_name_text_input.text
        print("Assign surname: {}".format(self.userInput))
        self.save()
        self.userInput = ''
        self.load()
        value = parse(self.userInput)
        if(value == 'NORTH' or value == 'SOUTH' or value == 'EAST' or value == 'WEST'):
            Map.getLocation(value)

    def save(self):
        with open("surname.txt", "w") as fobj:
            fobj.write(str(self.userInput))

    def load(self):
        with open("surname.txt") as fobj:
            for userInput in fobj:
                self.userInput = userInput.rstrip()


class RulesScreen(Screen):
    def func_abc(self, instance):
        print(f"func_abc: Called from Button with text={instance.text}")

    def func_xyz(self, instance):
        print(f"func_xyz: Called from Button with text={instance.text}")


class MapScreen(Screen):
    def map(self):
        Map.map()
        self.ids.map.reload()


# Create the screen manager
class ScreenManagement(ScreenManager):
    pass


class TestApp(App):

    def build(self):
        return ScreenManagement()


if __name__ == '__main__':
    TestApp().run()
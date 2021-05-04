from kivy.app import App
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.scatter import Scatter 
from kivy.uix.label import Label  
from kivy.uix.image import Image 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.scrollview import ScrollView
from ParserTest import parse1
from map import Map
import random
import kivymd
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.screen import Screen

import Story
LabelBase.register(name='arcade', 
                   fn_regular='Connectioniii-Rj3W.otf')

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<ScreenManagement>:
    MenuScreen:
        id: background
        name: 'background'
        
    RulesScreen:
        id: rules
        name: 'rules'

    PlayScreen:
        id: play
        name: 'play'

    MapScreen:
        id: map
        name: 'map'

    DiceScreen:
        id: dice
        name: 'dice'
        
<RoundedPlayButton@Button>:
    background_color:(0,0,0,0)
    background_normal: ''
    canvas.before:
        Color: 
            rgba: (0,0,0,0)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [24]
<RoundedHowButton@Button>:
    background_color:(0,0,0,0)
    background_normal: ''
    canvas.before:
        Color: 
            rgba: (0,0,0,0)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [15]

<ScrollableLabel>:
    text: ''
    Label:
        text: root.text
        font_size: 80
        text_size: self.width, None
        size_hint_y: None
        height: self.texture_size[1]

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
            font_size: 65
            font_name: "arcade"
            bold: True

        RoundedPlayButton:
            text: 'p la y'
            font_size: "60sp"
            pos: 330, 100
            color: (1, 1, 1, 1)  
            size: (20, 20) 
            size_hint: (.2, .15)
            font_name: "arcade"
            bold: True
            on_release: 
                root.manager.current = 'play'
                
        RoundedHowButton:
            text: 'How to Play'
            font_size: "30sp"
            color: (1, 1, 1, 1)  
            size: (10, 10) 
            font_name: "arcade"
            pos: 350, 20
            size_hint: (.15, .1)
            bold: True
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
            on_press: root.manager.current = 'background'

<PlayScreen>:
    last_name_text_input: last_name
    on_pre_enter: root.focusInput()
    FloatLayout:
        #canvas.before:
         #   Rectangle:
           #     id: map
          #      pos: 0, 100
            #    size: 800, 500
             #   source: "play3.jpeg"
        Label:
            id: stats
            text: '{}              HP'.format(root.hp)
            height: self.texture_size[1]
            font_size: "30sp"
            size: (32, 32) 
            pos: 0, 500
            size_hint: (1, .2)
            background_color: (0, 0, 0, 0) 
            font_name: "arcade"
        ScrollView:
            Label:
                id: output
                text: root.message
                text_size: self.width, 650
                height: self.texture_size[0]
                size_hint_y: .2
                font_name: "arcade"
                valign: 'bottom'

        MDTextField:
            id: last_name
            font_size: 50
            size_hint_y: None
            multiline: False
            focus: True
            mode: "fill"
            fill_color: 0, 0, 0, .4
            hint_text: 'Press Enter to Continue'
            on_text_validate: root.submit_input()
            text_validate_unfocus: False

        MDIconButton:
            icon: "dots-horizontal"
            pos_hint: {"center_x": .95, "center_y": .08}
            user_font_size: "40sp"
            on_press: 
                root.manager.current = 'map'
        #Button:
         #   text: 'View Map'
          #  background_color: (1, 1, 1, 1) 
           # color: (1, 1, 1, 1)  
            #size: (10, 10) 
            #size_hint: (.5, .2)
            #pos: 0, 500
            #on_press: root.manager.current = 'map'

<MapScreen>:
    on_pre_enter: root.map()
    MDFloatLayout:
        orientation: 'vertical'
        Image:
            id: map
            source: "latestMap.png"
            allow_stretch: True
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint_x: 0.88
            size_hint_y: 0.88
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": .04, "center_y": .95}
            user_font_size: "55sp"
            on_press: 
                root.manager.current = 'play'
          
<DiceScreen>:
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: .76, .76, .76, .76
            Rectangle:
                pos: self.pos
                size: self.size

        Button:
            id: diceroll
            background_normal: 'Dice/side_1.png' 
            background_down: 'Dice/side_2.png'
            on_press: root.roll()

""")

global num
global gMessage

def randomNum():
    global num
    try: 
        return num
    except NameError:
        num = random.randint(1,20)
        return num
    

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

class PlayScreen(Screen):
    global gMessage 
    gMessage = Story.introduction()
    last_name_text_input = ObjectProperty()
    ego = NumericProperty(0)
    userInput = StringProperty('')
    messageCount = 0
    message = Story.introduction()
    hp = 100
    strength = 0
    isAttack = False
    dropdown = ObjectProperty()
    #self.dropdown = MDDropdownMenu()
    #self.dropdown.items.append(
     #   {"viewclass": "MDMenuItem",
      #   "text": "View Map",
       # "callback": root.manager.current = 'map'}
    #)

    def focusInput(self):
        self.ids.last_name.focus = True

    def submit_input(self):
        global gMessage
        self.userInput = self.last_name_text_input.text
        self.last_name_text_input.text = ''
        self.ids.last_name.focus = True
        self.save()
        self.userInput = ''
        self.load()
        self.message = gMessage
        self.message += self.userInput.ljust(400, " ")
        
        print(self.messageCount)
        if (self.messageCount == 0):
            self.message += Story.room3_intro()
            self.messageCount = 1
        elif (self.messageCount == 1):
            if(self.userInput == 'Yes' or self.userInput == 'yes'):
                self.message += Story.room3_yes()
                Map.getLocation('EAST')
                self.messageCount = 2
            elif(self.userInput == 'No' or self.userInput == 'no'):
                self.message += Story.room3_no()
                Map.getLocation('EAST')
                self.messageCount = 2
            else:
                self.message += 'Please enter either yes or no'
                self.message += Story.room3_intro()
        elif (self.messageCount == 2):
            self.message += Story.room4_intro()
            self.messageCount = 3
        elif(self.messageCount == 3):
            print(self.userInput)
            value = parse1(self.userInput)
            print(value)
            if(value == 'ATTACK'):
                self.message += Story.room4_attack()
                self.messageCount = 4
                self.isAttack = True
            elif(value == 'SNEAK'):
                self.message += Story.room4_sneak()
                self.messageCount = 4
            else:
                self.message += 'That is an odd choice. You should probably attack or sneak around them '
        elif(self.messageCount == 4):
            self.manager.current = 'dice'
            num = randomNum()
            self.messageCount = 5
            if(self.isAttack == True):
                self.attack(num)
            else:
                self.peek(num)
        elif(self.messageCount == 5):
            print(self.userInput)
            value = parse1(self.userInput)
            print("The value is:")
            print(value)
            self.messageCount == 6
            if(value == 'NORTH' or value == 'SOUTH' or value == 'EAST' or value == 'WEST'):
                Map.getLocation(value)
        elif(self.messageCount == 6):
            if explore:
                self.message += Story.room4_explore
            else:
                self.message += Story.room4_next()
            self.messageCount = 7
        elif(self.messageCount == 7):
            self.message += room2_intro()
            self.messageCount = 8
        elif(self.messageCount == 8):
            self.message += room2_attack()
            self.messageCount = 9
        elif(self.message == 9):
            self.message += room2_attack_success()
            self.messageCount = 10
        
        self.ids.last_name.focus = True
        self.ids.output.text = self.message
        gMessage = self.message
        self.ids.last_name.focus = True
        self.userInput = ''
        self.focusInput()

    def attack(self, num):
        if(num > 15):
            self.message += Story.room4_attack_success()
        else:
            self.message += Story.room4_attack_fail()
            self.hp = self.hp - 10
            self.ids.stats.text = '{}              HP'.format(self.hp)

    def peek(self, num):
        if(num > 10):
            self.message += Story.room4_sneak_success()
        else:
            self.message += Story.room4_sneak_fail()
            self.hp = self.hp - 10
            self.ids.stats.text = '{}              HP'.format(self.hp)

    def update_input(self, newlines):
        for x in (newlines + 1): 
            self.input_message += '\n'


    def save(self):
        with open("surname.txt", "w") as fobj:
            fobj.write(str(self.userInput))

    def load(self):
        with open("surname.txt") as fobj:
            for userInput in fobj:
                self.userInput = userInput.rstrip()
    
    def on_icon_right(self, instance, value):
        self.dropdown.open(root)


class RulesScreen(Screen):
    def func_abc(self, instance):
        print(f"func_abc: Called from Button with text={instance.text}")

    def func_xyz(self, instance):
        print(f"func_xyz: Called from Button with text={instance.text}")


class MapScreen(Screen):
    def map(self):
        Map.map()
        self.ids.map.reload()

class DiceScreen(Screen):
    click = 0
    def roll(self):
        if (self.click == 0):
            num = randomNum()
            self.ids.diceroll.background_normal = f"Dice/side_{num}.png"
            self.click = 1
        else:
            self.manager.current = 'play'

# Create the screen manager
class ScreenManagement(ScreenManager):
    pass

class TestApp(MDApp):
    def on_start(self):
        Clock.schedule_interval(self.root.ids.background.scroll_texture, 1/100.)
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return ScreenManagement(transition = NoTransition())


if __name__ == '__main__':
    TestApp().run()
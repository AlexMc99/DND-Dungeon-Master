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
from kivy.lang import Builder
from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from ParserTest import parse1
from map import Map
import random
from random import seed
from datetime import datetime
import kivymd
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.screen import Screen

import game
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
        MDToolbar:
            id:toolbar
            title: 'How To Play'
            left_action_items: [["arrow-left", lambda x: root.home(x),"Go Back to Main Menu"]]
            pos: 0, 540
            anchor_title: "center"
        Label:
            text: "Just keep hitting enter until the game asks you a question. When that happens just answer the question."

<PlayScreen>:
    last_name_text_input: last_name
    on_pre_enter: root.focusInput()
    FloatLayout:
        canvas.before:
            Rectangle:
                id: map
                pos: 0, 100
                size: 800, 500
                source: "play4.jpeg"
        ScrollView:
            pos_hint: {'top': 1.0 - toolbar.height / self.parent.height}
            Label:
                id: output
                text: root.message
                text_size: self.width, 650
                height: self.texture_size[0]
                size_hint_y: .2
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
            color_mode: "accent"

        MDToolbar:
            id:toolbar
            title: 'HP:  {}     Strength:  {}     Intelligence:  {}'.format(root.hp, root.strength, root.intelligence)
            left_action_items: [["arrow-left", lambda x: root.home(x),"Go Back to Main Menu"]]
            right_action_items: [["map-search-outline", lambda x: root.map(x), "View Map"], ["help-circle", lambda x: root.rules(x), "Help"]]
            pos: 0, 540
            anchor_title: "center"

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

def randomNum(isRoll):
    global num
    if(isRoll == True):
        dt = datetime.today()
        random.seed(dt.timestamp())
        num = random.randint(1,20)
        return num
    else:
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
    dropdownMenu = ObjectProperty(None)
    global gMessage 
    gMessage = game.introduction()
    last_name_text_input = ObjectProperty()
    ego = NumericProperty(0)
    userInput = StringProperty('')
    messageCount = 0
    message = game.introduction()
    hp = 100
    strength = 0
    intelligence = 0
    isAttack = False
    totalDamage = 0
    checkBody = False

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
        self.message += self.userInput.rjust((190 - len(self.userInput)), " ")
        
        print(self.messageCount)
        if (self.messageCount == 0):
            self.message += game.room3_intro()
            self.messageCount = 1
        elif (self.messageCount == 1):
            Map.getLocation('EAST')
            self.message += game.room3_interact(self.userInput)
            if(self.userInput == "Yes" or self.userInput == 'yes'):
                self.intelligence += 10
                self.ids.toolbar.title = 'HP:  {}     Strength:  {}     Intelligence:  {}'.format(self.hp, self.strength, self.intelligence)
            self.messageCount = 2
        elif (self.messageCount == 2):
            self.message += game.room4_intro()
            self.messageCount = 3
            self.strength += 10
            self.ids.toolbar.title = 'HP:  {}     Strength:  {}     Intelligence:  {}'.format(self.hp, self.strength, self.intelligence)
        elif(self.messageCount == 3):
            value = parse1(self.userInput)
            self.message += game.room4_interact(value)
            self.messageCount = 4
            if(value != 'SNEAK'):
                self.isAttack = True
        elif(self.messageCount == 4):
            seed(1)
            self.manager.current = 'dice'
            num = randomNum(True)
            self.totalDamage += num
            print(self.totalDamage)
            if(self.isAttack == True):            
                self.message += game.room4_attack(self.totalDamage, self.strength)
                if(game.room4_attack_bool(self.totalDamage, self.strength) == True):
                    self.messageCount = 5
                else:
                    self.hp -= 5
                    self.ids.toolbar.title = 'HP:  {}     Strength:  {}     Intelligence:  {}'.format(self.hp, self.strength, self.intelligence)
            else:
                self.message += game.room4_sneak(self.totalDamage, self.intelligence)
                if(game.room4_sneak_bool(self.totalDamage, self.intelligence) == True):
                    self.messageCount = 5
                else:
                    self.isAttack = True
                    self.hp -= 5
                    self.ids.toolbar.title = 'HP:  {}     Strength:  {}     Intelligence:  {}'.format(self.hp, self.strength, self.intelligence)
        elif(self.messageCount == 5):
            self.totalDamage = 0
            self.isAttack == False
            self.message += game.room4_success(self.userInput)
            if'body' in self.userInput:
                checkBody = True
                self.hp += 10
                self.ids.toolbar.title = 'HP:  {}     Strength:  {}     Intelligence:  {}'.format(self.hp, self.strength, self.intelligence)
            if 'leave' in self.userInput:
                self.messageCount = 6
        elif(self.messageCount == 6):
            checkBody = False
            self.message += game.room_move()
            self.messageCount = 7
        elif(self.messageCount == 7):
            value = parse1(self.userInput)
            if (value == 'NORTH'):
                self.messageCount = 8
                Map.getLocation(value)
            self.message += game.room4_go_north(value)
        elif(self.messageCount == 8):
            self.message += game.room2_intro()
            self.messageCount = 9
            self.strength += 10
            self.ids.toolbar.title = 'HP:  {}     Strength:  {}     Intelligence:  {}'.format(self.hp, self.strength, self.intelligence)
        elif(self.messageCount == 9):
            value = parse1(self.userInput)
            self.message += game.room2_interact(value)
            self.messageCount = 10
            if(value != 'SNEAK'):
                self.isAttack = True
        elif(self.messageCount == 10):
            self.manager.current = 'dice'
            num = randomNum(True)
            self.totalDamage += num
            if(self.isAttack == True):            
                self.message += game.room2_attack(self.totalDamage, self.strength)
                if(game.room4_attack_bool(self.totalDamage, self.strength) == True):
                    self.messageCount = 11
                else:
                    self.hp -= 5
                    self.ids.toolbar.title = 'HP:  {}     Strength:  {}     Intelligence:  {}'.format(self.hp, self.strength, self.intelligence)
            else:
                self.message += game.room2_sneak(self.totalDamage, self.intelligence)
                if(game.room4_sneak_bool(self.totalDamage, self.intelligence) == True):
                    self.messageCount = 11
                else:
                    self.isAttack = True
                    self.hp -= 5
                    self.ids.toolbar.title = 'HP:  {}     Strength:  {}     Intelligence:  {}'.format(self.hp, self.strength, self.intelligence)
        elif(self.messageCount == 11):
            self.totalDamage = 0
            self.isAttack == False
            self.message += game.room2_success(self.userInput)
            if'body' in self.userInput:
                checkBody = True
                self.strength += 10
                self.hp += 10
                self.ids.toolbar.title = 'HP:  {}     Strength:  {}     Intelligence:  {}'.format(self.hp, self.strength, self.intelligence)
            if'leave' in self.userInput:
                self.messageCount = 12
        elif(self.messageCount == 12):
            self.message += game.room_move()
            self.messageCount = 13
        elif(self.messageCount == 13):
            value = parse1(self.userInput)
            if (value == 'NORTH'):
                self.messageCount = 14
                Map.getLocation(value)
            self.message += game.room2_move(value)
        elif(self.messageCount == 14):
            self.message += game.room1_intro()
            self.messageCount = 15
        elif (self.messageCount == 15):
            self.message += game.room1_interact(self.userInput)
            if(self.userInput == 'Yes' or 'yes'):
                self.hp -= 15
                self.ids.toolbar.title = 'HP:  {}     Strength:  {}     Intelligence:  {}'.format(self.hp, self.strength, self.intelligence)
            self.messageCount = 16
        elif(self.messageCount == 16):
            self.message += '   This is the end of the demo...'
            self.messageCount = 16

        self.ids.last_name.focus = True
        self.ids.output.text = self.message
        gMessage = self.message
        self.ids.last_name.focus = True
        self.userInput = ''
        self.focusInput()

    def save(self):
        with open("surname.txt", "w") as fobj:
            fobj.write(str(self.userInput))

    def load(self):
        with open("surname.txt") as fobj:
            for userInput in fobj:
                self.userInput = userInput.rstrip()
    def map(self, x):
        self.manager.current = 'map'
    def rules(self, x):
        self.manager.current = 'rules'
    def home(self, x):
        self.manager.current = 'background'


class RulesScreen(Screen):
    def home(self, x):
        self.manager.current = 'play'

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
            num = randomNum(False)
            self.ids.diceroll.background_normal = f"Dice/side_{num}.png"
            self.click = 1
        else:
            self.click = 0
            self.ids.diceroll.background_normal = f"Dice/side_1.png"
            self.manager.current = 'play'

# Create the screen manager
class ScreenManagement(ScreenManager):
    pass

class TestApp(MDApp):
    def on_start(self):
        Clock.schedule_interval(self.root.ids.background.scroll_texture, 1/100.)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Brown"
        self.theme_cls.primary_hue = "900"
        self.theme_cls.accent_palette = "Green"
        self.theme_cls.accent_hue = "50"
        return ScreenManagement(transition = NoTransition())

if __name__ == '__main__':
    TestApp().run()
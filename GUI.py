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
import random

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

    DiceScreen:
        id: dice
        name: 'dice'
        
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
    on_pre_enter: root.focusInput()
    BoxLayout: 
        orientation: 'vertical'
        Label:
            id: output
            text: root.message
            text_size: self.width, None
            height: self.texture_size[1]

        TextInput:
            id: last_name
            font_size: 50
            size_hint_y: None
            multiline: False
            focus: True
            height: 100
            hint_text: 'Press Enter to Continue'
            on_text_validate: root.submit_input()
            text_validate_unfocus: False

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
          
<DiceScreen>:
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
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

def randomNum():
    global num
    try: 
        return num
    except NameError:
        num = random.randint(1,20)
        return num
    

class MenuScreen(Screen):
    pass

class PlayScreen(Screen):
    last_name_text_input = ObjectProperty()
    ego = NumericProperty(0)
    userInput = StringProperty('')
    messageCount = 0
    message = ('It has been a long journey, but it will pay off soon. Do you remember what happened? ...')

    def focusInput(self):
        self.ids.last_name.focus = True

    def submit_input(self):
        self.userInput = self.last_name_text_input.text
        self.last_name_text_input.text = ''
        self.ids.last_name.focus = True
        #print("Assign surname: {}".format(self.userInput))
        self.save()
        self.userInput = ''
        self.load()
        if (self.messageCount == 0):
            self.message = 'Your brother was kidnapped by the King of Trolls during an invasion on your homeland, the Kingdom of Glott. Cattle was killed, homes were burned, and innocent lives were lost in the slaughter. Your brother, King Consort Hannibal, married to Queen Regnant Demetria, was kidnapped during the invasion.' 
            self.messageCount = 1
        elif (self.messageCount == 1):
            self.message = 'You have been venturing through the marshy, barbaric Land of Boog in hopes of finding your brother. It has been exhausting. You’ve been ambushed, beaten, and gone so far as nearly losing your own life. But it has all been worth it. It has all led you to an abandoned prison, deep within the woods. It may all have been a rumor, maybe even a trap, but you are desperate for answers. You want your brother back. Your life back.'
            self.messageCount = 2
        elif (self.messageCount == 2):
            self.message = 'You enter the abandoned building.'
            self.messageCount = 3
        elif (self.messageCount == 3):
            self.message = 'Upon entering, you see a torch to your left. Do you wish to take it?'
            self.messageCount = 4
        elif (self.messageCount == 4):
            if(self.userInput == 'Yes' or self.userInput == 'yes'):
                self.message = 'It will help to illuminate the pathway for you.'
                self.messageCount = 5
            elif(self.userInput == 'No' or self.userInput == 'no'):
                self.message = 'Your endeavor will be harder with your limited field of sight.'
                self.messageCount = 5
            else:
                self.message = 'Please enter either yes or no'
        elif (self.messageCount == 5):
            self.message = 'You go through the door, not knowing what awaits you on the other side.'
            self.messageCount = 6
            Map.getLocation('EAST')
        elif (self.messageCount == 6):
            self.message = 'You go through the door, not knowing what awaits you on the other side.'
            self.messageCount = 7
        elif (self.messageCount == 7):
            self.message = 'You hear a creaking noise down the hallway, what do you do?'
            self.messageCount = 8
        elif(self.messageCount == 8):
            if(self.userInput == 'ATTACK' or self.userInput == 'Attack' or self.userInput == 'attack'):
                self.manager.current = 'dice'
                num = randomNum()
                self.messageCount = 9
                self.attack(num)
            elif(self.userInput == 'PEEK' or self.userInput == 'Peek' or self.userInput == 'peek'):
                self.manager.current = 'dice'
                num = randomNum()
                self.messageCount = 9
                self.peek(num)
            else:
                self.message = 'Please enter peek or attack'
        elif(self.messageCount == 9):
            self.message = 'For the moment, you are safe. You managed to neutralize the threat in the room. What do you do? You can either continue and go north or retreat and go west'
            self.messageCount = 10
        else:
            
            value = parse(self.userInput)
            if(value.direction == 'NORTH' or value.direction == 'SOUTH' or value.direction == 'EAST' or value.direction == 'WEST'):
                Map.getLocation(value.direction)
                self.message = 'This is the end'
        self.ids.last_name.focus = True
        self.ids.output.text = self.message
        self.ids.last_name.focus = True
        self.focusInput()

    def attack(self, num):
        if(num > 15):
            self.message = 'Attack successful, you took him down easily.'
        else:
            self.message = 'Attack successful, unfortunately they put up a fight you lose 10 HP'

    def peek(self, num):
        if(num > 10):
            self.message = 'You were successful, the enemy doesn’t notice you.'
        else:
            self.message = 'The enemy noticed you and you prepare for a fight you lose 10 HP'

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


class TestApp(App):

    def build(self):
        return ScreenManagement()


if __name__ == '__main__':
    TestApp().run()
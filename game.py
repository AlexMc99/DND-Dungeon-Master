import kivy 
from kivy.app import App   
from kivy.uix.label import Label  
from kivy.uix.floatlayout import FloatLayout  
from kivy.uix.scatter import Scatter 
from kivy.uix.textinput import TextInput 
from kivy.uix.boxlayout import BoxLayout 
  
# Create the App class 
class TutorialApp(App): 
      
    def build(self): 
  
        b = BoxLayout(orientation ='vertical') 

        t = TextInput(font_size = 50, 
                      size_hint_y = None, 
                      height = 100,
                      padding = (10,10,10,10)) 
  
        b.add_widget(t) 
  
          
        return b 

if __name__ == "__main__": 
    TutorialApp().run() 
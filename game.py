#!/usr/bin/env python3

import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty, StringProperty, ObjectProperty

# TODO move node class and all nodes to nodes.py for easy writing
# from nodes import nodes

# TODO: visually organize text and buttons

class Node():

    # Basic unit of the RPG adventure, consisting of various properties.

    def __init__(self, name, text='', choices=['Continue'], text_input=False, image='test.jpg'):
        self.name = name
        self.text = text
        self.choices = choices
        self.text_input = text_input
        self.image = image
        self.active = False

class NodeNetwork():

    # The RPG adventure structure consisting of connected nodes.

    def __init__(self):
        # TODO: migrate these to nodes.py
        self.nodes = [Node('start',
                      text='Welcome to the machine!',
                      choices={'Tell me your name': 'name'}),
                 Node('name',
                      text='Please tell me your name.',
                      choices={'go go go': 'name',
                               'stop': 'name',
                               'stop stop stop': 'name'})]
        self.active_node = self.find_node('start')


    def find_node(self, name):
        try:
            return next(n for n in self.nodes if n.name == name)
        except StopIteration:
            exception = "couldn't find any node called {} in {}".format(name, [n.name for n in self.nodes])
            raise Exception(exception)


    def change_node(self, node_name):
        self.active_node = self.find_node(node_name)


class Choice_Button(Button):

    # A button that advances the RPG adventure per the user's choice.

    def __init__(self, network, node_name, **kwargs):
        super(Choice_Button, self).__init__(**kwargs)
        self.network = network
        self.target_node = node_name


    def change_node(self):
        self.network.change_node(self.target_node)


class NodeScreen(GridLayout):

    # The user interface widget.

    label = ObjectProperty(Label())
    buttons = ListProperty()
    image_name = StringProperty()
    image = ObjectProperty(Image())


    def __init__(self, **kwargs):
        super(NodeScreen, self).__init__(**kwargs)
        self.network = NodeNetwork()
        self.cols = 2
        self.rows = 3
        self.add_widget(self.image)
        self.add_widget(self.label)
        self.render()


    def render(self):
        self.update_label()
        self.update_pic()
        self.update_choices()


    def update_label(self):
        node = self.network.active_node
        self.label.text = node.text


    def update_pic(self):
        filename = self.network.active_node.image
        self.image.source='static/images/{}'.format(filename)


    def update_choices(self):
        node = self.network.active_node
        choices = self.network.active_node.choices
        for choice in choices:
            result = choices[choice]
            choose = Choice_Button(self.network, result, text=choice)
            choose.bind(on_press=self.button_change)
            self.buttons.append(choose)
            self.add_widget(choose)


    def button_change(self, button, **kwargs):
        self.clear_buttons()
        button.change_node()
        self.render()


    def clear_buttons(self):
        for button in self.buttons:
            self.remove_widget(button)


class RPGApp(App):

    def build(self):
        return NodeScreen()

if __name__ == '__main__':
    RPGApp().run()
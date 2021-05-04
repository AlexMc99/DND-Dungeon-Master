from kivymd.app import MDApp

he = '''
MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "MDToolbar"
        left_action_items: [["menu", lambda x: app.callback()]]

    MDLabel:
        text: "Content"
        halign: "center"

    Image:
        id: map
        source: "latestMap.png"
        size: root.size
'''


class DemoApp(MDApp):
    def build(self):
        self.theme.cls.primary_palette ="Yellow"
        self.theme.cls.theme_style

        return Builder.load_string(he)


DemoApp().run()
from kivymd.uix.gridlayout import MDGridLayout
from applib import FocusWithColor
from kivy.properties import StringProperty

class M3GridLayout(MDGridLayout):
    id = StringProperty()

    def __init__(self, **kwargs):
        super(M3GridLayout, self).__init__(**kwargs)


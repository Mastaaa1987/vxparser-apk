from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, BooleanProperty

class Header(MDLabel):
    name = StringProperty('header')
    font_style = StringProperty("H6")
    text = StringProperty()
    bold = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(Header, self).__init__(**kwargs)
    """ Settings Header"""

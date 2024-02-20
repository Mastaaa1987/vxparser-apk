from kivymd.uix.card.card import MDCard
from applib import FocusWithColor
from kivy.properties import StringProperty
from kivy.graphics import Color, Rectangle, RoundedRectangle

class Card(FocusWithColor, MDCard):
    def __init__(self, *args, **kwargs):
        super(Card, self).__init__(*args, **kwargs)
    """ Menu Buttons """


class M3Card(Card):
    name = StringProperty('card')
    text = StringProperty('Test')
    info = StringProperty('Info')

    def __init__(self, **kwargs):
        self.style = 'elevated'
        self.size =  [ "268dp", "150dp" ]
        self.size_hint = [ None, None ]
        self.spacing = "20dp"
        super(M3Card, self).__init__(**kwargs)


class M3SmartCard(Card):
    key = StringProperty()
    image_source = StringProperty()
    hidden = StringProperty()
    text = StringProperty()
    sv = StringProperty()

    def __init__(self, **kwargs):
        super(M3SmartCard, self).__init__(**kwargs)


from kivymd.uix.chip.chip import MDChip
from kivy.properties import StringProperty
from applib import FocusWithColor


class M3Chip(FocusWithColor, MDChip):
    name = StringProperty('chip')
    text = StringProperty()
    key = StringProperty()
    val = StringProperty()

    def __init__(self, **kwargs):
        super(M3Chip, self).__init__(**kwargs)


from kivymd.uix.boxlayout import MDBoxLayout
from applib import FocusWithColor
from kivy.properties import StringProperty

class M3SmartBox(MDBoxLayout):
    header = StringProperty()
    footer = StringProperty()
    key = StringProperty()
    image_source = StringProperty()

    def __init__(self, **kwargs):
        super(M3SmartBox, self).__init__(**kwargs)


class M3SpinnerBox(MDBoxLayout):
    def __init__(self, **kwargs):
        super(M3SpinnerBox, self).__init__(**kwargs)


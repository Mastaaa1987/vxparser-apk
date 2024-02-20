from kivymd.uix.scrollview import MDScrollView
from applib import FocusWithColor
from kivy.properties import StringProperty

class M3ScrollView(MDScrollView):
    height = StringProperty()

    def __init__(self, **kwargs):
        super(M3ScrollView, self).__init__(**kwargs)


class M3SmartView(MDScrollView):
    def __init__(self, **kwargs):
        super(M3SmartView, self).__init__(**kwargs)


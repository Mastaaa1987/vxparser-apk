from kivymd.uix.list.list import MDList
from kivy.properties import BooleanProperty, StringProperty
from applib import FocusWithColor


class M3List(MDList):
    def __init__(self, **kwargs):
        super(M3List, self).__init__(**kwargs)


class OMList(M3List):
    def __init__(self, **kwargs):
        super(OMList, self).__init__(**kwargs)


class OVList(M3List):
    def __init__(self, **kwargs):
        super(OVList, self).__init__(**kwargs)


class OXList(M3List):
    def __init__(self, **kwargs):
        super(OXList, self).__init__(**kwargs)



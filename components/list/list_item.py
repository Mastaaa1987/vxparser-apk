from kivymd.uix.list import BaseListItem
from kivy.properties import BooleanProperty, StringProperty
from applib import FocusWithColor


class ListItem(FocusWithColor, BaseListItem):
    def __init__(self, *args, **kwargs):
        super(ListItem, self).__init__(*args, **kwargs)


class ListHeader(ListItem):
    name = StringProperty('listheader')
    text = StringProperty()
    
    def __init__(self, **kwargs):
        super(ListHeader, self).__init__(**kwargs)


class X1ListItem(ListItem):
    name = StringProperty('listitem')
    text1 = StringProperty()
    color1 = StringProperty('#bcbcbc')
    awidth = StringProperty('0dp')

    def __init__(self, **kwargs):
        super(X1ListItem, self).__init__(**kwargs)


class M1ListItem(ListItem):
    name = StringProperty('listitem')
    text1 = StringProperty()
    color1 = StringProperty('#bcbcbc')
    awidth = StringProperty('0dp')

    def __init__(self, **kwargs):
        super(M1ListItem, self).__init__(**kwargs)


class M2ListItem(ListItem):
    name = StringProperty('listitem')
    text1 = StringProperty()
    text2 = StringProperty()
    color1 = StringProperty('#bcbcbc')
    color2 = StringProperty('#4c4e50')
    awidth = StringProperty('0dp')
    
    def __init__(self, **kwargs):
        super(M2ListItem, self).__init__(**kwargs)


class M3ListItem(ListItem):
    name = StringProperty('listitem')
    text1 = StringProperty()
    text0 = StringProperty()
    text2 = StringProperty()
    color1 = StringProperty('#bcbcbc')
    color0 = StringProperty('#bdcab3')
    color2 = StringProperty('#4c4e50')
    awidth = StringProperty('0dp')
    
    def __init__(self, **kwargs):
        super(M3ListItem, self).__init__(**kwargs)


from kivymd.uix.button import MDFloatingActionButton, MDFillRoundFlatButton, MDRoundFlatButton, MDRaisedButton
from kivymd.uix.button.button import BaseButton
from kivy.properties import StringProperty
from kivymd.uix.card.card import MDCard
from applib import FocusWithColor
from kivymd.app import MDApp


class M3Button(FocusWithColor, MDRoundFlatButton):
    name = StringProperty('button')
    text = StringProperty()
    key = StringProperty()
    val = StringProperty()
    val0 = StringProperty()
    text0 = StringProperty()

    def __init__(self, *args, **kwargs):
        super(M3Button, self).__init__(*args, **kwargs)

    def press(self):
        MDApp.get_running_app().__class__.callback(MDApp.get_running_app().__class__, self.key, self.val0)
        tmp_text = self.text
        tmp_val = self.val
        self.text = self.text0
        self.val = self.val0
        self.text0 = tmp_text
        self.val0 = tmp_val
        pass

    def add_widget(self, widget, index=0):
        super(M3Button, self).add_widget(widget)



class ButtonCard(FocusWithColor, MDCard):
    def __init__(self, *args, **kwargs):
        super(ButtonCard, self).__init__(*args, **kwargs)
    """ Menu Buttons """

class WideButton(ButtonCard):
    name = StringProperty('button')

    def __init__(self, **kwargs):
        self.style = 'elevated'
        self.md_bg_color = "#292d30"
        self.size =  [ "240dp", "64dp" ]
        self.size_hint = [ None, None ]
        self.spacing = "20dp"
        super(WideButton, self).__init__(**kwargs)


class ButtonBase(FocusWithColor, BaseButton):
    def __init__(self, *args, **kwargs):
        super(ButtonBase, self).__init__(*args, **kwargs)


class FilledButton(ButtonBase):
     name = StringProperty('button')
     
     def __init__(self, **kwargs):
         super(FilledButton, self).__init__(**kwargs)


class FlatButton(ButtonBase):
     name = StringProperty('button')
     
     def __init__(self, **kwargs):
         super(FlatButton, self).__init__(**kwargs)


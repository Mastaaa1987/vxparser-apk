from kivymd.uix.textfield.textfield import MDTextField
from applib import FocusWithColor
from kivy.properties import StringProperty
from kivymd.app import MDApp

class TextField(MDTextField):
    hint_text = StringProperty()
    name = StringProperty('textfield')
    helper_text = StringProperty()
    hidden = StringProperty()
    hhidden = StringProperty()
    key = StringProperty()
    awidth = StringProperty("200dp")


    def __init__(self, *args, **kwargs):
        MDApp.get_running_app().__class__.add_instances(MDApp.get_running_app().__class__, self)
        super(TextField, self).__init__(*args, **kwargs)
    

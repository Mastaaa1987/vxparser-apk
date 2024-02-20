from kivymd.uix.selectioncontrol.selectioncontrol import MDCheckbox
from kivy.properties import StringProperty

class M3Checkbox(MDCheckbox):
    name = StringProperty('checkbox')

    def __init__(self, **kwargs):
        super(M3Checkbox, self).__init__(**kwargs)
    
    def on_release(self):
        print(self)

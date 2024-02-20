from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.app import MDApp
from kivy.properties import BooleanProperty, StringProperty, NumericProperty

class M3Switch(MDSwitch):
    active = BooleanProperty(False)
    name = StringProperty('switch')
    key = StringProperty()
    shadow = NumericProperty(0)


    def __init__(self, **kwargs):
        super(M3Switch, self).__init__(**kwargs)
    
    def cb(self, next=None):
        app = MDApp.get_running_app()
        if self.active: app.callback(self.key, '1')
        else: app.callback(self.key, '0')

    #def active(self, *args):
        #print(self, args)
    

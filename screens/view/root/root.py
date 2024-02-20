from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

class RootScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_widget(self, widget, index=0):
        MDApp.get_running_app().__class__.root = self
        super(RootScreen, self).add_widget(widget)

from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty, ListProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from kivymd.uix.boxlayout import MDBoxLayout

class MainScreen(MDScreen):
    data = ListProperty()
    
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

    def add_widget(self, widget, index=0):
        super(MainScreen, self).add_widget(widget)

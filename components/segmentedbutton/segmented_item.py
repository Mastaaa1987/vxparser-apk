from kivymd.uix.segmentedbutton import MDSegmentedButton, MDSegmentedButtonItem
from kivy.properties import BooleanProperty, StringProperty
from applib import FocusWithColor

class M3SegmentedItem(FocusWithColor, MDSegmentedButtonItem):
    text = StringProperty()
    key = StringProperty()

    def __init__(self, *args, **kwargs):
        super(M3SegmentedItem, self).__init__(*args, **kwargs)


from kivymd.uix.card.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.imagelist.imagelist import MDSmartTile
from applib import FocusWithColor
from kivy.uix.image import Image
from kivymd.uix.fitimage.fitimage import FitImage
from kivy.properties import StringProperty
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.loader import Loader


class M3SmartTile(MDSmartTile):
    #name = StringProperty('scard')
    label = StringProperty()
    image_source = StringProperty()
    key = StringProperty()

    def __init__(self, **kwargs):
        super(M3SmartTile, self).__init__(**kwargs)


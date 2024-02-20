import sys
from kivy.properties import DictProperty, NumericProperty, ColorProperty, StringProperty
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.button import MDIconButton
from kivymd.uix.tooltip import MDTooltip
from kivymd.uix.card import MDCard
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
from kivy.animation import Animation
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.factory import Factory

from applib import FocusWithColor

class ElevationCard(RoundedRectangularElevationBehavior, MDCard):
    """ Base Class """

class MenuButton(FocusWithColor, MDIconButton, MDTooltip):
    name = StringProperty('_MenuButton')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_release(self):
        name = None
        app = MDApp.get_running_app()
        for i in range(0, len(app.items["RM"])):
            if self == app.items["RM"][i]:
                name = app.screen_names[i]
                break
        if not name is None:
            if not name == "exit": app.__class__.root.ids.screen_manager.current = (name)
            else: sys.exit()

    
class MagicMenu(ElevationCard): #ThemeableBehavior, 
    """ Base Class """
    name = StringProperty('_MagicMenu')
    pos_marker = NumericProperty(0)
    color_marker = ColorProperty([0, 0, 0, 1])
    menu_button = DictProperty(
            {
                "power": "Red",
                "alpha-m-circle-outline": "Indigo",
                "alpha-x-circle-outline": "Yellow",
                "cog": "BlueGray",
            }
    )

    def generate_menu(self):
        """ Gen Buttons """
        
        spacing_button = dp(12)
        start_position = dp(12)
        
        for i, name_icon in enumerate(self.menu_button.keys()):
            start_position += spacing_button
            if i == 1 or i == 3:
                start_position += (self.height / 10 * 2)
            menu_button = Factory.RMB(icon=name_icon)
            if i == 3:
                menu_button.y = ( 24.0 )
            else:
                menu_button.y = (
                    self.height - (menu_button.height * (i + 1) + start_position)
                )
            menu_button.bind(on_focused=self.set_menu_marker)
            self.ids.buttons_container.add_widget(menu_button)

        self.set_menu_marker(self.ids.buttons_container.children[0])

    def set_menu_marker(self, instance_menu_button: MenuButton):
        """ Color and Pos of area for selected menu items """
        
        anim = Animation(
            pos_marker=instance_menu_button.y - dp(4),
            #color_marker=get_color_from_hex(
                #colors[self.menu_button[instance_menu_button.icon]]["500"]
            #),
            t="in_out_sine",
            d=0.3,
        )
        #anim.bind(on_complete=self.set_screen_color)
        anim.start(self)
        
    #def set_screen_color(self, *args):
        #""" Background color of root Screen """
        
        #anim = Animation(
            #md_bg_color=self.color_marker,
            #t="in_out_sine",
            #d=0.3,
        #)
        #anim.start(self)

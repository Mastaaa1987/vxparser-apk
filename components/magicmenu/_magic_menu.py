from kivy.properties import DictProperty, NumericProperty, ColorProperty
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.button import MDIconButton
from kivymd.uix.tooltip import MDTooltip
from kivymd.uix.card import MDCard
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
from kivy.animation import Animation

class ElevationCard(RoundedRectangularElevationBehavior, MDCard):
    """ Base Class """

class MenuButton(MDIconButton, MDTooltip):
    """ Menu Buttons """
    
class MagicMenu(ElevationCard): #ThemeableBehavior, 
    """ Base Class """
    pos_marker = NumericProperty(0)
    #color_marker = ColorProperty([0, 0, 0, 0])
    menu_button = DictProperty(
            {
                "home": "Red",
                "account": "Indigo",
                "message": "Teal",
                "help": "Yellow",
                "close": "BlueGray",
            }
    )

    def generate_menu(self):
        """ Gen Buttons """
        
        spacing_button = dp(12)
        start_position = dp(6)
        
        for i, name_icon in enumerate(self.menu_button.keys()):
            start_position += spacing_button
            menu_button = MenuButton(icon=name_icon)
            menu_button.x = (
                self.width - (menu_button.width * (i + 1) + start_position)
            )
            print(self.ids, menu_button)
            menu_button.bind(on_enter=self.set_menu_marker)
            self.ids.buttons_container.add_widget(menu_button)

        #self.set_menu_marker(self.ids.buttons_container.children[0])

    def set_menu_marker(self, instance_menu_button: MenuButton):
        """ Color and Pos of area for selected menu items """
        
        anim = Animation(
            pos_marker=instance_menu_button.x - dp(4),
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

import components
#from .highlight import HighlightBehavior

from kivy.uix.behaviors import FocusBehavior
from kivymd.app import MDApp
from kivy.graphics import InstructionGroup, Color, Rectangle, RoundedRectangle, Callback, Line
from kivy.factory import Factory
from kivy.metrics import dp
from kivy.animation import Animation
from kivy.properties import BooleanProperty, ObjectProperty, ListProperty, OptionProperty, NumericProperty
from kivy.clock import Clock
from kivy.event import EventDispatcher

class FocusWithColor(FocusBehavior):

    _color = None
    _rect = None
    current_focused = BooleanProperty(False)
    current_highlighted = ObjectProperty(None, allownone=True)
    instruction_canvas = ObjectProperty(InstructionGroup())
    _size = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super(FocusWithColor, self).__init__(*args, **kwargs)
        MDApp.get_running_app().__class__.add_instances(MDApp.get_running_app().__class__, self)
        with self.canvas.before:
            self._color = Color(199, 198, 203, .0)
            self._rect = RoundedRectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self._rect.pos = instance.pos
        self._rect.size = instance.size

    def on_focused(self, instance, value, *largs):
        self.fcb()

    def redraw_canvas(self, *args):
        self.instruction_canvas.clear()
        self.instruction_canvas.add(Color(199, 198, 203, 1))
        self.instruction_canvas.add(Line(rounded_rectangle=self.pos + self.size + [dp(5)], width=1.01))

    def _scroll(self, par0, par1, st):
        if st == 'x':
            if par0.width - par1.width > 0:
                scroll_to = 1 / (par0.width - par1.width) * (self.pos[0] - 30)
                if scroll_to < 0: scroll_to = 0
                elif scroll_to > 1: scroll_to = 1
                par1.scroll_x = scroll_to
        elif st == 'y':
            if par0.height - par1.height > 0:
                scroll_to = 1 / (par0.height - par1.height) * self.pos[1]
                if scroll_to < 0: scroll_to = 0
                elif scroll_to > 1: scroll_to = 1
                par1.scroll_y = scroll_to
        pass

    def fcb(self, next=None):
        if self.current_focused == False:
            self.current_focused = True
            if "MSV1I" in str(self.__class__):
                self.size = [ "295dp", "165dp"]
                self._scroll(self.parent, self.parent.parent, 'x')
            elif "XSV1SC" in str(self.__class__):
                self.md_bg_color = [199, 198, 203, .5]
                self._scroll(self.parent.parent.parent.parent, self.parent.parent.parent.parent.parent, 'x')
            elif "OMC" in str(self.__class__):
                self.size = [ str(int(self.width)+10)+'dp', str(int(self.height)+5)+'dp' ]
            else:
                self._color.rgba = [199, 198, 203, .1]
                if "MSV2" in str(self.__class__) or "MSV3" in str(self.__class__) or "OSV1" in str(self.__class__) or "OSV2" in str(self.__class__) or "OSV3" in str(self.__class__):
                    self._scroll(self.parent, self.parent.parent, 'y')
        else:
            self.current_focused = False
            if "MSV1I" in str(self.__class__): self.size =  [ "268dp", "150dp" ]
                #anim = Animation(size=(268, 150), duration=.1)
                #anim.start(self)
                #self.style = 'elevated'
                #self.line_color = "#2A2C2D"
                #self.md_bg_color = "#202224"
                #self.canvas.after.remove(self.instruction_canvas)
                #self.instruction_canvas.clear()
            elif "XSV1SC" in str(self.__class__): self.md_bg_color = "#202224"
            elif "OMC" in str(self.__class__): self.size = [ str(int(self.width)-10)+'dp', str(int(self.height)-5)+'dp' ]
            else: self._color.rgba = [199, 198, 203, .0]
        if next:
            next.fcb()

    def add_widget(self, widget, index=0):
        super(FocusWithColor, self).add_widget(widget)

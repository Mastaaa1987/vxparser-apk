from kivymd.uix.spinner.spinner import MDSpinner
from kivy.properties import BooleanProperty

class M3Spinner(MDSpinner):
    active = BooleanProperty(True)

    def __init__(self, **kwargs):
        super(M3Spinner, self).__init__(**kwargs)


class M2Spinner(MDSpinner):
    active = BooleanProperty(True)

    def __init__(self, **kwargs):
        super(M2Spinner, self).__init__(**kwargs)


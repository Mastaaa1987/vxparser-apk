from android.runnable import run_on_ui_thread
from jnius import autoclass, cast, PythonJavaClass, java_method

KeyEvent = autoclass('android.view.KeyEvent')
PythonActivity = autoclass('org.kivy.android.PythonActivity')

class KeyListener(PythonJavaClass):
    __javacontext__ = 'app'
    __javainterfaces__ = ['android/view/View$OnKeyListener']

    def __init__(self, listener):
        super().__init__()
        self.listener = listener

    @java_method('(Landroid/view/View;ILandroid/view/KeyEvent;)Z')
    def onKey(self, v, key_code, event):
        if event.getAction() == KeyEvent.ACTION_DOWN and\
           key_code == KeyEvent.KEYCODE_BACK: 
            return self.listener()

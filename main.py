import importlib, json, os, tty, termios, sys, signal, re, aiosqlite, asyncio
from multiprocessing import Process, Manager
from concurrent.futures import ThreadPoolExecutor

from oscpy.server import OSCThreadServer
from oscpy.client import OSCClient

from kivy import Config
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.logger import Logger, LOG_LEVELS
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.utils import asynckivy
from kivy.utils import platform
from functools import partial

import utils.common as com
com.check()
import components, applib, screens
#if platform == 'android':
    #from android.runnable import run_on_ui_thread
    #from jnius import autoclass, cast, PythonJavaClass, java_method



class Parser(MDApp):
    add_instances = applib.add_instances
    callback = applib.callback
    items = {}
    list_focus = {}
    root = current_focused = current_sub = current_on_focus = current_list = sm = current_segment = service = server = client = other_task = None
    screen_names = [ "exit", "main", "xstream", "options" ]
    lists = [ "RM", "MSV1", "MSV2", "MSV3", "OSV0", "OSV1", "OSV2", "OSV3", "XSV0", "XSV1" ]
    screens = {}
    olists = {}
    other_tasks = []
    Logger.setLevel(LOG_LEVELS["info"])
    for item in lists:
        list_focus[item] = None
        items[item] = []


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_file(f'''{screens.root_screen["kv"]}''')
        self.root = screens.RootScreen()
        

    def build(self):
        Window.bind(on_keyboard=applib.Keyboard)
        Window.bind(on_joy_button_down=applib.Keyboard)
        com.set_setting('osc_port', '0')
        colors = self.theme_cls.colors
        colors["Dark"]["Background"] = "#2E3032"
        colors["Dark"]["FlatButtonDown"] = "#CCCCCC"
        self.theme_cls.colors = colors
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.material_style = "M3"
        self.server = server = OSCThreadServer()
        server.listen('localhost', default=True)
        server.bind(b'/log', self.recieve_log)
        server.bind(b'/echo', self.recieve_echo)
        server.bind(b'/reg', self.register_service)
        server.bind(b'/cb', self.recieve_callback)
        server.bind(b'/stat', self.recieve_stat)
        com.set_setting('osc_port', str(server.getaddress()[1]))
        for kv in components.kvs:
            Builder.load_file(f'''{kv}''')
        for screen in screens.screens:
            name_screen = screen["name"]
            Builder.load_file(f'''{screen["kv"]}''')
            view = eval(f'screens.{screen["screen_name"]}()')
            view.name = name_screen
            self.screens[name_screen] = view
            self.root.ids.screen_manager.add_widget(view)
        self.sm = self.root.ids.screen_manager
        magic_menu = components.MagicMenu()
        magic_menu.generate_menu()
        self.root.ids.nav.add_widget(magic_menu)
        self.items["RM"][1].fcb()
        self.current_focused = self.items["RM"][1]
        self.current_list = "RM"
        self.current_segment = "OSV1"
        Clock.schedule_once(self.builder)

        return self.root


    def on_start(self):
        Clock.schedule_once(partial(applib.start_service, self), 5)


    def builder(self, *args):
        Clock.schedule_once(lambda x: asynckivy.start(applib.main()))
        Clock.schedule_once(lambda x: asynckivy.start(applib.settings()))


    def on_marked(self, segment_button, segment_item, marked) -> None:
        view = self.screens['options']
        cs = { 'Main': 'OSV1', 'Vavoo': 'OSV2', 'Xstream': 'OSV3' }
        if segment_item.text in self.olists:
            view.ids.list.clear_widgets()
            for o in self.olists[segment_item.text]:
                view.ids.list.add_widget(o)
            self.current_segment = cs[segment_item.text]


    def register_service(self, message, *args):
        msg = message.decode('utf8')
        self.client = OSCClient(b'localhost',int(msg))


    def recieve_echo(self, msg, *args):
        Clock.schedule_once(partial(applib.callback_echo, self, msg), 0.5)


    def recieve_log(self, lvl, msg, typ=None, name=None, *args):
        Clock.schedule_once(partial(applib.callback_log, self, lvl, msg, typ, name), 0.5)

    def recieve_stat(self, name, typ, msg, *args):
        Clock.schedule_once(partial(applib.callback_stat, self, name, typ, msg), 0.5)

    def recieve_callback(self, key, val, *args):
        if key.decode('utf8') == 'global_search':
            if val.decode('utf8') == '1':
                Clock.schedule_once(partial(applib.callback_callback, self), 0.5)
            else:
                tf = self.screens['xstream'].ids.li1.ids.action.children[0]
                if not tf.hidden == '': tf.helper_text = 'No Entry found for: %s' %(tf.hidden)
                else: tf.helper_text = 'No Entry found!'
                tf.error = True
                self.screens['xstream'].ids.gl1.clear_widgets()
        if key.decode('utf8') == 'do_search':
            Clock.schedule_once(partial(applib.callback_xstream, self, val), 0.5)


    def exit(self):
        Logger.info('terminating ALL and exiting ...')
        if self.client:
            self.client.send_message(b'/kill', [])
        if not platform == 'android' and self.service:
            self.service.join(timeout=3)
            if self.service.is_alive():
                self.service.terminate()
        sys.exit()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, applib.signal_handler)
    signal.signal(signal.SIGTERM, applib.signal_handler)

    Parser().run()

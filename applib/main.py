import time
from kivy.factory import Factory
from kivymd.app import MDApp
import utils.common as com
from helper import sites
from kivymd.utils import asynckivy
from kivy.utils import platform
from kivy.logger import Logger
from kivy.clock import Clock
from multiprocessing import Process, Manager
if platform == 'android':
    from jnius import autoclass


def signal_handler(signal, frame):
    Logger.info(" CTRL + C detected, exiting ... ")
    exit(0)


def add_instances(self, widget):
    if "RM" in str(widget.__class__):
        if len(self.items["RM"]) == 1: self.list_focus["RM"] = widget
        self.items["RM"].append(widget)
    elif "MSV1" in str(widget.__class__):
        self.items["MSV1"].append(widget)
        self.list_focus["MSV1"] = widget
    elif "MSV2" in str(widget.__class__):
        if self.list_focus["MSV2"] == None: self.list_focus["MSV2"] = widget
        self.items["MSV2"].append(widget)
    elif "MSV3" in str(widget.__class__):
        if self.list_focus["MSV3"] == None: self.list_focus["MSV3"] = widget
        self.items["MSV3"].append(widget)
    elif "OSV0" in str(widget.__class__):
        if self.list_focus["OSV0"] == None:
            self.list_focus["OSV0"] = widget
            widget.active = True
        self.items["OSV0"].append(widget)
    elif "OSV1" in str(widget.__class__) and not "OSV1H" in str(widget.__class__):
        if self.list_focus["OSV1"] == None: self.list_focus["OSV1"] = widget
        self.items["OSV1"].append(widget)
    elif "OSV2" in str(widget.__class__) and not "OSV2H" in str(widget.__class__):
        if self.list_focus["OSV2"] == None: self.list_focus["OSV2"] = widget
        self.items["OSV2"].append(widget)
    elif "OSV3" in str(widget.__class__) and not "OSV3H" in str(widget.__class__):
        if self.list_focus["OSV3"] == None: self.list_focus["OSV3"] = widget
        self.items["OSV3"].append(widget)
    elif "XSV0" in str(widget.__class__):
        if self.list_focus["XSV0"] == None: self.list_focus["XSV0"] = widget
        self.items["XSV0"].append(widget)
    elif "XSV1" in str(widget.__class__):
        self.list_focus["XSV1"] = widget
        self.items["XSV1"].append(widget)



def callback_stat(self, name, typ, msg, *args):
    name = name.decode('utf8')
    typ = typ.decode('utf8')
    msg = msg.decode('utf8')
    for child in self.screens['main'].ids.gl1.children:
        if name in child.ids.action.children[0].key:
            print(name)
            if msg == 'done': child.ids.action.children[0].active = False
            if msg == 'start': child.ids.action.children[0].active = True


def callback_log(self, lvl, msg, typ=None, name=None, *args):
    widget = Factory.MSV2I2()
    children = []
    if len(self.screens['main'].ids.list2.children) > 0:
        for child in self.screens['main'].ids.list2.children:
            children.insert(0, child)
    if int(lvl.decode('utf8')) == 1: t = 'INFO'
    elif int(lvl.decode('utf8')) == 3: t = 'ERROR'
    if typ or name:
        if typ and name: widget.text2 = '[%s] [%s] [%s]' %(t, typ.decode('utf8').upper(), name.decode('utf8').upper())
        elif typ: widget.text2 = '[%s] [%s]' %(t, typ.decode('utf8').upper())
        elif name: widget.text2 = '[%s] [%s]' %(t, name.decode('utf8').upper())
    else: widget.text2 = '[%s]' %(t)
    widget.text1 = '%s' %(msg.decode('utf8'))
    self.screens['main'].ids.list2.clear_widgets()
    self.screens['main'].ids.list2.add_widget(widget)
    if len(children) > 0:
        for child in children:
            self.screens['main'].ids.list2.add_widget(child)
    if typ and name:
        if name.decode('utf8').upper() == 'SERVICE':
            if typ.decode('utf8').upper() == 'API':
                if "Successful started" in msg.decode('utf8'): a = True
                else: a = False
                for child in self.screens['main'].ids.gl1.children:
                    if child.ids.action.children[0].key == 'main-api':
                        c = child.ids.action.children[0]
                        c.active = a



def callback_callback(self, *args):
    async def global_search():
        cache = com.get_cache('global_search')
        if len(cache) > 0:
            children = []
            for i in range(0, len(cache)):
                loads = cache[i]
                if len(loads) > 0:

                    for x in range(0, len(loads)):
                        load = loads[x]
                        obj = Factory.XSV1SB()
                        obj2 = Factory.XSV1SC()
                        obj3 = Factory.XSV1ST()
                        obj.header = load["name"]
                        obj3.image_source = load["thumb"]
                        obj.footer = load["domain"]
                        key = str(i)+':'+str(x)
                        obj.key = obj2.key = obj3.key = key
                        obj2.ids.image.add_widget(obj3)
                        obj.ids.ibox.add_widget(obj2)
                        children.insert(0, obj)
            if len(children) > 0:
                view = self.screens['xstream'].ids.gl1
                view.clear_widgets()
                for child in children:
                    await asynckivy.sleep(0)
                    view.add_widget(child)

    asynckivy.start(global_search())


def callback_echo(self, msg, *args):
    widget = Factory.MSV3I1()
    children = []
    if len(self.screens['main'].ids.list3.children) > 0:
        for child in self.screens['main'].ids.list3.children:
            children.insert(0, child)
    widget.text1 = '%s' %(msg.decode('utf8'))
    self.screens['main'].ids.list3.clear_widgets()
    self.screens['main'].ids.list3.add_widget(widget)
    if len(children) > 0:
        for child in children:
            self.screens['main'].ids.list3.add_widget(child)


def callback_xstream(self, val, *args):
    widget = Factory.XLV1I2()
    children = []
    if len(self.screens['xstream'].ids.lv1.children) > 0:
        for child in self.screens['xstream'].ids.lv1.children:
            children.insert(0, child)
    if val.decode('utf8') == '1':
        widget.text1 = 'Auswahl wurde erfolgreich zur Datenbank hinzugefügt ...'
        widget.text2 = 'Mehr Info unter Main - Messages.'
    else:
        widget.text1 = 'Fehler beim hinzufügen der Auswahl!'
        widget.text2 = 'Bitte starte die Suche erneut!'
    self.screens['xstream'].ids.lv1.clear_widgets()
    self.screens['xstream'].ids.lv1.add_widget(widget)
    if len(children) > 0:
        for child in children:
            self.screens['xstream'].ids.lv1.add_widget(child)


def start_service(self, *args):
    #if None:
    if platform == 'android':
        from android import mActivity
        sPort = com.get_setting('osc_port')
        context =  mActivity.getApplicationContext()
        SERVICE_NAME = str(context.getPackageName()) +\
            '.Service' + 'Task'
        self.service = autoclass(SERVICE_NAME)
        self.service.start(mActivity, sPort)
    else:
        import services
        self.service = Process(target=services.service)
        self.service.start()


def callback(self, key, val=None, instance=None, shadow=None):
    if "setting-" in key:
        key = key.replace('setting-', '')
        tmp_val = ''
        if val:
            tmp_val = val
        tmp_key = com.get_setting(key)
        if not tmp_val == tmp_key:
            com.set_setting(key, tmp_val)
    elif "main-" in key:
        key = key.replace('main-', '')
        if key == 'api':
            if str(val) == '1': self.client.send_message(b'/reg', ["api_start".encode('utf8')])
            elif str(val) == '0': self.client.send_message(b'/reg', ["api_stop".encode('utf8')])
        if key == 'm3u8':
            if str(val) == '1': self.client.send_message(b'/reg', ["m3u8_start".encode('utf8')])
            elif str(val) == '0': self.client.send_message(b'/reg', ["m3u8_stop".encode('utf8')])
        if key == 'epg':
            if str(val) == '1': self.client.send_message(b'/reg', ["epg_start".encode('utf8')])
            elif str(val) == '0': self.client.send_message(b'/reg', ["epg_stop".encode('utf8')])
        if key == 'services':
            if str(val) == '1': self.client.send_message(b'/reg', ["service_restart".encode('utf8')])
            elif str(val) == '0': self.client.send_message(b'/reg', ["service_stop".encode('utf8')])
        if key == 'xstream':
            if str(val) == '1': self.client.send_message(b'/reg', ["xstream_start".encode('utf8')])
            elif str(val) == '0': self.client.send_message(b'/reg', ["xstream_stop".encode('utf8')])
    elif "xstream-" in key:
        key = key.replace('xstream-', '')
        if not val == '':
            import utils.xstream as xstream
            view = self.screens['xstream'].ids.gl1
            view.clear_widgets()
            self.items["XSV1"].clear()
            self.list_focus["XSV1"] = None
            obj = Factory.XSS()
            view.add_widget(obj)
            obj = Factory.XS()
            view.add_widget(obj)

            if instance:
                if not instance.hidden == '':
                    instance.hhidden = instance.hidden
                instance.hidden = instance.text
                instance.hint_text = instance.text
                instance.helper_text = ''
                instance.text = ''
            proc = Process(target=xstream.search, args=(val,))
            proc.start()
    elif "do_search" in key:
        if not val == '':
            import utils.xstream as xstream
            proc = Process(target=xstream.do_search, args=(val,))
            proc.start()


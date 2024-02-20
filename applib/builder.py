import json, aiosqlite
from kivy.factory import Factory
from kivymd.app import MDApp
import utils.common as com
from helper import sites
from kivymd.utils import asynckivy
from kivy.lang import Builder


def database(self, *args):
    async def look():
        app = MDApp.get_running_app()
        view = app.screens['database']
        con = com.con
        cur = con.cursor()
        x = 0
        for site in sites.sites:
            print(site.SITE_IDENTIFIER)
            cur.execute('SELECT * FROM info WHERE site="' + str(site.SITE_IDENTIFIER) + '"')
            test = cur.fetchone()
            if test:
                print('test')
                x += 1
                children = []
                for row in cur.execute('SELECT * FROM info WHERE site="' + str(site.SITE_IDENTIFIER) + '"'):
                    box = Factory.DSVB()
                    card = Factory.DSVC()
                    tile = Factory.DSVT()
                    box.header = row['name']
                    if not row['releaseDate'] == '':
                        box.footer = row['releaseDate']
                    if not row['poster'] == '':
                        tile.image_source = row['poster']
                    elif not row['backdrop'] == '':
                        tile.image_source = row['backdrop']
                    card.sv = 'sv'+str(x)
                    if not row['description'] == '':
                        card.hidden = row['description']
                    card.ids.image.add_widget(tile)
                    box.ids.ibox.add_widget(card)
                    children.insert(0, box)
                if len(children) > 0:
                    await asynckivy.sleep(0)
                    head = Factory.DH()
                    head.text = site.SITE_IDENTIFIER
                    scr = Factory.DSV()
                    for child in children:
                        scr.ids.gl.add_widget(child)
                    view.ids.list.add_widget(head)
                    view.ids.list.add_widget(scr)
                    break

    asynckivy.start(look())


async def main():
    with open('applib/main.json') as k:
        r = json.load(k)
    app = MDApp.get_running_app()
    view = app.screens['main']
    children = []
    for item in r:
        obj = Factory.MSV1I()
        action = Factory.MSW()
        action.key = 'main-'+item["key"]
        obj.text = item["title"]
        obj.ids.action.add_widget(action)
        children.insert(0, obj)
    for child in children:
        view.ids.gl1.add_widget(child)
    await asynckivy.sleep(0)


async def settings():
    with open('applib/config.json') as k:
        r = json.load(k)
    app = MDApp.get_running_app()
    view = app.screens['options']
    section = None
    for item in r:
        if not item["section"] == section:
            if not item["section"] in app.olists: app.olists[item["section"]] = []
            obj = Factory.OH()
            obj.text = item["section"]
            obj.bold = True
            app.olists[item["section"]].append(obj)
            section = item["section"]
        if item["type"] == "title":
            if item["section"] == 'Main':
                obj = Factory.OSV1H()
            elif item["section"] == 'Vavoo':
                obj = Factory.OSV2H()
            elif item["section"] == 'Xstream':
                obj = Factory.OSV3H()
            obj.text = item["title"]
            app.olists[item["section"]].append(obj)
        if not item["type"] == "title":
            if item["section"] == 'Main':
                if "desc" in item and "head" in item:
                    obj = Factory.OSV1I3()
                elif "desc" in item or "head" in item:
                    obj = Factory.OSV1I2()
                else:
                    obj = Factory.OSV1I1()
            elif item["section"] == 'Vavoo':
                if "desc" in item and "head" in item:
                    obj = Factory.OSV2I3()
                elif "desc" in item or "head" in item:
                    obj = Factory.OSV2I2()
                else:
                    obj = Factory.OSV2I1()
            elif item["section"] == 'Xstream':
                if "desc" in item and "head" in item:
                    obj = Factory.OSV3I3()
                elif "desc" in item or "head" in item:
                    obj = Factory.OSV3I2()
                else:
                    obj = Factory.OSV3I1()
            obj.text1 = item["title"]
            if "desc" in item: obj.text2 = item["desc"]
            if "head" in item: obj.text0 = item["head"]
            sett = com.get_setting(item["key"])
        if item["type"] == "bool":
            obj2 = Factory.OSW()
            obj2.key = 'setting-'+item["key"]
            if sett:
                if bool(int(sett)) == True: obj2.active = True
                else: obj2.active = False
            obj.awidth = "60dp"
            obj.ids.action.add_widget(obj2)
            app.olists[item["section"]].append(obj)
        if item["type"] == "numeric" or item["type"] == "string":
            obj2 = Factory.OTF()
            obj2.key = 'setting-'+item["key"]
            if "default" in item: obj2.hint_text = str(item["default"])
            if sett: obj2.text = str(sett)
            if item["type"] == "numeric":
                obj2.input_filter = "int"
                obj2.awidth = "75dp"
                obj.awidth = "75dp"
            else:
                obj.awidth = "200dp"
            obj.ids.action.add_widget(obj2)
            app.olists[item["section"]].append(obj)
        if item["type"] == "select":
            obj2 = Factory.OSB()
            obj2.key = 'setting-'+item["key"]
            j = json.loads(item["selection"])
            if sett and j:
                obj2.text = j[sett]
                obj2.val = sett
            for s in j:
                if not s == sett:
                  obj2.val0 = s
                  obj2.text0 = j[s]
            if item["key"] == 'epg_provider' or item["key"] == 'epg_logos': obj.awidth = '100dp'
            else: obj.awidth = '75dp'
            obj.ids.action.add_widget(obj2)
            app.olists[item["section"]].append(obj)
    obj = Factory.OH()
    obj.text = 'Xstream'
    obj.bold = True
    app.olists['Xstream'] = []
    app.olists['Xstream'].append(obj)
    obj = Factory.OSV3H()
    obj.text = 'Site Settings'
    app.olists['Xstream'].append(obj)
    for site in sites.sites:
        obj = Factory.OSV3I2()
        obj.text1 = site.SITE_IDENTIFIER
        obj.text2 = 'Global [Search] | [Automatic] Search'
        obj.awidth = "150dp"
        obj2 = Factory.OMC()
        obj2.text = 'Search'
        obj2.key = 'setting-'+site.SITE_IDENTIFIER+'_search'
        ss = bool(int(com.get_setting(site.SITE_IDENTIFIER+'_search', 'Xstream')))
        if ss == True: obj2.active = True
        else: obj2.active = False
        obj.ids.action.add_widget(obj2)
        obj2 = Factory.OMC()
        obj2.text = 'Auto'
        obj2.key = 'setting-'+site.SITE_IDENTIFIER+'_auto'
        sa = bool(int(com.get_setting(site.SITE_IDENTIFIER+'_auto', 'Xstream')))
        if sa == True: obj2.active = True
        else: obj2.active = False
        obj.ids.action.add_widget(obj2)
        app.olists['Xstream'].append(obj)
    #for o in app.olists['Main']:
        #view.ids.list.add_widget(o)
    await asynckivy.sleep(0)


def test(self, *args):
    f = Builder.load_string('''
Widget:
    OH:
        text: 'Main'

    OSV1H:
        text: 'Server Settings'

    OSV1I2:
        text1: 'FastAPI Server IP'
        text2: 'default: 0.0.0.0 #to listen on all ips'

        OTF:
            key: 'setting-server_host'
            hint_text: "0.0.0.0"

    OSV1I2:
        text1: 'FastAPI Server Port'
        text2: 'default: 8080'
        awidth: "75dp"

        OTF:
            input_filter: "int"
            awidth: "75dp"
            key: 'setting-server_port'
            hint_text: "8080"

    OSV1I2:
        text1: 'Set Automatic Network IP to Server IP'
        text2: 'default: True'
        awidth: "60dp"

        OSW:
            key: 'setting-server_service'

    OSV1I2:
        text1: 'Server IP for M3U8 List Creation'
        text2: '(If Set Automatic Network IP to Server IP to False)'
        awidth: "200dp"

        OTF:
            key: 'setting-server_ip'

    OSV1H:
        text: 'Misc Settings'

    OSV1I2:
        text1: 'LogLevel'
        text2: 'default: Error'
        awidth: "75dp"

        OSB:
            key: 'setting-log_lvl'
            text: 'Error'
            val: '3'
            text0: 'Info'
            val0: '1'

    OSV1I3:
        text1: 'Search in TMDB after VoD & Series Infos'
        text2: 'default: False'
        text0: 'Verlangsamt den Get New VoDs & Series Prozess!'
        awidth: "60dp"

        OSW:
            key: 'setting-get_tmdb'

    OSV1I2:
        text1: 'Bevorzugter codec für Xtream Codes'
        text2: 'default: ts'
        awidth: "75dp"

        OSB:
            key: 'setting-xtream_codec'
            text: 'ts'
            val: 't'
            text0: 'hls'
            val0: 'h'

    OSV1H:
        text: 'SerienStream Accound (s.to)'

    OSV1I2:
        text1: 'Username'
        text2: 'SerienStream (s.to)'

        OTF:
            key: 'setting-serienstream_username'

    OSV1I2:
        text1: 'Password'
        text2: 'SerienStream (s.to)'

        OTF:
            key: 'setting-serienstream_password'

    OH:
        text: 'Vavoo'

    OSV2H:
        text: 'Live TV Settings'

    OSV2I3:
        text1: 'Automatic M3U8 List Creation for LiveTV'
        text2: 'default: False'
        text0: 'Background Service'
        awidth: "60dp"

        OSW:
            key: 'setting-m3u8_service'

    OSV2I3:
        text1: 'Warte Zeit für M3U8 List Creation'
        text0: 'Background Service Wartezeit in Stunden'
        text2: 'default: 12'
        awidth: "75dp"

        OTF:
            input_filter: "int"
            awidth: "75dp"
            hint_text: "12"
            key: 'setting-m3u8_sleep'

    OSV2I3:
        text1: 'Generate HLS M3U8'
        text2: 'default: True'
        text0: 'Generiert 2. M3U8 Liste (<county>_hls.m3u8)'
        awidth: "60dp"

        OSW:
            key: 'setting-m3u8_hls'

    OSV2I3:
        text1: 'Vavoo Channel Namen ersetzen'
        text2: 'default: True'
        text0: 'Ändert die Anzeigenamen in M3U8 Lists'
        awidth: "60dp"

        OSW:
            key: 'setting-m3u8_name'

    OSV2H:
        text: 'Programm Zeitschrift (EPG)'

    OSV2I2:
        text1: 'Provider to get EPG Infos'
        text2: 'default: Magenta'
        awidth: "100dp"

        OSB:
            text: 'Magenta'
            val: 'm'
            text0: 'TvSpielfilme'
            val0: 't'
            key: 'setting-epg_provider'

    OSV2I2:
        text1: 'Provider IDs mit Rytec IDs ersetzen'
        text2: 'default: True'
        awidth: "60dp"

        OSW:
            key: 'setting-epg_rytec'

    OSV2I2:
        text1: 'Bevorzugte Channel Logos'
        text2: 'default: Provider'
        awidth: "100dp"

        OSB:
            text: 'Provider'
            val: 'p'
            text0: 'Original'
            val0: 'o'
            key: 'setting-epg_logos'

    OSV2H:
        text: 'EPG Service Settings'

    OSV2I3:
        text0: 'Background Service'
        text1: 'Start Automatic epg.xml.gz Creation for LiveTV'
        text2: 'default: False'
        awidth: "60dp"

        OSW:
            key: 'setting-epg_service'

    OSV2I3:
        text1: 'Wartezeit für epg.xml.gz Creation Service'
        text2: 'default: 5'
        text0: 'Background Service Wartezeit in Tagen'
        awidth: "75dp"

        OTF:
            input_filter: "int"
            awidth: "75dp"
            hint_text: "5"
            key: 'setting-epg_sleep'

    OSV2I3:
        text1: 'Anzahl an Tagen für epg.xml.gz Erstellung'
        text2: 'default: 7'
        text0: 'Background Service Grabbing Zeit in Tagen'
        awidth: "75dp"

        OTF:
            input_filter: "int"
            awidth: "75dp"
            hint_text: "7"
            key: 'setting-epg_grab'
            ''')

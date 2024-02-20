import components, sys
from kivymd.app import MDApp
from kivymd.toast import toast
from kivy.factory import Factory


def Keyboard(self, window, key, *args):
    app = MDApp.get_running_app()
    keycode = key
    #toast(str(key))
    next = prev = None
    instance = app.current_focused
    for i in range(0, len(app.items[app.current_list])):
        if app.items[app.current_list][i] == instance:
            if i < (len(app.items[app.current_list]) - 1): next = app.items[app.current_list][i+1]
            else: next = app.items[app.current_list][0]
            if i > 0: prev = app.items[app.current_list][i-1]
            else: prev = app.items[app.current_list][len(app.items[app.current_list])-1]
    if keycode == 16 or keycode == 139: key_m(app, instance, next, prev)
    if keycode == 40 or keycode == 0: key_enter(app, instance, next, prev)
    if keycode == 44 or keycode == 118: key_space(app)
    if keycode == 79 or keycode == 14: key_right(app, instance, next, prev)
    if keycode == 80 or keycode == 13: key_left(app, instance, next, prev)
    if keycode == 81 or keycode == 12: key_down(app, instance, next, prev)
    if keycode == 82 or keycode == 11: key_up(app, instance, next, prev)


def key_up(app, instance=None, next=None, prev=None):
    if app.current_on_focus:
        if app.current_on_focus.focus == False:
            app.current_on_focus = None
    if not app.current_on_focus:
        if app.current_list == "RM":
            if prev:
                instance.fcb(prev)
                app.list_focus[app.current_list] = prev
                app.current_focused = prev
        elif app.current_list == "OSV1" or app.current_list == "OSV2" or app.current_list == "OSV3":
            if instance == app.items[app.current_list][0]:
                app.current_list = "OSV0"
                app.current_focused = app.list_focus[app.current_list]
                instance.fcb(app.current_focused)
                if app.current_sub:
                    app.current_sub.fcb()
                    app.current_sub = None
            elif prev:
                instance.fcb(prev)
                app.list_focus[app.current_list] = prev
                app.current_focused = prev
                if app.current_sub:
                    app.current_sub.fcb()
                    app.current_sub = None
        elif app.current_list == "MSV2" or app.current_list == "MSV3":
            if instance == app.items[app.current_list][len(app.items[app.current_list])-1]:
                app.current_list = "MSV1"
                app.current_focused = app.list_focus[app.current_list]
                instance.fcb(app.current_focused)
            elif next:
                prev = next
                instance.fcb(prev)
                app.current_focused = prev
        elif app.current_list == "XSV1":
            app.current_list = "XSV0"
            app.current_focused = app.list_focus[app.current_list]
            instance.fcb(app.current_focused)
    pass


def key_down(app, instance=None, next=None, prev=None):
    if app.current_on_focus:
        if app.current_on_focus.focus == False:
            app.current_on_focus = None
    if not app.current_on_focus:
        if app.current_list == "MSV1":
            if len(app.items["MSV2"]) > 0 or len(app.items["MSV3"]) > 0:
                if len(app.items["MSV2"]) > 0: app.current_list = "MSV2"
                else: app.current_list = "MSV3"
                app.list_focus[app.current_list] = app.items[app.current_list][len(app.items[app.current_list])-1]
                app.current_focused = app.list_focus[app.current_list]
                instance.fcb(app.current_focused)
        elif app.current_list == "OSV0":
            app.current_list = app.current_segment
            app.current_focused = app.list_focus[app.current_list]
            instance.fcb(app.current_focused)
            if app.current_focused.parent.height - app.current_focused.parent.parent.height > 0:
                app.current_focused.parent.parent.scroll_y = 1
        elif app.current_list == "XSV0":
            if len(app.items["XSV1"]) > 0:
                app.current_list = "XSV1"
                app.current_focused = app.list_focus[app.current_list]
                instance.fcb(app.current_focused)
        else:
            if app.current_list == "MSV2" or app.current_list == "MSV3":
                next = prev
            if next:
                instance.fcb(next)
                app.list_focus[app.current_list] = next
                app.current_focused = next
                if app.current_sub:
                    app.current_sub.fcb()
                    app.current_sub = None
    pass


def key_left(app, instance=None, next=None, prev=None):
    if app.current_on_focus:
        if app.current_on_focus.focus == False:
            app.current_on_focus = None
    if not app.current_on_focus:
        if app.current_list == "MSV1":
            if instance == app.items[app.current_list][len(app.items[app.current_list])-1]:
                app.current_list = "RM"
                app.current_focused = app.list_focus[app.current_list]
                instance.fcb(app.current_focused)
            else:
                prev = next
                instance.fcb(prev)
                app.current_focused = prev
        elif app.current_list == "XSV1":
            if instance == app.items[app.current_list][len(app.items[app.current_list])-1]:
                app.current_list = "RM"
                app.current_focused = app.list_focus[app.current_list]
                instance.fcb(app.current_focused)
            else:
                prev = next
                instance.fcb(prev)
                app.current_focused = prev
        elif app.current_list == "OSV0":
            if instance == app.items[app.current_list][0]:
                app.current_list = "RM"
                app.current_focused = app.list_focus[app.current_list]
                instance.fcb(app.current_focused)
            elif prev:
                instance.fcb(prev)
                app.list_focus[app.current_list] = prev
                app.current_focused = prev
        elif app.current_list == "XSV0":
            app.current_list = "RM"
            app.current_focused = app.list_focus[app.current_list]
            instance.fcb(app.current_focused)
        else:
            if app.current_list == "MSV2" or app.current_list == "OSV1" or app.current_list == "OSV2" or app.current_list == "OSV3": app.current_list = "RM"
            elif app.current_list == "MSV3" and len(app.items["MSV2"]) > 0: app.current_list = "MSV2"
            elif app.current_list == "MSV3": app.current_list = "RM"
            app.current_focused = app.list_focus[app.current_list]
            instance.fcb(app.current_focused)
            if app.current_sub:
                app.current_sub.fcb()
                app.current_sub = None


def key_right(app, instance=None, next=None, prev=None):
    if app.current_on_focus:
        if app.current_on_focus.focus == False:
            app.current_on_focus = None
    if not app.current_on_focus:
        if app.current_list == "RM" or app.current_list == "MSV2":
            if app.current_list == "RM":
                if app.sm.current == 'main':
                    app.current_list = "MSV1"
                    app.list_focus[app.current_list] = app.items[app.current_list][len(app.items[app.current_list])-1]
                if app.sm.current == 'options':
                    app.current_list = "OSV0"
                    app.list_focus[app.current_list] = app.items[app.current_list][0]
                if app.sm.current == 'xstream':
                    app.current_list = "XSV0"
                    app.list_focus[app.current_list] = app.items[app.current_list][0]
            if app.current_list == "MSV2":
                if len(app.items["MSV3"]) > 0:
                    app.current_list = "MSV3"
                    app.list_focus[app.current_list] = app.items[app.current_list][len(app.items[app.current_list])-1]
            app.current_focused = app.list_focus[app.current_list]
            instance.fcb(app.current_focused)
        elif app.current_list == "MSV1":
            next = prev
            instance.fcb(next)
            app.current_focused = next
        elif app.current_list == "XSV1":
            next = prev
            instance.fcb(next)
            app.current_focused = next
        elif app.current_list == "OSV0":
            if next:
                instance.fcb(next)
                app.list_focus[app.current_list] = next
                app.current_focused = next
        elif "action" in instance.ids:
            if len(instance.ids.action.children) == 2:
                if not app.current_sub == instance.ids.action.children[0] and not app.current_sub == instance.ids.action.children[1]:
                    if app.current_sub:
                        app.current_sub.fcb()
                    app.current_sub = instance.ids.action.children[1]
                    app.current_sub.fcb()
                elif app.current_sub == instance.ids.action.children[0]:
                    app.current_sub.fcb()
                    app.current_sub = instance.ids.action.children[1]
                    app.current_sub.fcb()
                elif app.current_sub == instance.ids.action.children[1]:
                    app.current_sub.fcb()
                    app.current_sub = instance.ids.action.children[0]
                    app.current_sub.fcb()
    pass


def key_enter(app, instance=None, next=None, prev=None):
    if app.current_on_focus:
        if app.current_on_focus.focus == False:
            app.current_on_focus = None
    if not app.current_on_focus:
        if instance:
            if app.current_list == "RM":
                for i in range(0, len(app.screen_names)):
                    if instance == app.items["RM"][i]:
                        if not app.screen_names[i] == "exit":
                            app.sm.current = (app.screen_names[i])
                        else: app.exit()
            elif "OSV0I" in str(instance.__class__):
                instance.parent.mark_item(instance)
            elif "XSV1SC" in str(instance.__class__):
                icon = instance.children[1].children[0].ids.icon
                key = instance.key
                if icon.icon == "star-outline":
                    app.callback('do_search', key)
                    icon.icon = "star"
            if "action" in instance.ids:
                if len(instance.ids.action.children) == 2:
                    if not app.current_sub == instance.ids.action.children[0] and not app.current_sub == instance.ids.action.children[1]:
                        if app.current_sub:
                            app.current_sub.fcb()
                        app.current_sub = instance.ids.action.children[1]
                        instance.ids.action.children[1].fcb()
                    elif app.current_sub == instance.ids.action.children[0]:
                        if instance.ids.action.children[0].active: instance.ids.action.children[0].active = False
                        else: instance.ids.action.children[0].active = True
                    elif app.current_sub == instance.ids.action.children[1]:
                        if instance.ids.action.children[1].active: instance.ids.action.children[1].active = False
                        else: instance.ids.action.children[1].active = True
                elif len(instance.ids.action.children) > 0:
                    if "SW" in str(instance.ids.action.children[0].__class__):
                        if instance.ids.action.children[0].active:
                            instance.ids.action.children[0].active = False
                            instance.ids.action.children[0].cb()
                        else:
                            instance.ids.action.children[0].active = True
                            instance.ids.action.children[0].cb()
                    if "SB" in str(instance.ids.action.children[0].__class__):
                        instance.ids.action.children[0].press()
                    if "TF" in str(instance.ids.action.children[0].__class__):
                        app.current_on_focus = instance.ids.action.children[0]
                        instance.ids.action.children[0].focus = True
    pass


def key_space(app, instance=None, next=None, prev=None):
    widget = Factory.MSV1I()
    action = Factory.MSW()
    widget.ids.action.add_widget(action)
    children = []
    if len(app.screens['main'].ids.gl1.children) > 0:
        for child in app.screens['main'].ids.gl1.children:
            children.insert(0, child)
    app.screens['main'].ids.gl1.clear_widgets()
    app.screens['main'].ids.gl1.add_widget(widget)
    if len(children) > 0:
        for child in children:
            app.screens['main'].ids.gl1.add_widget(child)

    widget = Factory.MSV3I2()
    children = []
    x = 0
    if len(app.screens['main'].ids.list3.children) > 0:
        for child in app.screens['main'].ids.list3.children:
            children.insert(0, child)
            x += 1
    widget.text1 = 'text' + str(x)
    widget.text2 = 'info' + str(x)
    app.screens['main'].ids.list3.clear_widgets()
    app.screens['main'].ids.list3.add_widget(widget)
    if len(children) > 0:
        for child in children:
            app.screens['main'].ids.list3.add_widget(child)
    pass


def key_m(app, instance=None, next=None, prev=None):
    #print(app.screens['main'].ids.gl1.children[0].key)
    print(app.screens['main'].ids.gl1.children[0].ids.action.children[0].key)
    #if instance:
        #print(instance, instance.children[1], instance.children[1].children[0], instance.children[1].children[0].ids.icon.icon, instance.width, instance.height)
    pass


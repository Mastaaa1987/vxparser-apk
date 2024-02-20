import importlib
from .view.root.root import RootScreen
from .view.main.main import MainScreen
from .view.xstream.xstream import XstreamScreen
from .view.options.options import OptionScreen

root_screen = { "name": "root", "screen_name": "RootScreen", "kv": "screens/view/root/root.kv" }
screens = [ { "name": "main", "screen_name": "MainScreen", "kv": "screens/view/main/main.kv" }, { "name": "xstream", "screen_name": "XstreamScreen", "kv": "screens/view/xstream/xstream.kv" }, { "name": "options", "screen_name": "OptionScreen", "kv": "screens/view/options/options.kv" } ]

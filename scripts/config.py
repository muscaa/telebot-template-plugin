from utils.package import *
from utils import platform as p

NAME: str = "telebot-template-plugin"

PACKAGE_LIBRARIES: list[Lib] = [
]
PACKAGE_OTHER: list[File] = [
    File("LICENSE"),
    File("NOTICE"),
]
PLUGIN_JSON: dict = {
    "name": NAME,
    "author": "muscaa",
    "version": "1.0.0",
    "plugin_lib": NAME,
    "plugin_main": "ttp::main"
}

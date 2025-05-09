from utils.package import *
from utils import platform as p

NAME: str = "telebot-template-plugin"

PACKAGE_LIBRARIES: list[Lib] = [
]
PACKAGE_OTHER: list[File] = [
    File("plugin.json"),
    File("LICENSE"),
    File("NOTICE"),
]

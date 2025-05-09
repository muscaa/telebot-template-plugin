from utils.package import *
from utils import platform as p

NAME: str = "telebot-template-plugin"

PACKAGE_LIBRARIES: list[Lib] = [
    Lib(f"lib{NAME}", path_to=f"plugin-{p.SYSTEM}-{p.ARCH}", platforms=[p.LINUX, p.MACOS]),
    Lib(NAME, path_to=f"plugin-{p.SYSTEM}-{p.ARCH}", platforms=[p.WINDOWS]),
]
PACKAGE_OTHER: list[File] = [
    File("plugin.json"),
    File("LICENSE"),
    File("NOTICE"),
]

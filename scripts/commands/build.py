import subprocess
import os

import config
from commands import init
from utils import project

def build():
    init.init()

    print("Building...")

    subprocess.run(["cmake", "--preset", f"{project.get_triplet()}"])
    subprocess.run(["cmake", "--build", "--preset", f"{project.get_triplet()}"])

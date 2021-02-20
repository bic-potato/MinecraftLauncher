import json
import os

with open("bin/path.json", mode="w+")as f:
    path = os.path.abspath("main.py")
    json.dump({"launcher_path": path}, f)

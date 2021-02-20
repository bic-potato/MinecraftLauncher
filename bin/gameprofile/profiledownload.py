import json
import os
from urllib.request import urlretrieve
import gamelocation
from shutil import copyfile

class Library(gamelocation.Profile):
    def __init__(self):
        gamelocation.Profile.__init__(self)
        self.object_index_path = f"{self.game_path}/assets/indexes/"
        self.object_path = f"{self.game_path}/assets/objects/"

    def objectdownload(self, version):
        with open(f"{self.object_index_path}{version}.json") as f:
            for i in json.load(f)["object"]:
                hash = i['hash']
                if not os.path.isfile(f"{self.object_path}/{hash[0,2]}/{hash}"):
                    urlretrieve(url=f"http://resources.download.minecraft.net/{hash[0,2]}/{hash}",
                                filename=f"{self.object_path}/{hash[0,2]}/{hash}", reporthook=None, data=None)
                copyfile(f"{self.object_path}/{hash[0,2]}/{hash}", f"{self.game_path}assets/virtual/legacy/{hash[0,2]}/{hash}")


library = Library()
library.objectdownload(1.16)
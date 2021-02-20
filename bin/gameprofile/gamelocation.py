import json
import os
import sys
from urllib.request import urlretrieve


def get_filelist(dir):
    appendix = []
    for dirs in os.walk(dir):
        appendix.extend(dirs[1])
        return appendix


class Profile:
    def __init__(self):
        self.game_path = self.get_GamePATH
        # self.launcher_path = self.get_launcher_path

    @property
    def get_Gamelist(self):
        try:
            os.remove("../../lib/version_manifest.json")
            urlretrieve(url="https://launchermeta.mojang.com/mc/game/version_manifest.json",
                        filename="../../lib/version_manifest.json", reporthook=None, data=None)
        except FileNotFoundError:
            urlretrieve(url="https://launchermeta.mojang.com/mc/game/version_manifest.json",
                        filename="../../lib/version_manifest.json", reporthook=None, data=None)
        with open("../../lib/version_manifest.json") as f:
            gamelist = json.load(f)
        return gamelist

    # def cratepath():
    #     path={"linux":"~/.minecraft","windows":"%APPDATA%\.minecraft","darwin":"~/.minecraft"}
    #     file="./lib/default_game_path.json"
    #     with open(file, mode='w') as f:
    #         json.dump(path, f)
    @property
    def get_GamePATH(self):
        try:
            with open("game_path.json") as f:
                gamePATH = json.load(f)
            return gamePATH['PATH']
        except FileNotFoundError:
            with open("../../lib/default_game_path.json") as f:
                gamePATH = json.load(f)
                return gamePATH[sys.platform]

    @property
    def get_LocalGameVersionList(self):
        gamelist = get_filelist(str(self.game_path) + "/versions/")
        print(gamelist)

    # @property
    # def get_launcher_path(self):
    #     with open("../../bin1/path.json") as f:
    #         return json.load(f)["launcher_path"]

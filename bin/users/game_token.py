import json
from bin.gameprofile.gamelocation import Profile


class Token():
    def __init__(self):
        self.path = Profile.get_GamePATH
        self.client_token
        self.access_token

    @property
    def IsClientToken_exists(self):
        try:
            with open(str(self.path) + "/launcher_profiles.json") as f:
                launcher_profiles = json.load(f)
                if "clientToken" in launcher_profiles:
                    return True
                else:
                    return False
        except FileNotFoundError:
            return False

    @property
    def get_ClientToken(self):
        with open(str(self.path) + "/launcher_profiles.json") as f:
            launcher_profiles = json.load(f)
            return launcher_profiles["clientToken"]

import json
import lib.requests
from bin.users.game_token import Token


class MojangLogin(Token):
    def __init__(self):
        Token.__init__(self)

    def mojang_login(self, id, password):
        """
        :param id: Mojang account
        :param password: Mojang account password
        :return: user_profiles
        """
        if self.IsClientToken_exists:
            login_post = {"agent": {"name": "Minecraft", "version": 1}, "username": id, "password": password,
                          "clientToken": str(self.get_ClientToken)}
        else:
            login_post = {"agent": {"name": "Minecraft", "version": 1}, "username": id, "password": password}
            url = "https://authserver.mojang.com/authenticate"
            header = {"Content-Type": "application/json"}
            login_response = requests.post(url=url, headers=header, data=json.dumps(login_post))
            repeat = login_response.json()
            if login_response == 200:
                self.access_token = repeat["accessToken"]
                self.cilent_token = repeat["clientToken"]
                return repeat["availableProfiles"]
            else:
                return repeat

    @property
    def IsaccessToken_vaild(self):
        """
        check whether accessToken is valid
        :return: Boolean
        """
        if self.IsClientToken_exists or self.access_token != None:
            valid_post = {"accessToken": str(self.access_token),
                          "clientToken": str(self.get_ClientToken)}
        else:
            valid_post = {"accessToken": str(self.access_token), }
        url = "https://authserver.mojang.com/validate"
        header = {"Content-Type": "application/json"}
        login_response = lib.requests.post(url=url, headers=header, data=json.dumps(valid_post))
        if login_response == 204:
            return True
        else:
            return False

    @property
    def refreshToken(self):
        refresh_post = {{"accessToken": str(self.access_token), "clientToken": str(self.cilent_token)}}
        header = {"Content-Type": "application/json"}
        login_response = lib.requests.post(url=url, headers=header, data=json.dumps(refresh_post))
        response = login_response.json()
        self.access_token = response["accessToken"]
        self.cilent_token = response["cilent_token"]
        return response["availableProfiles"]

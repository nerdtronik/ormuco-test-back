import requests


class Nova(object):
    def __init__(self, id: str):
        self.__id = id

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, value) -> None:
        self.__id = value

    def getServerList(self, token: str, detailed: str = "false", version: str = "2.1") -> list:
        headers = {"Content-Type": "application/json",
                   "X-Auth-Token": token}
        url = f"https://api-acloud.ormuco.com:8774/v{version}/{self.id}/servers"
        if detailed == "true":
            url += "/detail"
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        return r.json()["servers"]

    def getFlavorList(self, token: str, detailed: str = "false", version: str = "2.1") -> list:
        headers = {"Content-Type": "application/json",
                   "X-Auth-Token": token}
        url = f"https://api-acloud.ormuco.com:8774/v{version}/{self.id}/flavors"
        if detailed == "true":
            url += "/detail"
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        return r.json()["flavors"]

    def createServer(self, token: str, name: str, keyPair: str, networks, flavor: str, image: str, version: str = "2") -> dict:
        headers = {"Content-Type": "application/json",
                   "X-Auth-Token": token}
        url = f"https://api-acloud.ormuco.com:8774/v{version}/{self.id}/servers"
        body = {
            "server": {
                "name": name,
                "flavorRef": flavor,
                "networks": networks,
                "key_name": keyPair,
                "imageRef": image
            }
        }
        print(body)
        r = requests.post(url, headers=headers, json=body)
        r.raise_for_status()
        return r.json()["server"]

    def getKeypairsList(self, token: str, version: str = "2.1") -> list:
        headers = {"Content-Type": "application/json",
                   "X-Auth-Token": token}
        url = f"https://api-acloud.ormuco.com:8774/v{version}/{self.id}/os-keypairs"
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        return r.json()["keypairs"]

    def createKeypair(self, token: str, name: str, version: str = "2.1") -> dict:
        headers = {"Content-Type": "application/json",
                   "X-Auth-Token": token}
        url = f"https://api-acloud.ormuco.com:8774/v{version}/{self.id}/os-keypairs"
        body = {
            "keypair": {
                "name": name
            }
        }
        r = requests.post(url, headers=headers, json=body)
        r.raise_for_status()
        return r.json()["keypair"]

    def getNetworkList(self, token: str) -> list:
        headers = {"Content-Type": "application/json",
                   "X-Auth-Token": token}
        url = f"https://api-acloud.ormuco.com:9696/v2.0/networks"
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        return r.json()["networks"]

    def getImageList(self, token: str, version: str = "2.1") -> list:
        headers = {"Content-Type": "application/json",
                   "X-Auth-Token": token}
        url = f"https://api-acloud.ormuco.com:8774/v{version}/{self.id}/images"
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        return r.json()["images"]

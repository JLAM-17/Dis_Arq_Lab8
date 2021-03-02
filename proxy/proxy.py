import requests


class Proxy:
    def __init__(self, instance):
        self.instance = instance

    def proxy(self):
        object_instance = self.instance
        if object_instance.numero % 2 == 0:
            response = requests.get(
                f"https://restcountries.eu/rest/v2/region/asia")
            print(response.content.decode('utf-8'))
            return True
        response = requests.get(
            f"https://restcountries.eu/rest/v2/region/americas")
        print(response.content.decode('utf-8'))

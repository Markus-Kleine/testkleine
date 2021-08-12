import requests

class CocktailAPI:
    def __init__(self):
        self.url="https://thecocktaildb.com/api/json/v1"
    def get_cocktails(self, cocktailname):
        cocktail = requests.get(self.url + '/1/search.php?s=' + cocktailname)
        return cocktail.json()["drinks"]


class ArtdetAPI:
    def __init__(self):
        self.url="https://soadigital.zedach.eu:1443/kds/api?"
    def get_artikel(self, artikelnr):
        artdet = requests.get(self.url + 'service=GETARTDETAIL&customer=KDS&apikey=35A44QQ95IRAIFH20210809102218&matnr=' + artikelnr)
        return artdet.json()




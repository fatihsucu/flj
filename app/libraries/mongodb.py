"""
Bu modul mongodb veritabani icin gerekli baglanti nesnesini
(connection resource) verir. Ayrica mongodb veritabaniyla
ilgili yardimci metodlari da icerir.

config(dict) parametresindeki mongoURI direktifini kullanarak
bir mongodb veritabani(database) nesnesi dondurur. Dikkat:
pymongo.connection degil, pymongo.database dondurur.
"""

from pymongo import MongoClient

# yeni veritabani baglantisi olusturulurken eger config verilmediyse bu
# varsayilan olan kullanilir.
DEFAULT_CONFIG = None

# singleton database nesnesi. getDB() tarafindan olusturulur ve yonetilir.
DATABASE = None


def setDefaultConfig(config):
    """
    varsayilan veritabani baglanti konfigurasyonunu belirler.
    """
    global DEFAULT_CONFIG
    DEFAULT_CONFIG = config


def getDb(config=None, force=False):
    """
    verilen config'i kullanarak pymongo.database nesnesi dondurur.

    Ornek kullanim:

    from libraries import mongodb
    db = mongodb.getDb(config)

    Ikinci kez cagrildiginda ilk seferde olusturulan baglanti kullanilir,
    dolayisiyla config vermeyere gerek kalmaz.
    db2 = mongodb.getDb()
    Bu durumda db ile db2 birebir aynidir.

    Eger force argumani true ise mevcut baglanti olsa bile bir
    yenisi olusturularak bu baglanti dondurulur.
    db3 = mongodb.getDb(anotherConfig, force=True)
    Bu durumda db ve db2 ayni iken db3 farklidir.
    """

    # eger database nesnesi zaten uretilmisse yenisini uretmek yerine
    # bunu kullan.
    global DATABASE
    global DEFAULT_CONFIG

    if not force and DATABASE:
        return DATABASE

    if not config and not DEFAULT_CONFIG:
        raise TypeError('while invoking getDb(), config is missing and \
            default config is not set')

    config = config or DEFAULT_CONFIG

    try:
        client = MongoClient(config.MONGODB_URI)
        DATABASE = client[config.MONGODB_DATABASENAME]
    except Exception as error:
        raise error

    return DATABASE

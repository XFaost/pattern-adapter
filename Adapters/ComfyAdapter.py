from IStore import IStore, IncorrectUrlError
from Stores.Comfy import Comfy


class ComfyAdapter(IStore):

    def __init__(self):
        self.__comfy = Comfy()
        self.__store_name = 'Comfy'

    def __check_domain(self, url):
        return 'comfy.ua' in url

    def __get_path_from_url(self, url: str) -> str:
        return url.replace('https://', '').replace('www.', '').replace('comfy.ua', '')

    def get_store_name(self):
        return self.__store_name

    def get_product_price(self, url):
        # ...
        if self.__check_domain(url):
            path = self.__get_path_from_url(url)
            return self.__comfy.get_price(path)
        else:
            raise IncorrectUrlError(self.get_store_name())

    def get_product_data(self, url):
        # ...
        if self.__check_domain(url):
            path = self.__get_path_from_url(url)
            return self.__comfy.get_product_data(path)
        else:
            raise IncorrectUrlError(self.get_store_name())
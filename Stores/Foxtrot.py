from IStore import IStore, IncorrectUrlError


class Foxtrot(IStore):

    def __init__(self):
        self.__store_name = 'Foxtrot'

    def __check_domain(self, url):
        return 'foxtrot.com.ua' in url

    def get_store_name(self):
        return self.__store_name

    def get_product_price(self, url):
        # ...
        if self.__check_domain(url):
            return 12000.0
        else:
            raise IncorrectUrlError(self.get_store_name())

    def get_product_data(self, url):
        # ...
        if self.__check_domain(url):
            return {
                'name': 'SAMSUNG SM-A725F Galaxy A72 6/128 Duos ZKD Black',
                'price': 15000.0,
                'memory': 128,
                'ram': 6,
                'screen_diagonal': 6.7,
                'display': 'SUPER AMOLED',
                'battery': 5000
            }
        else:
            raise IncorrectUrlError(self.get_store_name())
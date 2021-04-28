class Comfy:

    def __init__(self):
        self.__site_url = 'comfy.ua'

    def get_site_url(self):
        return self.__site_url

    def get_price(self, path) -> float:
        # ...
        return 10500.0

    def get_product_data(self, path) -> dict:
        # ...
        return {
            'name': 'SAMSUNG SM-A725F Galaxy A72 6/128 Duos ZKD Black',
            'price': 13500.0,
            'memory': 128,
            'ram': 6,
            'screen_diagonal': 6.7,
            'display': 'SUPER AMOLED',
            'battery': 5000
        }
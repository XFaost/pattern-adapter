class IncorrectUrlError(Exception):

    def __init__(self, store_name: str):
        self.message = 'Incorrect url in ' + store_name
        super().__init__(self.message)


class IStore:

    def get_store_name(self) -> str:
        pass

    def get_product_price(self, url: str) -> float:
        pass

    def get_product_data(self, url: str) -> dict:
        pass

    def __check_domain(self, url: str) -> bool:
        pass

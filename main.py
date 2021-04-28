from Adapters.ComfyAdapter import ComfyAdapter
from Stores.Eldorado import Eldorado
from Stores.Foxtrot import Foxtrot

if __name__ == '__main__':
    eldorado = Eldorado()
    foxtrot = Foxtrot()
    comfy = ComfyAdapter()

    product = {
        'eldorado': 'https://eldorado.ua/smartfon-samsung-galaxy-a32-464-gb-black-sm-a325-fzkdsek-/p71321561/?utm_content=smartphony&gclid=CjwKCAjwj6SEBhAOEiwAvFRuKCaQbrjIKrjXGHectknyfKo0wF58azu70RlISdB76Vtnt8NdE9Er1RoCF8AQAvD_BwE',
        'foxtrot': 'https://www.foxtrot.com.ua/uk/shop/mobilnye_telefony_samsung_sm-a325f-galaxy-a32-4-64-duos-zkd-black.html',
        'comfy': 'https://comfy.ua/ua/smartfon-samsung-galaxy-a32-4-64gb-black-sm-a325flkdsek.html',
    }

    print(eldorado.get_product_price(product['eldorado']))
    print(foxtrot.get_product_price(product['foxtrot']))
    print(comfy.get_product_price(product['comfy']))

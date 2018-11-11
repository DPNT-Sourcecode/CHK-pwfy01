class Product(object):
    products_list = [
        {
            "sku": "A",
            "price": 50,
            "offer_id": [1]
        },
        {
            "sku": "B",
            "price": 50,
            "offer_id": [2]
        }
    ]

    def __init__(self, sku):
        self.sku = sku

    def is_available(self):
        if any(product.get('sku') == self.sku for product in self.products_list):
            return True
        return False

    def get_product(self):
        if self.is_available():
            for idx, product in enumerate(self.products_list):
                if self.sku == product.get('sku'):
                    return [self.products_list[idx]]
        return []

    def on_offer(self):
        if self.is_available() and self.get_product()[0]['offer_id']:
            return True
        return False


class Offer(object):
    offers_list = [
        {
            "offer_id": 1,
            "quantity": 3,
            "price": 130
        },
        {
            "offer_id": 2,
            "quantity": 2,
            "price": 45
        }
    ]

    def __init__(self, id):
        self.id = id

    def is_available(self):
        pass

    def get_offer(self):
        pass


class Basket(object):
    def __init__(self, skus, products=None):
        self.skus = skus
        self.products = products if products else []

    def is_valid(self):
        pass


def checkout(skus):
    raise NotImplementedError()

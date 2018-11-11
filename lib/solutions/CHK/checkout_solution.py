import itertools


class Product(object):
    products_list = [
        {
            "sku": "A",
            "price": 50,
            "offer_id": [1, 4]
        },
        {
            "sku": "B",
            "price": 30,
            "offer_id": [2]
        },
        {
            "sku": "C",
            "price": 20,
            "offer_id": []
        },
        {
            "sku": "D",
            "price": 15,
            "offer_id": []
        },
        {
            "sku": "E",
            "price": 40,
            "offer_id": [3]
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
        },
        {
            "offer_id": 3,
            "quantity": 2,
            "price": 0,
            "sku": "B",
            "sku_quantity": 1
        },
        {
            "offer_id": 4,
            "quantity": 5,
            "price": 200
        },
    ]

    def __init__(self, id):
        self.id = id

    def is_available(self):
        if any(offer.get('offer_id') == self.id for offer in self.offers_list):
            return True
        return False

    def get_offer(self):
        if self.is_available():
            for idx, offer in enumerate(self.offers_list):
                if self.id == offer.get('offer_id'):
                    return [self.offers_list[idx]]
        return []


class Basket(object):
    def __init__(self, skus, products=None):
        self.skus = skus
        self.products = products if products else []

    def is_valid(self):
        if all(sku.isalpha() for sku in self.skus) or not self.skus:
            return True
        return False

    def clean(self):
        applied_offers = []
        for prod_id in self.skus:
            product = Product(prod_id).get_product()[0]

            offers = product.get('offer_id')
            for offer_id in offers:
                offer = Offer(offer_id).get_offer()[0]
                if not offer.get('price') and offer_id not in applied_offers:
                    prd_for_free = offer.get('sku')
                    prd_qnty = offer.get('quantity')
                    quo, rem = divmod(self.skus.count(product.get('sku')), prd_qnty)
                    self.skus = self.skus.replace(prd_for_free, '', quo * offer.get('sku_quantity'))
                applied_offers.append(offer_id)

        return self.skus


def checkout(skus):
    skus_list = ''.join(sorted(skus))
    basket = Basket(skus_list)
    if not basket.is_valid():
        return -1

    for sku in skus_list:
        if Product(sku).is_available():
            basket.products.append(Product(sku))
        else:
            return -1

    product_groups = []
    for sku, group in itertools.groupby(basket.products, key=lambda x: x.get_product()[0].get('sku')):
        product_groups.append((sku, len(list(group))))

    total = 0

    for group in product_groups:
        prd = Product(group[0])
        prd_price = prd.get_product()[0].get('price')
        if prd.on_offer():
            offer_ids = prd.get_product()[0].get('offer_id')
            cart = group[1]
            for offer_id in offer_ids:
                offer = Offer(offer_id).get_offer()[0]
                offer_qnty = offer.get('quantity')
                price = offer.get('price')
                if price:
                    quo, rem = divmod(cart, offer_qnty)
                    total += quo * price
                    if quo != 0:
                        cart -= offer_qnty * quo
            total += cart * prd_price

        else:
            total += group[1] * prd_price

    return total

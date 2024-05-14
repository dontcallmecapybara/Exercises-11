import json


class Load:
    '''
    A class used to load data from JSON files.
    '''
    with open('country.json', 'r', encoding='utf-8') as f:
        countries = json.load(f)
    
    with open('producer.json', 'r', encoding='utf-8') as f:
        producers = json.load(f)
    
    with open('product.json', 'r', encoding='utf-8') as f:
        products = json.load(f)


class Product:
    '''
    A class used to represent a Product.

    Attributes
    ----------
    products (list): List with product and information about it.

    Parameters
    ----------
    barcode (str): Barcode which condiders information about product, producer and country.
    price (int): Price of product.
    '''

    products = []

    def __init__(self, barcode, price):
        self.__barcode = barcode
        self.__country = Load.countries[barcode[:3]]
        self.__producer = Load.producers[barcode[3:7]]
        self.__product = Load.products[barcode[7:12]]
        self.__price = price
        Product.products.append((self.__product, self.__barcode, self.__country, self.__price))

    @property
    def product(self):
        return self.__product

    @property
    def barcode(self):
        return self.__barcode

    @property
    def country(self):
        return self.__country

    @property
    def price(self):
        return self.__price
    
    def __repr__(self):
        return (
            f'----------------------------\n'
            f'Продукт: {self.__product}\n'
            f'Номер штрихкода: {self.__barcode}\n'
            f'Страна: {self.__country}\n'
            f'Производитель: {self.__producer}\n'
            f'Цена: {self.__price}\n'
            f'----------------------------'
        )
    
class ShoppingCart:
    '''
    A class used to represent a Shopping Cart.
    '''


    def __init__(self):
        self.__products = []
        self.__total_price = 0.0

    @property
    def products(self):
        return self.__products

    @property
    def total_price(self):
        return self.__total_price
    
    def add_product(self, product):
        '''
        The method to add a product to the cart.

        Parameters
        -----------
        product (Product): The product to be added.
        '''
        self.__products.append(product)
        self.__total_price += product.price

    def del_product(self, num):
        '''
        The method to delete a product from the cart.

        Parameters:
        num (int): The number of the product to be deleted.
        '''
        price = self.__products[num].price
        self.__products.pop(num)
        self.__total_price -= price

    def view_cart(self):
        '''
        The method to view all products in the cart.
        '''
        result = ''
        for product in self.__products:
            result += (
                f'----------------------------\n'
                f'Номер товара: {self.__products.index(product)}\n'
                f'Название: {product.product}, \n'
                f'Штрих-код: {product.barcode}, \n'
                f'Страна-производитель: {product.country}, \n'
                f'Цена: {product.price}\n'
                f'----------------------------'
            )
        result += f'\nИтого: {self.__total_price} руб'
        return result

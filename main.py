class Product:
    def __init__(self,name,weight,category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name},{self.weight},{self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
    def get_prodocts(self):
        """считывает всю информацыю из файла и возврощает единую строку со всеми товарами."""
        try:
            with open(self.__file_name,'r') as file:
                return file.read()
        except FileNotFoundError:
            return ''
    def __add__(self,*products):
        """Добовляет продукты в файл, есле их еще нет."""
        existing_products = self.get_prodocts()
        with open(self.__file_name,'a') as file:
            for product in products:
                if isinstance(product, Product):
                    if product.name in existing_products:
                        print(f'Продукт {product.name} уже есть в магазине')
                    else:
                        file.write(f'{product}\n')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti',3.4,'Groceries')
p3 = Product('Potato', 5.5,'Vegetables')

print(p2)

s1.__add__(p1,p2,p3)

print(s1.get_prodocts())

import json

class Product:

 all_products = []
 FILE_PATH = 'data/products.json'   

def __init__(self, productId, name, price, stock, category):
        self.id = productId
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

Product.all_products.append(self)

def __repr__(self):
        return f"{self.productId} | {self.name} | KES {self.price} | stock: {self.stock})"

def to_dict(self):
        return {
            'productId': self.productId,
            'name': self.name,
            'price': self.price,
            'stock': self.stock,
            'category': self.category
        }

def safe_to_json(self):
    try:
        with open(self.FILE_PATH, 'w') as file:
            data = json.load(file)
            data.append(self.to_dict())
            
        with open(self.FILE_PATH, 'w') as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print(f"An error occurred while saving the product: {e}") 


@classmethod
def read_all(cls):
    with open(cls.FILE_PATH, 'r') as file:
        data = json.load(file)
    
    return [Product(**item) for item in data]
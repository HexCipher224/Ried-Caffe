import json

FILE_PATH = 'data/products.json'

def load_products():
    with open(FILE_PATH, 'r') as file:
        return json.load(file)
    
def save_product(product):
    with open(FILE_PATH, 'r') as file:
        json.dump(product, file, indent=4)
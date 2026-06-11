from models.products import Product

def list_products():
    products = Product.read_all()
    print("\n--- Product List ---")
    for product in products:
        print(product)


def create_product():
    productId = int(input("Enter product ID: "))
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock quantity: "))
    category = input("Enter product category: ")
    
    product = Product(
        productId,
        name,
        price,
        stock,
        category
    )
    product.save_to_json()
   
    print(f"Product '{name}' created successfully!")


def update_stock():
    productId = int(input("Enter product ID: "))
    new_stock = int(input("Enter new stock: "))
    
    products = Product.read_all()
    for product in products:
        if product.id == productId:
            product.stock = new_stock
    with open(Product.FILE_PATH, 'w') as file:
        import json
        json.dump([p.to_dict() for p in products], file, indent=4)
    
    print("Stock updated successfully!")

def add_product():
    products = {}
    while True:
        product_name = input("Enter name of product(or 'done'to exit):")

        if product_name == "done":
            break
        product_price = eval(input("Enter price:"))
        products[product_name]=product_price
    return products

def find_product(products):
                             while True:
                                name = input("Enter name of product to search(or 'done' to exit):")

                                if name == "done":
                                    break
                                if name in products:
                                    print("Price",products[name])
                                else:
                                    print("Product not found!!!")

product_dict = add_product()
find_product(product_dict)

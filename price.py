def discounted(price, discount, max_discount=50):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError("Очень большая скидка")
    if discount >= max_discount:
        price_whit_discount = price
    else:
        price_whit_discount = price - price * discount / 100
    return price_whit_discount

# product = {"name": "Samsung s10", "stock": 8, "price": 50000.0, "discount": 50}

# product["with_discount"] = discounted(product["price"], product["discount"])

# print(product) 

print(discounted(100, 40))
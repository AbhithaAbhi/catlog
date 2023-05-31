discount_rules = {
    "flat_10_discount": 10,
    "bulk_5_discount": 0.05,
    "bulk_10_discount": 0.1,
    "tiered_50_discount": 0.5
}

products = {
    "product A": 20,
    "product B": 40,
    "product C": 50,
}

subtotal = 0
total_discount = 0
shipping_fee = 0
gift_wrap_fee_total = 0
total_cost = 0
gift_wrap_fee = 1
shipping_fee_per_package = 5
products_per_package = 10
discount_rule = ""
discount_price = 0
product_quantities = {}
gift_wraps = {}

for product in products:
    quantity = int(input(f"Enter quantity for {product}: "))
    product_quantities[product] = quantity

    gift_wrap = input(f"Is {product} wrapped as a gift? (yes/no): ").lower()
    if gift_wrap == "yes":
        gift_wraps[product] = quantity
    else:
        gift_wraps[product] = 0

for product, quantity in product_quantities.items():
    price = products[product]
    product_total = price * quantity
    subtotal += product_total
    total_quantity = sum(product_quantities.values())

    if subtotal > 200 and "flat_10_discount" in discount_rules:
        total_discount = max(total_discount, discount_rules["flat_10_discount"])
        discount_rule = "flat_10_discount"
        discount_price += total_discount

    if "bulk_5_discount" in discount_rules:
        for product, quantity in product_quantities.items():
            if quantity > 10:
                item_discount = products[product] * quantity * discount_rules["bulk_5_discount"]
                total_discount += item_discount
                discount_rule = "bulk_5_discount"
                discount_price += item_discount

    if "bulk_10_discount" in discount_rules and total_quantity > 20:
        bulk_discount = subtotal * discount_rules["bulk_10_discount"]
        total_discount += bulk_discount
        discount_rule = "bulk_10_discount"
        discount_price += bulk_discount

    if "tiered_50_discount" in discount_rules and total_quantity > 30:
        for product, quantity in product_quantities.items():
            if quantity > 15:
                tiered_discount = (quantity - 15) * products[product] * discount_rules["tiered_50_discount"]
                total_discount += tiered_discount
                discount_rule = "tiered_50_discount"
                discount_price += tiered_discount

num_packages = total_quantity // products_per_package
shipping_fee = num_packages * shipping_fee_per_package
gift_wrap_fee_total = gift_wrap_fee * sum(gift_wraps.values())
total_cost = subtotal - total_discount + shipping_fee + gift_wrap_fee_total

print("\n******** Order Summary ********")
for product, quantity in product_quantities.items():
    price = products[product]
    product_total = price * quantity
    print(f"{product}: Quantity: {quantity} - Total: ${product_total}")

print(f"\nTotal Quantity: {total_quantity}")

print(f"Subtotal: ${subtotal}")

if discount_rule:
    print(f"Discount applied ({discount_rule}): ${total_discount}")

print(f"Shipping fee: ${shipping_fee}")
print(f"Gift wrap fee: ${gift_wrap_fee_total}")
print(f"Total: ${total_cost}")

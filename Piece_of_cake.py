def get_recipe_price(prices=None, optionals=None, **args):
    if optionals is None:
        optionals = []

    if prices is None or args is None or len(args) + len(optionals) != len(prices):
        return 0

    sum_prices = 0

    for key, value in prices.items():
        if key not in optionals:
            sum_prices += (args.get(key) // 100) * value
    return sum_prices


d = get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100)
b = get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300)
print(d, b, get_recipe_price())

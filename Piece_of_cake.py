def get_recipe_price(prices, optionals=None, **args):
    """
    This function gets a dictionary (prices), a list (optionals) and the ingredients weight.
    @param prices - A dictionary that include the necessary ingredients (keys) and their prices for 100 gram (values).
    @param optionals - An optional list that include ingredients name to ignore in the recipe.
    @param args - Arguments that indicate the weight of each ingredient in prices.
    """
    if optionals is None:
        optionals = []

    prices_sum = 0

    for key, value in prices.items():
        if key not in optionals:
            prices_sum += (args.get(key) // 100) * value
    return prices_sum


if __name__ == '__main__':
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))

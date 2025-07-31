prices = {
    "Bubblegum": 2,
    "Toffee": 0.2,
    "Ice cream": 5,
    "Milk chocolate": 4,
    "Doughnut": 2.5,
    "Pancake": 3.2,
}


def stage_1(prices):
    print("Prices:")
    print("\n".join([f"{item}: ${price}" for item, price in prices.items()]))


stage_1(prices)

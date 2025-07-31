prices = {
    "Bubblegum": 2,
    "Toffee": 0.2,
    "Ice cream": 5,
    "Milk chocolate": 4,
    "Doughnut": 2.5,
    "Pancake": 3.2,
}

earnings = {
    "Bubblegum": 202,
    "Toffee": 118,
    "Ice cream": 2250,
    "Milk chocolate": 1680,
    "Doughnut": 1075,
    "Pancake": 80,
}


def display_item_and_money(shop_items: dict[str, float]) -> str:
    print("\n".join([f"{item}: ${value}" for item, value in shop_items.items()]))


def stage_1(prices: dict[str, float]):
    print("Prices:")
    display_item_and_money(prices)


def stage_2(earnings: dict[str, float]):
    print("Earned amount:")
    display_item_and_money(earnings)
    income = sum(earnings.values())
    print(f"\nIncome: ${income:.1f}")


stage_2(earnings)

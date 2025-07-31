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


def display_earned_amount(earnings: dict[str, float], income: float):
    print("Earned amount:")

    display_item_and_money(earnings)

    print(f"\nIncome: ${income:.1f}")


def get_income(earnings: dict[str, float]) -> float:
    income = sum(earnings.values())
    return income


def stage_2(earnings: dict[str, float]):
    income = get_income(earnings)
    display_earned_amount(earnings, income)


def stage_3(earnings: dict[str, float]):
    income = get_income(earnings)
    display_earned_amount(earnings, income)

    staff_expenses = int(input("Staff expenses: "))
    other_expenses = int(input("Other expenses: "))
    total_expenses = staff_expenses + other_expenses

    net_income = income - total_expenses
    print(f"Net income: ${net_income}")


if __name__ == "__main__":
    stage_3(earnings)

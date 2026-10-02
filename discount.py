def calculate_discount(total):
    if total < 0:
        raise ValueError("total must be non-negative")
    return total * 5 / 100
def calculate_discount(total):
    
    if total < 0:
        raise ValueError("Total cannot be negative")
    if total < 100:
        return 0
    if total < 500:
        return total * 0.05

    return total * 0.10
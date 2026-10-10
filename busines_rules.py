# Business_rules.py
# Author: Rahim Rozani

APPROVAL_LIMIT = 1000


def calculate_total(price: float, quantity: int) -> float:
    """return total with 7% tax"""
    return price * quantity * 1.07


def requires_review(amount) -> bool:
    """Checks if amount over threshold"""
    return amount > APPROVAL_LIMIT


def get_approval_tier(amount) -> str:
    """Checks where does amount need approval"""
    if amount <= 500:
        return "auto"
    elif amount <= 2000:
        return "manager"
    else:
        return "director"


def apply_discount(price, pct) -> float:
    """Return price after discount. pct is 0-100"""
    return price * (1 - pct / 100)

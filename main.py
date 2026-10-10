from busines_rules import (
    calculate_total,
    requires_review,
    get_approval_tier,
    apply_discount,
)

# add sample inputs
price, qty = 450.0, 3

total = calculate_total(price, qty)
review = requires_review(total)
tier = get_approval_tier(total)
discounted_price = apply_discount(price, 10)

print(f"Total: ${total:.2f}")
print(f"Requires Review: {review}")
print(f"approval Tier: {tier}")
print(f"10% discount: {discounted_price}")

class ItemNotFound(Exception):
    """Raises when item code does not found in price rules configuration"""


class InvalidDiscountType(Exception):
    """Raises when discount type does not matched with available discounts"""
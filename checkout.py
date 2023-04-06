# Packages
import json

# Modules
from discounts import Discounts
from exceptions import ItemNotFound, InvalidDiscountType


class Checkout:
    """
    This class is responsible for checkout process of the
    product purchase.
    """

    def __init__(
            self,
            discounts: Discounts,
            price_rules_file: str
    ):
        self._items = {}
        self._discounts = discounts
        self._price_rules = json.load(open(price_rules_file))

    def scan(self, item_code) -> None:
        """Add item and its increments its count

        Args:
            item_code: item code (e.g. VOUCHER, TSHIRT)

        """
        if not item_code in self._price_rules:
            raise ItemNotFound(f"`{item_code}` not found in price rules")

        if item_code in self._items:
            self._items[item_code] += 1
        else:
            self._items[item_code] = 1

    def _calculate_price_with_discount(
            self,
            item_code: str,
            item_count: int,
            discount_type: str
    ) -> float:
        """Calculates the price of item with respective discount type

        Args:
            item_code: item code
            item_count: number of items
            discount_type: type of discount

        Returns:
            total value of item after applying discount
        """
        item_price_rule = self._price_rules[item_code]
        if discount_type == "two_for_one":
            price = item_price_rule["price"]
            return self._discounts.two_for_one(item_count, price)
        elif discount_type == "bulk":
            price = item_price_rule["price"]
            discount_price = item_price_rule["discount_price"]
            bulk_quantity = item_price_rule["bulk_quantity"]
            return self._discounts.bulk(item_count, price, discount_price, bulk_quantity)
        else:
            raise InvalidDiscountType(f"`{discount_type}` discount type is not available")

    def total(self) -> float:
        """Calculates total price of items including the discounts if there are any

        Returns:
            total price of items
        """
        total_price = 0.0
        for item_code, item_count in self._items.items():
            if not item_code in self._price_rules:
                raise ItemNotFound(f"`{item_code}` not found in price rules")

            item_price = self._price_rules[item_code]["price"]

            if "discount_type" in self._price_rules[item_code]:
                discount_type = self._price_rules[item_code]["discount_type"]
                total_price += self._calculate_price_with_discount(item_code, item_count, discount_type)
            else:
                total_price += (item_price * item_count)

        return float(format(total_price, '.2f'))

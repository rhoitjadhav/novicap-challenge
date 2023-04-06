class Discounts:
    @staticmethod
    def two_for_one(item_count: int, price: float) -> float:
        """Get 2 for the price of 1

        Args:
            item_count: number of items
            price: price of item

        Returns:
            total value of items
        """
        return price * (item_count // 2 + item_count % 2)

    @staticmethod
    def bulk(
            item_count: int,
            price: float,
            discount_price: float,
            bulk_quantity: int = 3
    ) -> float:
        """Get items in bulk with discounted price

        Args:
            item_count:
            price:
            discount_price:
            bulk_quantity:

        Returns:
            total value of items
        """
        if item_count >= bulk_quantity:
            return discount_price * item_count

        return item_count * price

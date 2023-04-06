from checkout import Checkout
from discounts import Discounts


def main():
    checkout = Checkout(Discounts(), "price_rules.json")
    msg = "\nSelect Anyone: \n" \
          "1. VOUCHER\n" \
          "2. TSHIRT\n" \
          "3. MUG\n" \
          "4. JEANS\n" \
          "5. Checkout\n" \
          "--> "
    while True:
        item = input(msg)

        if item == "1":
            checkout.scan("VOUCHER")
        elif item == "2":
            checkout.scan("TSHIRT")
        elif item == "3":
            checkout.scan("MUG")
        elif item == "4":
            checkout.scan("Jeans")
        elif item == "5":
            print("Total:", checkout.total())
            exit(0)
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()

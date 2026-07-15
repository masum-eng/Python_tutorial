from customer import get_customer
from receipt import print_receipt

def main():
    # Get customer data
    name, food, quantity, price, delivery_charges = get_customer()

    # Print the food receipt
    print_receipt(name, food, quantity, price, delivery_charges)

if __name__ == "__main__":
    main()
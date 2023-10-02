def display_menu():
    print("Menu:")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. View current shopping list")
    print("4. Quit")


def add_item(cart):
    item = input("Enter item to add: ")
    quantity = int(input("Enter quantity: "))

    if item in cart:
        cart[item] += quantity
    else:
        cart[item] = quantity


def remove_item(cart):
    item = input("Enter item to remove: ")

    if item in cart:
        quantity = int(input("Enter quantity to remove: "))
        if cart[item] > quantity:
            cart[item] -= quantity
        else:
            del cart[item]
    else:
        print("Item not found in the cart.")


def view_cart(cart):
    print("Current Shopping List:")
    for item, quantity in cart.items():
        print(f"{item}: {quantity}")


def generate_receipt(cart):
    print("Receipt:")
    total = 0
    for item, quantity in cart.items():
        print(f"{item}: {quantity}")
        total += quantity
    print(f"Total items: {total}")


def main():
    cart = {}

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_item(cart)
        elif choice == "2":
            remove_item(cart)
        elif choice == "3":
            view_cart(cart)
        elif choice == "4":
            generate_receipt(cart)
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

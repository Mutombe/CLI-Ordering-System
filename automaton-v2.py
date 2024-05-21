from datetime import datetime

class MenuItem:
    def __init__(self, name, price, order_date, customization_options=None):
        self.name = name
        self.price = price
        self.customization_options = customization_options or []
        self.order_date = order_date

class Menu:
    def __init__(self):
        self.menu_items = {
            "1": MenuItem("Burger", 10, datetime.now, ["Extra Cheese", "Bacon"]),
            "2": MenuItem("Pizza", 12, datetime.now, ["Toppings", "Crust Type"]),
            "3": MenuItem("Salad", 8, datetime.now, ["Dressing", "Add-ons"])
        }

    def display_menu(self):
        print("Menu:")
        for item_number, item in self.menu_items.items():
            print(f"{item_number}. {item.name} - ${item.price}")

    def display_customization_options(self, item_number):
        item = self.menu_items[item_number]
        print(f"Customization options for {item.name}:")
        for option in item.customization_options:
            print(f"- {option}")

class Automaton:
    def __init__(self):
        self.menu = Menu()
        self.order_history = []

    def place_order(self):
        self.menu.display_menu()
        item_number = input("Select item number: ")
        if item_number in self.menu.menu_items:
            item = self.menu.menu_items[item_number]
            print(f"You ordered {item.name} for ${item.price}.")
            self.customize_order(item_number)
            self.process_payment()
            self.order_history.append(item)
            print("Order placed successfully!")
        else:
            print("Invalid item number. Please try again.")

    def customize_order(self, item_number):
        self.menu.display_customization_options(item_number)
        selected_options = []
        item = self.menu.menu_items[item_number]
        print("Customize your order: ")
        for option in item.customization_options:
            user_input = input(f"Do you want to add `{option}`: ")
            selected_options.append(user_input)

        print("Order customization:")
        for option, selection in zip(item.customization_options, selected_options):
            print(f"n\ - {option}: {selection}")

        # You can store the selected options in the item object or in a separate data structure as per your needs
        item.customization_options = selected_options

    def process_payment(self):
        pass
        # Implement payment processing logic here

    def display_order_history(self):
        print("Order History:")
        for item in self.order_history:
            print(f"- {item.name} (${item.price}) {item.order_date()}")

# Usage
automaton = Automaton()
automaton.place_order()
automaton.display_order_history()

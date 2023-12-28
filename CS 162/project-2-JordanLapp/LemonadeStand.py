# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 6/28/2023
# Description: Created classes to represent a lemonade stand, menu items, and track prices.

class MenuItem:
    """Creates a menu item with a name, wholesale cost, and selling price."""

    def __init__(self, name, wholesale_cost, selling_price):
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        """Returns menu item's name."""
        return self._name

    def get_wholesale_cost(self):
        """Returns menu item's wholesale cost."""
        return self._wholesale_cost

    def get_selling_price(self):
        """Returns menu item's selling price."""
        return self._selling_price


class SalesForDay:
    """Keeps track of the sales of every item for a given day."""

    def __init__(self, day, sales_dict=None):
        self._day = day
        if sales_dict:
            self._sales_dict = sales_dict
        else:
            self._sales_dict = {}

    def get_day(self):
        """Returns day of sales."""
        return self._day

    def get_sales_dict(self):
        """Returns dictionary of sales for single day."""
        return self._sales_dict


class InvalidSalesItemError(Exception):
    """Exception raised when sales item is not in menu."""
    pass


class LemonadeStand:
    """Lemonade stand with a name, current day, dictionary of menu items, and list of sales for each day."""

    def __init__(self, name):
        self._name = name
        self._current_day = 0
        self._menu = {}
        self._sales = []

    def get_name(self):
        """Returns the name of the lemonade stand."""
        return self._name

    def get_current_day(self):
        """Returns the current day."""
        return self._current_day

    def get_menu(self):
        """Returns a dictionary of all menu items."""
        return self._menu

    def get_sales(self):
        """Returns a list of sales from every day."""
        return self._sales

    def add_menu_item(self, item):
        """Adds an item to the menu of the stand."""
        name = item.get_name()
        self._menu[name] = item

    def enter_sales_for_today(self, sales):
        """Enters the sales of each menu item for the day."""

        # Check for invalid menu items.
        for name in sales:
            if name not in self._menu:
                raise InvalidSalesItemError

        # Create SalesForDay object with current day and dictionary parameter.
        day = self.get_current_day()
        day_sales = SalesForDay(day, sales)
        self._sales.append(day_sales)

        # Increment day by 1.
        self._current_day += 1

    def sales_of_menu_item_for_day(self, day, item):
        """Returns the quantity sold of a specified item on a given day."""
        day_sales = self._sales[day].get_sales_dict()
        if item in day_sales:
            return day_sales[item]
        else:
            return 0

    def total_sales_for_menu_item(self, item):
        """Returns the total quantity sold of an item for all days."""
        total = 0
        for i in range(len(self._sales)):
            total += self.sales_of_menu_item_for_day(i, item)
        return total

    def total_profit_for_menu_item(self, item):
        """Returns the total profit earned from a single item."""
        sales = self.total_sales_for_menu_item(item)
        cost = self._menu[item].get_wholesale_cost()
        revenue = self._menu[item].get_selling_price()
        profit = sales * (revenue - cost)
        return profit

    def total_profit_for_stand(self):
        """Returns the total profit from all items."""
        total_profit = 0
        for item in self._menu:
            total_profit += self.total_profit_for_menu_item(item)
        return total_profit


def main():
    stand = LemonadeStand("My stand")
    lemonade = MenuItem("Lemonade", 1, 3)
    water = MenuItem("Water", 0.1, 1)
    stand.add_menu_item(lemonade)
    stand.add_menu_item(water)
    day_0_sales = {"Lemonade": 5, "Water": 4, "Cookie": 3}
    try:
        stand.enter_sales_for_today(day_0_sales)
    except InvalidSalesItemError:
        print("There is an item that is not on the menu!")


if __name__ == "__main__":
    main()

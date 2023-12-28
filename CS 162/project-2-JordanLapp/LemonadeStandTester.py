import unittest
import LemonadeStand


class Tests(unittest.TestCase):

    def test_MenuItem(self):
        """Tests initialization of MenuItem object."""
        item = LemonadeStand.MenuItem("Lemonade", 1, 2)
        name = item.get_name()
        wholesale_cost = item.get_wholesale_cost()
        selling_price = item.get_selling_price()

        self.assertEqual("Lemonade", name)
        self.assertAlmostEqual(1, wholesale_cost)
        self.assertAlmostEqual(2, selling_price)

    def test_SalesForDay(self):
        """Tests initialization of SalesForDay object."""
        sales_dict_init = {
            "Lemonade": 5,
            "Water": 3
        }
        sales = LemonadeStand.SalesForDay(0, sales_dict_init)
        no_sales = LemonadeStand.SalesForDay(0)

        sales_day = sales.get_day()
        sales_dict = sales.get_sales_dict()
        sales_empty_dict = no_sales.get_sales_dict()

        self.assertEqual(0, sales_day)
        self.assertEqual(sales_dict["Lemonade"], 5)
        self.assertEqual(sales_empty_dict, {})

    def test_add_menu_item(self):
        item = LemonadeStand.MenuItem("Lemonade", 1, 2)
        stand = LemonadeStand.LemonadeStand("My stand")
        stand.add_menu_item(item)
        name = item.get_name()
        menu = stand.get_menu()

        self.assertIn(name, menu)

    def test_sales_for_day(self):
        item = LemonadeStand.MenuItem("Lemonade", 1, 2)
        stand = LemonadeStand.LemonadeStand("My stand")
        stand.add_menu_item(item)

        # Test for sale of valid item and correct incrementation of current day.
        test_valid = {"Lemonade": 5}
        stand.enter_sales_for_today(test_valid)

        sales_a = LemonadeStand.SalesForDay(0, test_valid)
        sales_a_dict = sales_a.get_sales_dict()
        sales_b = stand.get_sales()
        sales_b_dict = sales_b[0].get_sales_dict()

        day = stand.get_current_day()

        self.assertEqual(sales_a_dict, sales_b_dict)
        self.assertEqual(1, day)

        # Test for InvalidSalesItemError
        test_invalid = {"Lemonade": 5, "Water": 3}

        with self.assertRaises(LemonadeStand.InvalidSalesItemError):
            stand.enter_sales_for_today(test_invalid)

    def test_sales(self):
        stand = LemonadeStand.LemonadeStand("My stand")
        lemonade = LemonadeStand.MenuItem("Lemonade", 1, 3)
        water = LemonadeStand.MenuItem("Water", 0.1, 1)
        stand.add_menu_item(lemonade)
        stand.add_menu_item(water)
        day_0_sales = {"Lemonade": 5}
        day_1_sales = {"Lemonade": 3, "Water": 4}
        stand.enter_sales_for_today(day_0_sales)
        stand.enter_sales_for_today(day_1_sales)

        # Test each function
        self.assertEqual(stand.sales_of_menu_item_for_day(0, "Lemonade"), 5)
        self.assertEqual(stand.sales_of_menu_item_for_day(1, "Lemonade"), 3)
        self.assertEqual(stand.total_sales_for_menu_item("Lemonade"), 8)
        self.assertEqual(stand.total_sales_for_menu_item("Water"), 4)
        self.assertAlmostEqual(stand.total_profit_for_menu_item("Lemonade"), 16)
        self.assertAlmostEqual(stand.total_profit_for_menu_item("Water"), 3.6)
        self.assertAlmostEqual(stand.total_profit_for_stand(), 19.6)


if __name__ == '__main__':
    unittest.main()

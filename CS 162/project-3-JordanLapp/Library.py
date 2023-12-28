# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 7/9/2023
# Description: Library class with LibraryItems and Patrons that can check out or reserve items.

class LibraryItem:
    """Generic library item that tracks various attributes."""
    def __init__(self, identity, title):
        self._library_item_id = identity
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = None

    def get_location(self):
        """Returns the location of the library item."""
        return self._location

    def get_id(self):
        """Returns the id of the library item."""
        return self._library_item_id

    def get_name(self):
        """Returns the name of the library item."""
        return self._title

    def get_checked_out_by(self):
        """Returns the id of the patron checking out the item."""
        return self._checked_out_by

    def get_requested_by(self):
        """Returns the patron requesting the item, or None."""
        return self._requested_by

    def get_date_checked_out(self):
        """Returns date item was checked out."""
        return self._date_checked_out

    def update_checked_out_by(self, patron=None):
        """Updates the item to be checked out by patron, or None."""
        self._checked_out_by = patron
        return

    def update_date_checked_out(self, date):
        """Updates the date the item was checked out."""
        self._date_checked_out = date
        return

    def update_requested_by(self, patron_id=None):
        """Updates the request status of the item."""
        self._requested_by = patron_id
        return

    def location_checked_out(self):
        self._location = "CHECKED_OUT"
        return

    def location_on_shelf(self):
        self._location = "ON_SHELF"
        return

    def location_on_hold_shelf(self):
        self._location = "ON_HOLD_SHELF"
        return


class Book(LibraryItem):
    """Represents a book library item with an author."""
    def __init__(self, identity, title, author):
        LibraryItem.__init__(self, identity, title)
        self._author = author

    def get_author(self):
        """Returns the author of the book."""
        return self._author

    def get_check_out_length(self):
        """Returns the number of days that a book can be check out."""
        return 21


class Album(LibraryItem):
    """Represents an album library item with an artist."""
    def __init__(self, identity, title, artist):
        LibraryItem.__init__(self, identity, title)
        self._artist = artist

    def get_artist(self):
        """Returns the artist of the album."""
        return self._artist

    def get_check_out_length(self):
        """Returns the number of days that an album can be check out."""
        return 14


class Movie(LibraryItem):
    """Represents a movie library item with a director."""
    def __init__(self, identity, title, director):
        LibraryItem.__init__(self, identity, title)
        self._director = director

    def get_director(self):
        """Returns the director of the movie."""
        return self._director

    def get_check_out_length(self):
        """Returns the number of days that a movie can be check out."""
        return 7


class Patron:
    """Represents a patron of a library."""
    def __init__(self, identity, name):
        self._patron_id = identity
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_fine_amount(self):
        """Returns the amount owed by the patron."""
        return self._fine_amount

    def get_id(self):
        """Returns patron's ID."""
        return self._patron_id

    def get_checked_out_items(self):
        """Returns checked out items."""
        return self._checked_out_items

    def add_library_item(self, item):
        """Adds a specified LibraryItem to checked_out_items."""
        self._checked_out_items.append(item)
        return

    def remove_library_item(self, item):
        """Removes a specified LibraryItem from checked_out_items"""
        self._checked_out_items.remove(item)
        return

    def amend_fine(self, fine):
        """Adds or removes an amount to the fine."""
        self._fine_amount += fine
        return


class Library:
    """Represents a library class with various library items used by various patrons."""
    def __init__(self):
        self._holdings = {}
        self._members = {}
        self._current_date = 0

    def get_holdings(self):
        """Returns the dictionary of LibraryItems."""
        return self._holdings

    def add_library_item(self, item):
        """Adds library item to the holdings."""
        item_id = item.get_id()
        self._holdings[item_id] = item

    def add_patron(self, patron):
        """Adds patron to the members."""
        patron_id = patron.get_id()
        self._members[patron_id] = patron

    def lookup_library_item_from_id(self, item_id):
        """Returns library item corresponding to ID."""
        if item_id in self._holdings:
            return self._holdings[item_id]
        return None

    def lookup_patron_from_id(self, patron_id):
        """Returns patron corresponding to ID."""
        if patron_id in self._members:
            return self._members[patron_id]
        return None

    def check_out_library_item(self, patron_id, item_id):
        """Checks out library item for patron if able."""
        # Check Patron is in Library's members
        if patron_id not in self._members:
            return "patron not found"

        # Check LibraryItem is in Library's holdings
        if item_id not in self._holdings:
            return "item not found"

        # Check location of LibraryItem
        item = self._holdings[item_id]
        location = item.get_location()
        if location == "CHECKED_OUT":
            return "item already checked out"
        if location == "ON_HOLD_SHELF":
            request = item.get_requested_by()
            if request != patron_id:
                return "item on hold by other patron"

        # Item is available, update item's and patron's parameters.
        item.update_checked_out_by(patron_id)
        date = self._current_date
        item.update_date_checked_out(date)
        item.update_requested_by()
        patron = self._members[patron_id]
        patron.add_library_item(item)
        item.location_checked_out()
        return "check out successful"

    def return_library_item(self, item_id):
        """Returns an item to the library."""
        # Check LibraryItem is in Library holdings.
        if item_id not in self._holdings:
            return "item not found"

        # Check LibraryItem's location
        item = self._holdings[item_id]
        location = item.get_location()
        if location != "CHECKED_OUT":
            return "item already in library"

        # Update Patron's checked_out_items
        patron_id = item.get_checked_out_by()
        if patron_id not in self._members:
            return "patron not found"
        patron = self._members[patron_id]
        patron.remove_library_item(item)

        # Update Library_Item's location
        request = item.get_requested_by()
        if request:
            item.location_on_hold_shelf()
        else:
            item.location_on_shelf()

        # Update LibraryItem's checked_out_by
        item.update_checked_out_by()
        return "return successful"

    def request_library_item(self, patron_id, item_id):
        """Requests the item for a patron if able."""
        # Check Patron is in Library's members
        if patron_id not in self._members:
            return "patron not found"

        # Check LibraryItem is in Library's holdings
        if item_id not in self._holdings:
            return "item not found"

        # Check if LibraryItem is already requested
        item = self._holdings[item_id]
        request = item.get_requested_by()
        if request:
            return "item already on hold"

        # Update LibraryItem's requested_by
        item.update_requested_by(patron_id)

        # Update LibraryItem's location
        location = item.get_location()
        if location == "ON_SHELF":
            item.location_on_hold_shelf()
        return "request successful"

    def pay_fine(self, patron_id, amount):
        # Check Patron is in Library's members
        if patron_id not in self._members:
            return "patron not found"

        patron = self._members[patron_id]
        patron.amend_fine(-amount)
        return "payment successful"

    def increment_current_date(self):
        """Increments day and calculates fines."""
        for patron_id in self._members:
            patron = self._members[patron_id]
            held_items = patron.get_checked_out_items()
            for item in held_items:
                date_checked_out = item.get_date_checked_out()
                check_out_length = item.get_check_out_length()
                if (self._current_date - date_checked_out) >= check_out_length:
                    patron.amend_fine(0.1)

        self._current_date += 1
        return

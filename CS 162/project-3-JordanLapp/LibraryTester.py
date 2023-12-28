import unittest
import Library


class Tests(unittest.TestCase):

    def test_library_item(self):
        test_item = Library.LibraryItem(1, "The Bible")
        test_id = test_item.get_id()
        test_name = test_item.get_name()
        test_location = test_item.get_location()

        self.assertEqual(test_id, 1)
        self.assertEqual(test_name, "The Bible")
        self.assertEqual(test_location, "ON_SHELF")

    def test_book(self):
        test_book = Library.Book(2, "Cat In The Hat", "Dr Seuss")
        test_id = test_book.get_id()
        test_name = test_book.get_name()
        test_author = test_book.get_author()
        test_length = test_book.get_check_out_length()
        test_location = test_book.get_location()

        self.assertEqual(test_id, 2)
        self.assertEqual(test_name, "Cat In The Hat")
        self.assertEqual(test_location, "ON_SHELF")
        self.assertEqual(test_author, "Dr Seuss")
        self.assertEqual(test_length, 21)

    def test_album(self):
        test_album = Library.Album(3, "Pink Tape", "Lil Uzi Vert")
        test_id = test_album.get_id()
        test_name = test_album.get_name()
        test_artist = test_album.get_artist()
        test_length = test_album.get_check_out_length()
        test_location = test_album.get_location()

        self.assertEqual(test_id, 3)
        self.assertEqual(test_name, "Pink Tape")
        self.assertEqual(test_location, "ON_SHELF")
        self.assertEqual(test_artist, "Lil Uzi Vert")
        self.assertEqual(test_length, 14)

    def test_movie(self):
        test_movie = Library.Movie(4, "Inception", "Christopher Nolan")
        test_id = test_movie.get_id()
        test_name = test_movie.get_name()
        test_director = test_movie.get_director()
        test_length = test_movie.get_check_out_length()
        test_location = test_movie.get_location()

        self.assertEqual(test_id, 4)
        self.assertEqual(test_name, "Inception")
        self.assertEqual(test_location, "ON_SHELF")
        self.assertEqual(test_director, "Christopher Nolan")
        self.assertEqual(test_length, 7)

    def test_check_out_library_item(self):
        b1 = Library.Book("345", "Phantom Tollbooth", "Juster")
        a1 = Library.Album("456", "...And His Orchestra", "The Fastbacks")
        m1 = Library.Movie("567", "Laputa", "Miyazaki")

        p1 = Library.Patron("abc", "Felicity")
        p2 = Library.Patron("bcd", "Waldo")

        lib = Library.Library()
        lib.add_library_item(b1)
        lib.add_library_item(a1)
        lib.add_patron(p1)
        lib.add_patron(p2)

        # Check out library item
        lib.check_out_library_item("abd", "345")
        lib.check_out_library_item("abc", "346")
        lib.check_out_library_item("abc", "345")
        lib.check_out_library_item("bcd", "345")
        lib.request_library_item("bcd", "345")
        lib.request_library_item("bcd", "456")
        lib.check_out_library_item("abc", "456")
        lib.request_library_item("abc", "456")
        length = b1.get_check_out_length()
        for _ in range(28):
            lib.increment_current_date()
            fine = p1.get_fine_amount()
            print(fine)
        lib.pay_fine("abc", 0.7)
        fine = p1.get_fine_amount()
        print(fine)
        lib.return_library_item("345")
        lib.return_library_item("456")
        lib.check_out_library_item("abc", "456")
        lib.check_out_library_item("bcd", "456")
if __name__ == '__main__':
    unittest.main()

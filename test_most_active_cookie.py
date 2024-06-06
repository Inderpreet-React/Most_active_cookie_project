import unittest
from io import StringIO
from most_active_cookie import extract_cookie_data, find_most_active_cookies

class TestMostActiveCookie(unittest.TestCase):

    def test_extract_cookie_data(self):
        log_data = StringIO(
            "cookie,timestamp\n"
            "AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00\n"
            "SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00\n"
            "AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00\n"
            "4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00\n"
        )
        lines = log_data.readlines()[1:]  # Skip header
        cookie_count = extract_cookie_data(lines, "2018-12-09")
        self.assertEqual(cookie_count["AtY0laUfhglK3lC7"], 2)
        self.assertEqual(cookie_count["SAZuXPGUrfbcn5UA"], 1)

    def test_find_most_active_cookies(self):
        cookie_count = {
            "AtY0laUfhglK3lC7": 2,
            "SAZuXPGUrfbcn5UA": 1
        }
        most_active_cookies = find_most_active_cookies(cookie_count)
        self.assertEqual(most_active_cookies, ["AtY0laUfhglK3lC7"])

if __name__ == '__main__':
    unittest.main()

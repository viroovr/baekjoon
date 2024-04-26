import unittest


def leap_year(year):
    if year % 4 != 0:
        return False
    if year % 100 == 0 and year % 400 != 0:
        return False
    return True


class LeapYearTest(unittest.TestCase):
    def test_leap_year(self):
        self.assertTrue(leap_year(0))
        self.assertTrue(leap_year(4))
        self.assertTrue(leap_year(1200))
        self.assertTrue(leap_year(2000))
        self.assertTrue(leap_year(2020))
        self.assertTrue(leap_year(2024))
        self.assertTrue(leap_year(2028))

    def test_not_leap_year(self):
        self.assertFalse(leap_year(1))
        self.assertFalse(leap_year(3))
        self.assertFalse(leap_year(700))
        self.assertFalse(leap_year(900))
        self.assertFalse(leap_year(1300))

    def test_same_calender(self):
        import calendar
        for year in range(1, 100000):
            self.assertEqual(leap_year(year), calendar.isleap(year))


if __name__ == "__main__":
    unittest.main()

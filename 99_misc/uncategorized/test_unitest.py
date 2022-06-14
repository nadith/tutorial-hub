import unittest

class TestDataGenerator(unittest.TestCase):
    """Description."""

    def setUp(self):
        self.val = "Hello"

    def test_case1(self):

        print("Hello World", self.val)

        def _fail():
            raise Exception("foobar")

        # test_fail(_fail, contains="f1oo")
        self.assertRaises(Exception, _fail)

        # Ref: https://docs.python.org/3/library/unittest.html
        self.assertEqual(0, 10)

# Ref: https://stackoverflow.com/questions/20992731/meaning-of-unittest-main-in-python-unittest-module
if __name__ == "__main__":
    unittest.main()

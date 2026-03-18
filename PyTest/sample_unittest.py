import unittest

class TestSample(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

class TestSample2(unittest.TestCase):
    def setUp(self):
        self.target = 'foo'

    def test_upper(self):
        self.assertEqual(self.target.upper(), 'FOO')

class TestSample3(unittest.TestCase):
    @unittest.skip("Skip this test")
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == "__main__":
    # unittest.main()

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests([
        loader.loadTestsFromTestCase(TestSample),
        loader.loadTestsFromTestCase(TestSample2),
        loader.loadTestsFromTestCase(TestSample3),
    ])
    unittest.TextTestRunner(verbosity=2).run(suite)

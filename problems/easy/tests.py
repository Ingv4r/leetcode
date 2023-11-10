import unittest


class TestDuplicates(unittest.TestCase):
    n1 = [1, 1, 2]
    n2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    n3 = []
    n4 = [1, 1]

    def test_case1(self):
        self.assertSequenceEqual(self.n1, [1, 2])

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    unittest.main()

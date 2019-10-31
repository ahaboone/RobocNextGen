import random
import unittest

my_list = ["chien", "chat", "lion", "panthere", "grenouille", "giraffe"]
mon_choix = random.choice(my_list)
print(mon_choix)
mon_echantillon = random.sample(my_list,5)
print(mon_echantillon)


class Mytest(unittest.TestCase):
    def setUp(self):
        """Initialisation des tests."""
        self.my_test_list = list(range(10))

    def test_choice(self):
        my_elt = random.choice(self.my_test_list)
        self.assertIn(my_elt, self.my_test_list)

    def test_shuffle(self):
        temp = list(self.my_test_list)
        random.shuffle(self.my_test_list)
        self.assertEqual(self.my_test_list.sort(),temp.sort())

    def test_sample(self):
        my_sample = random.sample(self.my_test_list,5)
        for elt in my_sample:
            self.assertIn(elt, self.my_test_list)

        with self.assertRaises(ValueError):
            random.sample(self.my_test_list, 20)

unittest.main()


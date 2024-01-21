import unittest
from body_goals import body_goals

class TestBodyGoals(unittest.TestCase):
    def test_berat_badan_lakilaki(self):
        self.assertAlmostEqual(body_goals(175, 'lakilaki'), 67.5, delta=0.01)

    def test_berat_badan_perempuan(self):
        self.assertAlmostEqual(body_goals(160, 'perempuan'), 51.0, delta=0.01)

    def test_gender_tidak_valid(self):
        with self.assertRaises(ValueError):
            body_goals(170, 'lainnya')

if __name__ == "__main__":
    unittest.main()

import unittest
from example import kalkulator

class KalkulatorTest(unittest.TestCase):

    def test_jumlah(self):
        self.assertEqual(kalkulator(10, 20, "jumlah"), 30)

    def test_kurang(self):
        self.assertEqual(kalkulator(10, 20, "kurang"), -10)

    def test_kali(self):
        self.assertEqual(kalkulator(10, 20, "kali"), 200)

    def test_bagi(self):
        self.assertEqual(kalkulator(10, 20, "bagi"), 0.5)

    def test_pangkat(self):
        self.assertEqual(kalkulator(10, 2, "pangkat"), 100)

    def test_modulus(self):
        self.assertEqual(kalkulator(10, 2, "modulus"), 0)

if __name__ == '__main__':
    unittest.main()
    # untuk run unit test menggunakan 
    #if __name__ == '__main__':
    #unittest.main()
    #spasi dan tab diperhatikan agar test run berhasil
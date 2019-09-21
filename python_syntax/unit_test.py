import unittest
import calc

class TestCalc(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_add(self):
        result=calc.add(12,6)
        self.assertEqual(result,18)

    def test_pow(self):
        rel=calc.cos(60)
        self.assertEqual(round(rel,1),0.5)
    def test_didv(self):
        rel=calc.divide(10,3)
        self.assertEqual(rel,3)

        # self.assertRaises(ValueError,calc.divide,10,0)
if __name__=='__main__':
    unittest.main()
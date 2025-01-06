import unittest
from services import final_price

class TestFinalPrice(unittest.TestCase):

    def test_final_price(self):
        # Calculate final price using a 10% discount on 100
        self.assertEqual(final_price(100, 10), 90)  # 100 - 10% of 100 (10) = 90
        
        # Calculate final price using a 15% discount on 200
        self.assertEqual(final_price(200, 15), 170)  # 200 - 15% of 200 (30) = 170
        
        # Edge case: price is 0, final price should be 0 regardless of the discount
        self.assertEqual(final_price(0, 50), 0)
        
        # Edge case: no discount (0%), final price should be same as the price
        self.assertEqual(final_price(100, 0), 100)
        
        # Edge case: full discount (100%), final price should be 0
        self.assertEqual(final_price(100, 100), 0)

        # Check with negative price (should still work)
        #self.assertEqual(final_price(-100, 20), -120)  # -100 - 20% of -100 (-20) = -120

if __name__ == '__main__':
    unittest.main()
import unittest
from services import calculate_discount, final_price

class TestCalculateDiscount(unittest.TestCase):
    
    def test_calculate_discount(self):
        # 10% of 100 is 10
        self.assertEqual(calculate_discount(100, 10), 10)
        
        # 15% of 200 is 30
        self.assertEqual(calculate_discount(200, 15), 30)
        
        # Edge case: price is 0, so discount is 0
        self.assertEqual(calculate_discount(0, 50), 0)
        
        # Edge case: 0% discount should return 0
        self.assertEqual(calculate_discount(100, 0), 0)
        
        # Edge case: 100% discount should return the full price
        self.assertEqual(calculate_discount(100, 100), 100)
        
        # Check for negative price (should return a negative discount)
        self.assertEqual(calculate_discount(-100, 20), -20)

if __name__ == '__main__':
    unittest.main()
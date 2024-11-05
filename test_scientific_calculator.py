import unittest
import math
from scientific_calculator import (sin_function, cos_function, tan_function, sqrt_function, log_function, exp_function, asin_function, acos_function,
    atan_function, sinh_function, cosh_function, tanh_function)

class TestScientificCalculator(unittest.TestCase):

    # Test for sin_function
    def test_sin_positive(self):
        self.assertAlmostEqual(sin_function(90), 1, places=2)

    def test_sin_negative(self):
        self.assertAlmostEqual(sin_function(-90), -1, places=2)

    def test_sin_zero(self):
        self.assertAlmostEqual(sin_function(0), 0, places=2)

    def test_sin_non_numeric(self):
        with self.assertRaises(ValueError):
            sin_function("hello")

    # Test for cos_function
    def test_cos_positive(self):
        self.assertAlmostEqual(cos_function(0), 1, places=2)

    def test_cos_negative(self):
        self.assertAlmostEqual(cos_function(180), -1, places=2)

    def test_cos_zero(self):
        self.assertAlmostEqual(cos_function(90), 0, places=2)

    def test_cos_non_numeric(self):
        with self.assertRaises(ValueError):
            cos_function("hello")

    # Test for tan_function
    def test_tan_positive(self):
        self.assertAlmostEqual(tan_function(45), 1, places=2)

    def test_tan_negative(self):
        self.assertAlmostEqual(tan_function(-45), -1, places=2)

    def test_tan_zero(self):
        self.assertAlmostEqual(tan_function(0), 0, places=2)

    def test_tan_non_numeric(self):
        with self.assertRaises(ValueError):
            tan_function("hello")

    # Test for sqrt_function
    def test_sqrt_positive(self):
        self.assertAlmostEqual(sqrt_function(16), 4)

    def test_sqrt_zero(self):
        self.assertEqual(sqrt_function(0), 0)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            sqrt_function(-1)

    def test_sqrt_non_numeric(self):
        with self.assertRaises(ValueError):
            sqrt_function("hello")

    # Test for log_function
    def test_log_positive(self):
        self.assertAlmostEqual(log_function(10), 1, places=2)

    def test_log_zero(self):
        with self.assertRaises(ValueError):
            log_function(0)

    def test_log_negative(self):
        with self.assertRaises(ValueError):
            log_function(-1)

    def test_log_non_numeric(self):
        with self.assertRaises(ValueError):
            log_function("hello")

    # Test for exp_function
    def test_exp_positive(self):
        self.assertAlmostEqual(exp_function(2), math.exp(2), places=2)

    def test_exp_zero(self):
        self.assertAlmostEqual(exp_function(0), 1, places=2)

    def test_exp_negative(self):
        self.assertAlmostEqual(exp_function(-2), math.exp(-2), places=2)

    def test_exp_non_numeric(self):
        with self.assertRaises(ValueError):
            exp_function("hello")


    # Tests for asin_function
    def test_asin_positive(self):
        self.assertAlmostEqual(asin_function(1), math.degrees(math.asin(1)), places=2)

    def test_asin_zero(self):
        self.assertAlmostEqual(asin_function(0), 0, places=2)

    def test_asin_negative(self):
        self.assertAlmostEqual(asin_function(-1), math.degrees(math.asin(-1)), places=2)

    def test_asin_out_of_range(self):
        with self.assertRaises(ValueError):
            asin_function(2)

    def test_asin_non_numeric(self):
        with self.assertRaises(ValueError):
            asin_function("hello")

    # Tests for acos_function
    def test_acos_positive(self):
        self.assertAlmostEqual(acos_function(1), 0, places=2)

    def test_acos_zero(self):
        self.assertAlmostEqual(acos_function(0), 90, places=2)

    def test_acos_negative(self):
        self.assertAlmostEqual(acos_function(-1), 180, places=2)

    def test_acos_out_of_range(self):
        with self.assertRaises(ValueError):
            acos_function(2)

    def test_acos_non_numeric(self):
        with self.assertRaises(ValueError):
            acos_function("hello")

    # Tests for atan_function
    def test_atan_positive(self):
        self.assertAlmostEqual(atan_function(1), math.degrees(math.atan(1)), places=2)

    def test_atan_zero(self):
        self.assertAlmostEqual(atan_function(0), 0, places=2)

    def test_atan_negative(self):
        self.assertAlmostEqual(atan_function(-1), math.degrees(math.atan(-1)), places=2)

    def test_atan_non_numeric(self):
        with self.assertRaises(ValueError):
            atan_function("hello")

    # Tests for sinh_function
    def test_sinh_positive(self):
        self.assertAlmostEqual(sinh_function(2), math.sinh(2), places=2)

    def test_sinh_zero(self):
        self.assertAlmostEqual(sinh_function(0), 0, places=2)

    def test_sinh_negative(self):
        self.assertAlmostEqual(sinh_function(-2), math.sinh(-2), places=2)

    def test_sinh_non_numeric(self):
        with self.assertRaises(ValueError):
            sinh_function("hello")

    # Tests for cosh_function
    def test_cosh_positive(self):
        self.assertAlmostEqual(cosh_function(2), math.cosh(2), places=2)

    def test_cosh_zero(self):
        self.assertAlmostEqual(cosh_function(0), 1, places=2)

    def test_cosh_negative(self):
        self.assertAlmostEqual(cosh_function(-2), math.cosh(-2), places=2)

    def test_cosh_non_numeric(self):
        with self.assertRaises(ValueError):
            cosh_function("hello")

    # Tests for tanh_function
    def test_tanh_positive(self):
        self.assertAlmostEqual(tanh_function(2), math.tanh(2), places=2)

    def test_tanh_zero(self):
        self.assertAlmostEqual(tanh_function(0), 0, places=2)

    def test_tanh_negative(self):
        self.assertAlmostEqual(tanh_function(-2), math.tanh(-2), places=2)

    def test_tanh_non_numeric(self):
        with self.assertRaises(ValueError):
            tanh_function("hello")



if __name__ == '__main__':
    unittest.main()

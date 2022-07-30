from decimal import Decimal
import unittest
from calculate import Calculator

calculator = Calculator()


class test_calculator(unittest.TestCase):
    # misc tests
    def test_ignore_spaces(self):
        """2 + 2 + 5"""
        test_param_spaces = "2 + 2 + 5"
        test_param_no_spaces = "2+2+5"
        result_spaces = calculator.calculate(test_param_spaces)
        result_no_spaces = calculator.calculate(test_param_no_spaces)
        self.assertEqual(result_spaces, result_no_spaces)

    def test_ignore_spaces_with_negative_int(self):
        test_param_spaces = "2 + -2 + 5"
        test_param_no_spaces = "2+-2+5"
        result_spaces = calculator.calculate(test_param_spaces)
        result_no_spaces = calculator.calculate(test_param_no_spaces)
        self.assertEqual(result_spaces, result_no_spaces)

    def test_ignore_trailing_spaces(self):
        test_param = "       2 + 5 + 8 + 9   "
        result = calculator.calculate(test_param)
        self.assertEqual(result, 24.0)
    # TODO Add some error handling tests

    def test_raise_zero_division_error(self):
        test_params = "2 / 0"
        with self.assertRaises(ZeroDivisionError):
            calculator.calculate(test_params)

    # addition
    def test_simple_int_addition(self):
        test_param = "3 + 5"
        result = calculator.calculate(test_param)
        self.assertEqual(result, 8)

    def test_longer_int_addition(self):
        test_param = "3 + 5 + 4 + 6"
        result = calculator.calculate(test_param)
        self.assertEqual(result, 18)

    def test_simple_float_addition(self):
        test_param = "1.5 + 2.6"
        result = calculator.calculate(test_param)
        self.assertEqual(result, 4.1)

    def test_longer_float_addition(self):
        test_params = "0.2 + 0.9 + 10.5"
        result = calculator.calculate(test_params)
        self.assertEqual(result, 11.6)

    def test_negative_integer_addition(self):
        test_params = "-2 + -5"
        result = calculator.calculate(test_params)
        self.assertEqual(result, -7)

    def test_negative_float_addition(self):
        test_params = "-2.5 + -5.3"
        result = calculator.calculate(test_params)
        self.assertEqual(result, -7.8)

    # Subtraction
    def test_simple_int_subtraction(self):
        test_param = "5 - 3"
        result = calculator.calculate(test_param)
        self.assertEqual(result, 2)

    def test_longer_int_subtraction(self):
        test_param = "22 - 10 - 2 - 4"
        result = calculator.calculate(test_param)
        self.assertEqual(result, 6)

    def test_simple_float_subtraction(self):
        test_param = "5.6 - 2.1"
        result = calculator.calculate(test_param)
        self.assertEqual(result, 3.5)

    def test_longer_float_subtraction(self):
        test_params = "18.9 - 6.3 - 6.3"
        result = calculator.calculate(test_params)
        self.assertEqual(result, 6.3)

    def test_negative_integer_subtraction(self):
        test_params = "-2 - -5"
        result = calculator.calculate(test_params)
        self.assertEqual(result, 3)

    def test_negative_float_subtraction(self):
        test_params = "-2.5 - -10.5"
        result = calculator.calculate(test_params)
        self.assertEqual(result, 8)

    # Multiplication
    def test_simple_int_multiplication(self):
        test_param = "5 * 3"
        result = calculator.calculate(test_param)
        self.assertEqual(result, 15)

    def test_longer_int_multiplication(self):
        test_param = "10 * 10 * 4"
        result = calculator.calculate(test_param)
        self.assertEqual(result, 400)

    def test_simple_float_multiplication(self):
        test_param = "2.5 * 2.5"
        result = calculator.calculate(test_param)
        self.assertEqual(result, 6.25)

    def test_longer_float_multiplication(self):
        test_params = "16.5 * 6.34 - 6.342"
        result = calculator.calculate(test_params)
        self.assertEqual(result, 98.268)

    def test_negative_integer_multiplication(self):
        test_params = "-2 * -5"
        result = calculator.calculate(test_params)
        self.assertEqual(result, 10)

    def test_negative_float_multiplication(self):
        test_params = "-2.2 * -10.4"
        result = calculator.calculate(test_params)
        self.assertEqual(result, 22.88)

    # Division
    def test_simple_int_division(self):
        test_param = "10 / 2"
        result = calculator.calculate(test_param)
        self.assertEqual(result, 5)

    def test_longer_int_division(self):
        test_param = "100 / 10 / 2"
        result = calculator.calculate(test_param)
        self.assertEqual(result, 5)

    def test_simple_float_division(self):
        test_param = "9.3 / 2.5"
        result = calculator.calculate(test_param)
        self.assertEqual(result, 3.72)

    def test_longer_float_division(self):
        test_params = "55.3 / 6.1 / 2.2"
        result = calculator.calculate(test_params)
        self.assertAlmostEqual(result, 4.12071535022)

    def test_negative_integer_division(self):
        test_params = "-6 * -2"
        result = calculator.calculate(test_params)
        self.assertEqual(result, 12)

    def test_negative_float_division(self):
        test_params = "-9.3 / -3.1"
        result = calculator.calculate(test_params)
        self.assertEqual(result, 3)

    # Exponentials
    # def test_squaring_integer(self):
    #     test_param = '2^2'
    #     result = calculator.calculate(test_param)
    #     self.assertEqual(result, 4)

    # def test_squaring_float(self):
    #     test_param = '2.5^2'
    #     result = calculator.calculate(test_param)
    #     self.assertEqual(result, 6.25)

    # def test_cubing_integer(self):
    #     test_param = '2^3'
    #     result = calculator.calculate(test_param)
    #     self.assertEqual(result, 8)

    # def test_cubing_float(self):
    #     test_param = '3.33^3'
    #     result = calculator.calculate(test_param)
    #     self.assertEqual(result, 36.926037)

    #  Operations inolving brackets
    def test_int_addition_in_brackets(self):
        test_param = '(1 + 5)'
        result = calculator.calculate(test_param)
        self.assertEqual(result, 6)

    def test_int_subtraction_in_brackets(self):
        test_param = '(6 - 3)'
        result = calculator.calculate(test_param)
        self.assertEqual(result, 3)

    def test_int_multiplication_in_brackets(self):
        test_param = '(2 * 3)'
        result = calculator.calculate(test_param)
        self.assertEqual(result, 6)

    def test_int_division_in_brackets(self):
        test_param = '(9 / 3)'
        result = calculator.calculate(test_param)
        self.assertEqual(result, 3)

    def test_multiplication_outside_of_brackets(self):
        test_param = '9 * (9)'
        result = calculator.calculate(test_param)
        self.assertEqual(result, 81)

    # calculations with mixed operators, number types
    def test_multiple_operators_1(self):
        test_param = '8 * 5 - 20 + 6'
        result = calculator.calculate(test_param)
        self.assertEqual(result, 26)

    def test_multiple_operators_2(self):
        test_param = '8.5 * 5 * 20.9 / 6'
        result = calculator.calculate(test_param)
        self.assertEqual(result, 148.04166666666666)

    # TODO for future iteration add tests for roots
    # TODO for future iteration add tests for logarithms
    # TODO for future iterations add tests for trigonometric functions
# unittest.main()

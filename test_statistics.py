from unittest import TestCase
from statistics import variance, stdev, average
from math import sqrt
import random


class StatisticsTest(TestCase):

    def test_variance_typical_values(self):
        """variance of typical values"""
        self.assertEqual(0.0, variance([10.0, 10.0, 10.0, 10.0, 10.0]))
        self.assertEqual(2.0, variance([1, 2, 3, 4, 5]))
        self.assertEqual(8.0, variance([10, 2, 8, 4, 6]))

    def test_variance_non_integers(self):
        """variance should work with decimal values"""
        # variance([x,y,z]) == variance([x+d,y+d,z+d]) for any d
        self.assertAlmostEqual(4.0, variance([0.1, 4.1]))
        # variance([0,4,4,8]) == 8
        self.assertAlmostEqual(8.0, variance([0.1, 4.1, 4.1, 8.1]))

    def test_variance_empty_list(self):
        """variance of an empty list should raise a ValueError"""
        with self.assertRaises(ValueError):
            variance([])

    def test_stdev(self):
        # standard deviation of a single value should be zero
        self.assertEqual(0.0, stdev([10.0]))
        # simple test
        self.assertEqual(2.0, stdev([1, 5]))
        # variance([0, 0.5, 1, 1.5, 2.0]) is 0.5
        self.assertEqual(sqrt(0.5), stdev([0, 0.5, 1, 1.5, 2]))

    def test_stdev_empty_list(self):
        """standard deviation of an empty list should raise a ValueError"""
        with self.assertRaises(ValueError):
            stdev([])

    def test_average(self):
        # average of typical values
        self.assertEqual(3.0, average([1, 2, 3, 4, 5]))
        # average of decimal values
        self.assertEqual(3.5, average([1.5, 3.5, 5.5]))
        # average of empty list should raise a ValueError
        with self.assertRaises(ValueError):
            average([])
        with self.assertRaises(TypeError):
            average(['a', 'b', 'c'])

    def test_variance_zero_values(self):
        self.assertEqual(0.0, variance([0, 0, 0]))

    def test_average_negative_numbers(self):
        self.assertEqual(0, average([-2, 0, 2]))

    def test_average_zero_values(self):
        self.assertEqual(0.0, average([0, 0, 0]))

    def test_average_large_dataset(self):
        # Generate a large dataset
        data = [random.randint(1, 1000) for _ in range(10000)]
        # Calculate average using a known method for comparison
        expected_average = sum(data) / len(data)
        self.assertAlmostEqual(expected_average, average(data))

    def test_stdev_zero_values(self):
        self.assertEqual(0.0, stdev([0, 0, 0]))

    def test_stdev_large_dataset(self):
        data = [random.randint(1, 1000) for _ in range(10000)]
        # Calculate standard deviation using a known method for comparison
        expected_stdev = sqrt(variance(data))
        self.assertAlmostEqual(expected_stdev, stdev(data))

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            average(['a', 'b', 'c'])

    def test_variance_single_value(self):
        """variance of a single value should be zero"""
        self.assertEqual(0.0, variance([10.0]))

    def test_stdev_single_value(self):
        """standard deviation of a single value should be zero"""
        self.assertEqual(0.0, stdev([10.0]))

    def test_variance_non_numeric(self):
        """variance should raise TypeError for non-numeric input"""
        with self.assertRaises(TypeError):
            variance(['a', 'b', 'c'])

    def test_stdev_non_numeric(self):
        """stdev should raise TypeError for non-numeric input"""
        with self.assertRaises(TypeError):
            stdev(['a', 'b', 'c'])

    def test_variance_none(self):
        """variance should raise TypeError for None input"""
        with self.assertRaises(TypeError):
            variance(None)

    def test_stdev_none(self):
        """stdev should raise TypeError for None input"""
        with self.assertRaises(TypeError):
            stdev(None)

    def test_average_none(self):
        """average should raise TypeError for None input"""
        with self.assertRaises(TypeError):
            average(None)

    def test_variance_two_values(self):
        """variance should handle a list with two identical values"""
        self.assertEqual(0.0, variance([5, 5]))
        self.assertEqual(1.0, variance([5, 3]))

    def test_stdev_two_values(self):
        """stdev should handle a list with two identical values"""
        self.assertEqual(0.0, stdev([5, 5]))
        self.assertEqual(1.0, stdev([5, 3]))

    def test_variance_large_identical_values(self):
        """variance of a large list of identical values should be zero"""
        data = [100.0] * 10000  # Large dataset with all identical values
        self.assertEqual(0.0, variance(data))

    def test_stdev_large_identical_values(self):
        """stdev of a large list of identical values should be zero"""
        data = [100.0] * 10000  # Large dataset with all identical values
        self.assertEqual(0.0, stdev(data))

    def test_average_mixed_values(self):
        """average of a mix of positive and negative values"""
        self.assertEqual(0.0, average([-1, 1, -2, 2]))
        self.assertEqual(2.5, average([0, 5]))

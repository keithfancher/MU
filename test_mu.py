#!/usr/bin/env python


import unittest
from mu import mu_test


class TestMu(unittest.TestCase):

    # These tuples are in the form: (start, goal, iterations)
    should_pass = (('MI', 'MI', 1),
                   ('MI', 'MIU', 10),
                   ('MI', 'MII', 10),
                   ('MI', 'MIIII', 10),
                   ('MI', 'MIIIIU', 10),
                   ('MI', 'MUIU', 10),
                   ('MI', 'MIIUIIU', 10),
                   ('MI', 'MUIUUIU', 10),
                   ('MI', 'MIUIUIUIU', 10))

    should_fail = (('MI', 'MU', 10),
                   ('MI', 'MIIUIIU', 1))

    def test_known_good_pairs(self):
        """Test known successful pairs"""
        for start, goal, iternum in self.should_pass:
            self.assertTrue(mu_test(start, goal, iternum))

    def test_known_bad_pairs(self):
        """Test pairs known to fail"""
        for start, goal, iternum in self.should_fail:
            self.assertFalse(mu_test(start, goal, iternum))

    # TODO!
    def test_malformed_input(self):
        pass


if __name__ == "__main__":
    unittest.main()

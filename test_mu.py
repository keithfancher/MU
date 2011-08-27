#!/usr/bin/env python


import unittest

from mu import mu_test
from mu import BadInputError


class TestMu(unittest.TestCase):

    # These tuples are in the form: (start, goal, iterations)
    should_pass = (('MI', 'MI', 1),
                   ('MI', 'MIU', 10),
                   ('MI', 'MII', 10),
                   ('MI', 'MIIII', 10),
                   ('MI', 'MIIIIU', 10),
                   ('MI', 'MUIu', 10),
                   ('MI', 'MIIUIIU', 10),
                   ('MI', 'MUIUUIU', 10),
                   ('MI', 'muiuuiu', 10),
                   ('MI', 'MIUIUIUIU', 10))

    should_fail = (('MI', 'MU', 10),
                   ('MI', 'MUUUUUUUUUUUU', 10),
                   ('MI', 'MUIUIUIUIUIUUIU', 10),
                   ('MI', 'MIIUUUUUUUIIU', 10),
                   ('MI', 'MIIUIIU', 1))

    bad_input = (('', '', 1),
                 ('MI', '', 1),
                 ('', 'MU', 1),
                 ('M', 'MII', 10),
                 ('MI', 'M', 10),
                 ('MIA', 'MU', 10),
                 ('MI', 'MIIhello', 10),
                 ('hello', '92', 10),
                 ('maximum', 'overdrive', 10))

    def test_known_good_pairs(self):
        """Test known successful pairs"""
        for start, goal, iternum in self.should_pass:
            self.assertTrue(mu_test(start, goal, iternum))

    def test_known_bad_pairs(self):
        """Test pairs known to fail"""
        for start, goal, iternum in self.should_fail:
            self.assertFalse(mu_test(start, goal, iternum))

    def test_malformed_input(self):
        """Test invalid input"""
        for start, goal, iternum in self.bad_input:
            self.assertRaises(BadInputError, mu_test, start, goal, iternum)


if __name__ == "__main__":
    unittest.main()

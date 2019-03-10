import unittest
import CIDR


class TestCIDR(unittest.TestCase):
    def test_validate_cidr(self):
        """
        Test cases for validating CIDR input
        """
        # No prefix length specified
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3.4")

        # Non numeric character for prefix length
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3.4/O")

        # incorrect prefix length
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3.4/33")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3.4/-1")

        # Incorrect octet count
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.4/1")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3.4.5/1")

        # Illegal octet values
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3.256/30")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.256.4/30")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.256.3.4/30")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "256.2.3.4/30")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3.2O8/30")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3oo.4/30")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2OO.3.4/30")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "25O.2.3.4/30")

    def test_to_string(self):
        """
        Test case for converting CIDR object to string
        """
        # Check if to_string returns the correct string representation
        self.assertEqual(CIDR.CIDR("1.2.3.4/5").to_string(), "1.2.3.4/5")

    def test_init(self):
        """
        Test __init__ function
        """
        # Check correct representation of CIDR in list and integer form
        cidr = CIDR.CIDR("1.2.3.4/5")
        self.assertEqual(cidr.octets[0], 1)
        self.assertEqual(cidr.octets[1], 2)
        self.assertEqual(cidr.octets[2], 3)
        self.assertEqual(cidr.octets[3], 4)
        self.assertEqual(cidr.prefix_len, 5)


if '__name__' == '__main__':
    unittest.main()
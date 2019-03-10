import unittest
import CIDR


class TestCIDR(unittest.TestCase):
    def test_validate_cidr(self):
        # no prefix length specified
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3.4")

        # non numeric character for prefix length
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3.4/O")

        # incorrect prefix length
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3.4/33")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3.4/-1")

        # Incorrect octet count
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.4/1")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3.4.5/1")

        # Illegal octet values
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3.400/30")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.300.4/30")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1000.2.3.4/30")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2000.3.4/30")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3.4OO/30")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3OO.4/30")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1OOO.2.3.4/30")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2OOO.3.4/30")

    def test_stringify(self):
        # check if stringify returns the correct string representation
        self.assertEqual(CIDR.CIDR("1.2.3.4/5").stringify(), "1.2.3.4/5")

    def test_init(self):
        # check correct CIDR notation
        cidr = CIDR.CIDR("1.2.3.4/5")
        self.assertEqual(cidr.octets[0], 1)
        self.assertEqual(cidr.octets[1], 2)
        self.assertEqual(cidr.octets[2], 3)
        self.assertEqual(cidr.octets[3], 4)
        self.assertEqual(cidr.prefix_len, 5)


if '__name__' == '__main__':
    unittest.main()
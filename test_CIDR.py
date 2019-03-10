import unittest
import CIDR


class TestCIDR(unittest.TestCase):
    def test_validate_cidr(self):
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3.4")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3.4/o")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3.4/33")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3.4/-1")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.4/1")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3.4.5/1")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.3.400/30")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2.300.4/30")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1000.2.3.4/30")
        self.assertRaises(ValueError, CIDR.CIDR.validate_cidr, "1.2000.3.4/30")

    def test_stringify(self):
        self.assertEqual(CIDR.CIDR("1.2.3.4/5").stringify(), "1.2.3.4/5")

    def test_init(self):
        cidr = CIDR.CIDR("1.2.3.4/5")
        self.assertEqual(cidr.octets[0], 1)
        self.assertEqual(cidr.octets[1], 2)
        self.assertEqual(cidr.octets[2], 3)
        self.assertEqual(cidr.octets[3], 4)
        self.assertEqual(cidr.prefix_len, 5)

if '__name__' == '__main__':
    unittest.main()
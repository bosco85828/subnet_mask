import unittest
import subnets as sub


class TestSubnets(unittest.TestCase):
    def test_init(self):
        """
        Test cases for __init__ function
        """
        # Check for empty subnets list
        self.assertRaises(ValueError, sub.Subnets, [])
        ValueError("Please provide at least one subnet when initializing")

        # Check correct representation of CIDRs
        cidrs = ['10.0.0.0/8', '5.0.0.0/8', '9.0.0.0/8']
        subnets = sub.Subnets(cidrs)
        self.assertEqual(len(subnets.subnets), 3)
        self.assertEqual(subnets.subnets[0].to_string(), '10.0.0.0/8')
        self.assertEqual(subnets.subnets[1].to_string(), '5.0.0.0/8')
        self.assertEqual(subnets.subnets[2].to_string(), '9.0.0.0/8')

    def test_get_smallest_supernet(self):
        """
        Test cases for get_smallest_supernet
        """
        # Same subnets, same prefix
        subnets = sub.Subnets(['10.0.128.0/24', '10.0.128.0/24'])
        self.assertEqual(subnets.get_smallest_supernet().to_string(), '10.0.128.0/24')

        # Same subnets, different prefix
        subnets = sub.Subnets(['10.0.128.0/28', '10.0.128.0/24'])
        self.assertEqual(subnets.get_smallest_supernet().to_string(), '10.0.128.0/24')

        # Different subnets, same prefix
        subnets = sub.Subnets(['10.0.0.0/8', '9.0.0.0/8'])
        self.assertEqual(subnets.get_smallest_supernet().to_string(), '8.0.0.0/6')

        # Different subnets, different prefix
        subnets = sub.Subnets(['10.0.1.0/26', '10.0.2.0/24'])
        self.assertEqual(subnets.get_smallest_supernet().to_string(), '10.0.0.0/22')

        # One subnet is supernet of other
        subnets = sub.Subnets(['10.0.0.0/23', '10.0.1.0/24'])
        self.assertEqual(subnets.get_smallest_supernet().to_string(), '10.0.0.0/23')

        # More than two subnets
        subnets = sub.Subnets(['10.0.0.0/8', '5.0.0.0/8', '9.0.0.0/8', '8.0.0.1/9'])
        self.assertEqual(subnets.get_smallest_supernet().to_string(), '0.0.0.0/4')

        # No bits common
        subnets = sub.Subnets(['64.0.0.0/8', '128.0.0.0/8'])
        self.assertEqual(subnets.get_smallest_supernet(), None)

        # Prefix length smaller than length of longest common prefix
        subnets = sub.Subnets(['10.10.0.1/8', '10.10.0.200/8'])
        self.assertEqual(subnets.get_smallest_supernet().to_string(), '10.0.0.0/8')
        subnets = sub.Subnets(['10.10.0.1/10', '10.10.0.200/11'])
        self.assertEqual(subnets.get_smallest_supernet().to_string(), '10.0.0.0/10')


if '__name__' == '__main__':
    unittest.main()

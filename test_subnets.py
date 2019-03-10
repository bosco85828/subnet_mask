import unittest
import subnets as sub


class TestSubnets(unittest.TestCase):
    def test_init(self):
        # check correct representation of CIDRs
        cidrs = ['10.0.0.0/8', '5.0.0.0/8', '9.0.0.0/8']
        subnets = sub.Subnets(cidrs)
        self.assertEqual(len(subnets.subnets), 3)
        self.assertEqual(subnets.subnets[0].stringify(), '10.0.0.0/8')
        self.assertEqual(subnets.subnets[1].stringify(), '5.0.0.0/8')
        self.assertEqual(subnets.subnets[2].stringify(), '9.0.0.0/8')

    def test_get_smallest_supernet(self):
        # same subnets
        subnets = sub.Subnets(['10.0.128.0/24', '10.0.128.0/24'])
        self.assertEqual(subnets.get_smallest_supernet().stringify(), '10.0.128.0/24')

        # different prefix length
        subnets = sub.Subnets(['10.0.1.0/26', '10.0.2.0/24'])
        self.assertEqual(subnets.get_smallest_supernet().stringify(), '10.0.0.0/22')

        # same prefix length
        subnets = sub.Subnets(['10.0.0.0/8', '9.0.0.0/8'])
        self.assertEqual(subnets.get_smallest_supernet().stringify(), '8.0.0.0/6')

        # one subnet is supernet of another
        subnets = sub.Subnets(['10.0.0.0/23', '10.0.1.0/24'])
        self.assertEqual(subnets.get_smallest_supernet().stringify(), '10.0.0.0/23')

        # more than two subnets
        subnets = sub.Subnets(['10.0.0.0/8', '5.0.0.0/8', '9.0.0.0/8'])
        self.assertEqual(subnets.get_smallest_supernet().stringify(), '0.0.0.0/4')

        # no bits common
        subnets = sub.Subnets(['64.0.0.0/8', '128.0.0.0/8'])
        self.assertEqual(subnets.get_smallest_supernet().stringify(), '0.0.0.0/0')

        # prefix length smaller than length of longest common prefix
        subnets = sub.Subnets(['10.10.0.1/8', '10.10.0.200/8'])
        self.assertEqual(subnets.get_smallest_supernet().stringify(), '10.0.0.0/8')


if '__name__' == '__main__':
    unittest.main()
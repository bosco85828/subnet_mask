import unittest
import subnets as sub


class TestSubnets(unittest.TestCase):
    def test_init(self):
        cidrs = ['10.0.0.0/8', '5.0.0.0/8', '9.0.0.0/8']
        subnets = sub.Subnets(cidrs)
        self.assertEqual(len(subnets.subnets), 3)
        self.assertEqual(subnets.subnets[0].stringify(), '10.0.0.0/8')
        self.assertEqual(subnets.subnets[1].stringify(), '5.0.0.0/8')
        self.assertEqual(subnets.subnets[2].stringify(), '9.0.0.0/8')

    def test_get_smallest_supernet(self):
        subnets = sub.Subnets(['10.0.0.0/24', '10.0.1.0/24'])
        self.assertEqual(subnets.get_smallest_supernet().stringify(), '10.0.0.0/23')

        subnets = sub.Subnets(['10.0.1.0/24', '10.0.2.0/24'])
        self.assertEqual(subnets.get_smallest_supernet().stringify(), '10.0.0.0/22')

        subnets = sub.Subnets(['10.0.0.0/23', '10.0.1.0/24'])
        self.assertEqual(subnets.get_smallest_supernet().stringify(), '10.0.0.0/23')

        subnets = sub.Subnets(['10.0.0.0/8', '9.0.0.0/8'])
        self.assertEqual(subnets.get_smallest_supernet().stringify(), '8.0.0.0/6')

        subnets = sub.Subnets(['10.0.0.0/8', '5.0.0.0/8', '9.0.0.0/8'])
        self.assertEqual(subnets.get_smallest_supernet().stringify(), '0.0.0.0/4')

        subnets = sub.Subnets(['64.0.0.0/8', '128.0.0.0/8'])
        self.assertEqual(subnets.get_smallest_supernet().stringify(), '0.0.0.0/0')


if '__name__' == '__main__':
    unittest.main()
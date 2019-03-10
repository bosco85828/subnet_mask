from network.CIDR import CIDR


class Subnets:
    def __init__(self, subnets):
        if not subnets:
            raise ValueError("Please provide at least one subnet when initializing")

        self.subnets = []
        for subnet in subnets:
            self.subnets.append(CIDR(subnet))

    def get_smallest_supernet(self):
        """
        Get the smallest supernet for all the subnets in the list.
        Time complexity: O(n) where n is the number of subnets in the input list
        Space complexity: O(1) as the algorithm uses constant space for any size of input

        :return: CIDR notation of network containing smallest number of
                 IPV4 addresses after prefix aggregation of all the subnets
        :type: CIDR
        """
        supernet = CIDR("255.255.255.255/0")
        mask_or = CIDR("0.0.0.0/0")
        min_prefix_len = 32

        # Perform bitwise AND and OR operation on all the cidrs
        # AND operation would only keep the common bits
        # OR operation would be used to obtain the prefix length
        for subnet in self.subnets:
            for i in range(4):
                supernet.octets[i] &= subnet.octets[i]
                mask_or.octets[i] |= subnet.octets[i]
            min_prefix_len = min(min_prefix_len, subnet.prefix_len)

        # Calculate prefix length and mask all bits beyond this length
        longest_common_prefix_found = False
        supernet.prefix_len = 0
        for i in range(4):
            # Find index of first bit from left which flipped
            bitindex = 128

            # Mask for setting all bits in host part of subnet to 0
            bitmask = 255
            bits = mask_or.octets[i] ^ supernet.octets[i]

            while bitindex and not longest_common_prefix_found:
                if bits & bitindex or supernet.prefix_len == min_prefix_len:
                    longest_common_prefix_found = True
                else:
                    supernet.prefix_len += 1
                    bitindex >>= 1
                    bitmask >>= 1

            # Mask all bits beyond prefix length
            supernet.octets[i] &= ~bitmask

        # Return None if the networks cannot be aggregated
        if supernet.prefix_len == 0:
            return None
        else:
            return supernet

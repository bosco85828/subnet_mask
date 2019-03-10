from CIDR import CIDR


class Subnets:
    def __init__(self, subnets):
        self.subnets = []
        for subnet in subnets:
            self.subnets.append(CIDR(subnet))

    def get_smallest_supernet(self):
        supernet = CIDR("255.255.255.255/0")
        mask_or = CIDR("0.0.0.0/0")
        min_prefix_len = 32

        # perform bitwise AND and OR operation on all the cidrs
        # AND operation would only keep the common bits
        # OR operation would be used to obtain the prefix length
        for subnet in self.subnets:
            for i in range(4):
                supernet.octets[i] &= subnet.octets[i]
                mask_or.octets[i] |= subnet.octets[i]
            min_prefix_len = min(min_prefix_len, subnet.prefix_len)

        # calculate prefix length and mask all bits beyond this length
        longest_common_prefix_found = False
        supernet.prefix_len = 0
        for i in range(4):
            # find index of first bit from left which flipped
            bitindex = 128

            # mask for removing all uncommon bits
            bitmask = 255
            bits = mask_or.octets[i] ^ supernet.octets[i]

            while bitindex and not longest_common_prefix_found:
                if bits & bitindex or supernet.prefix_len == min_prefix_len:
                    longest_common_prefix_found = True
                else:
                    supernet.prefix_len += 1
                    bitindex >>= 1
                    bitmask >>= 1

            # mask all bits beyond prefix length
            supernet.octets[i] &= ~bitmask

        return supernet

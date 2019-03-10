from CIDR import CIDR


class Subnets:
    def __init__(self, subnets):
        self.subnets = []
        for subnet in subnets:
            self.subnets.append(CIDR(subnet))

    def get_smallest_supernet(self):
        supernet = CIDR("255.255.255.255/0")

        # perform bitwise & operation on all the cidrs
        # this operation would only keep the common bits
        for subnet in self.subnets:
            for i in range(4):
                supernet.octets[i] &= subnet.octets[i]

        # calculate xor masks - used to find the first changing bit
        # calculate or mask
        mask_xor = []
        mask_or = []
        for o in self.subnets[0].octets:
            mask_xor.append(o)
            mask_or.append(o)

        for subnet in self.subnets[1:]:
            for i in range(4):
                mask_or[i] |= subnet.octets[i]
                mask_xor[i] ^= subnet.octets[i]

        # calculate supernet
        found = False
        supernet.prefix_len = 0
        for i in range(4):
            bitmask = 128
            bits = mask_or[i] ^ supernet.octets[i]
            supernet.octets[i] &= ~mask_xor[i]
            while bitmask and not found:
                if bits & bitmask:
                    found = True
                else:
                    supernet.prefix_len += 1
                bitmask >>= 1

        return supernet


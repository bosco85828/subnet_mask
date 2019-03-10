import network

subnets = network.Subnets(["10.0.0.0/24", "10.0.1.0/24"])
supernet = subnets.get_smallest_supernet()
supernet.display()

subnets = network.Subnets(["10.0.1.0/24", "10.0.2.0/24"])
supernet = subnets.get_smallest_supernet()
supernet.display()

subnets = network.Subnets(["10.0.0.0/23", "10.0.1.0/24"])
supernet = subnets.get_smallest_supernet()
supernet.display()

subnets = network.Subnets(["10.0.0.0/8", "9.0.0.0/8"])
supernet = subnets.get_smallest_supernet()
supernet.display()

subnets = network.Subnets(["10.0.0.0/8", "9.0.0.0/8", "5.0.0.0/8"])
supernet = subnets.get_smallest_supernet()
supernet.display()

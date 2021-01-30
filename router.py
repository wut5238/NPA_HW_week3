class Router:
    def __init__(self, brand, model, hostname):
        self.interfaces = []
        self.brand = brand
        self.model = model
        self.hostname = hostname
    def add_inf(self, inf):
        self.interfaces.append(inf)
r1 = Router('Cisco', 'IOSv', "R1")
print(r1.hostname)
r1.add_inf("GigabitEthernet 0/1")
print(r1.interfaces)

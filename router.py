class Router:
    def __init__(self, brand, model, hostname):
        self.interfaces = []
        self.brand = brand
        self.model = model
        self.hostname = hostname
    def add_inf(self, inf):
        self.interfaces.append(inf)
    def show_inf(self):
        print("show interface of",self.hostname)
        print("{} has {} interfaces".format(self.hostname, len(self.interfaces)))
        print(*self.interfaces, sep="\n")

r1 = Router('Cisco', 'IOSv', "R1")
r1.add_inf("GigabitEthernet 0/1")
r1.add_inf("GigabitEthernet 0/2")
r1.show_inf()

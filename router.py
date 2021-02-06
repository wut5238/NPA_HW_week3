class Router:
    def __init__(self, brand, model, hostname):
        self.connection = {}
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

    def connect(self, inf1, router, inf2):
        self.connection["{}".format(router.hostname)]="{} intrface {} connect to {} on interface {}".format(self.hostname ,inf1, router.hostname, inf2)
        router.connection["{}".format(self.hostname)]="{} intrface {} connect to {} on interface {}".format(router.hostname ,inf2, self.hostname, inf1)

    #Which router is this router connected to
    def show_connection(self):
        print("{} connected to router".format(self.hostname), end=" ")
        print(*self.connection.keys(), sep=", ")
        print(*self.connection.values(), sep="\n")


r1 = Router('Cisco', 'IOSv', "R1")
r1.add_inf("GigabitEthernet 0/1")
r1.add_inf("GigabitEthernet 0/2")
r1.show_inf()
print()
r2 = Router('Cisco', 'IOSv', "R2")
r2.add_inf("GigabitEthernet 0/2")
r2.show_inf()
print()
r3 = Router('Cisco', 'IOSv', "R3")
r3.add_inf("GigabitEthernet 0/1")
r3.show_inf()
print()

r1.connect("GigabitEthernet 0/1", r2, "GigabitEthernet 0/2")
r1.connect("GigabitEthernet 0/2", r3, "GigabitEthernet 0/1")
r1.show_connection()
print()
r2.show_connection()
print()
r3.show_connection()
print()

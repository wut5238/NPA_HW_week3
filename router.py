
class Router:
    def __init__(self, brand, model, hostname):
        self.interfaces = []
        self.brand = brand
        self.model = model
        self.hostname = hostname
r1 = Router('Cisco', 'IOSv', "R1")
print(r1.hostname)

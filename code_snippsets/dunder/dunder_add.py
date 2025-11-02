class Server:
    def __init__(self, name, cpu):
        self.name = name
        self.cpu = cpu  # cores amount

    def __add__(self, other):
        if not isinstance(other, Server):
            return NotImplemented
        return Server(f"{self.name}+{other.name}", self.cpu + other.cpu)

    def add_two_objects(self, other):
        if not isinstance(other, Server):
            return NotImplemented
        return Server(f"{self.name}+{other.name}", self.cpu + other.cpu)


s1 = Server("Web", 4)
s2 = Server("DB", 8)
s3 = s1.add_two_objects(s2)
print(s3.name)
# print(s3.name, s3.cpu)  # Web+DB 12

class Server:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

    def __eq__(self, other):
        if not isinstance(other, Server):
            return NotImplemented
        return self.ip == other.ip

    def __ne__(self, other):
        if not isinstance(other, Server):
            return NotImplemented
        return self.ip != other.ip


s1 = Server("Web", "192.168.1.10")
s2 = Server("DB", "192.168.1.10")
print(s1 == s2)

print(s1 != s2)

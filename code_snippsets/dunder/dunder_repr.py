class Server:
    def __init__(self, name, ip, status="stopped"):
        self.name = name
        self.ip = ip
        self.status = status

    def __repr__(self):
        return f"Server({self.name!r}, {self.ip!r}, {self.status!r})"

    def __str__(self):
        return f"{self.name} [{self.ip}] — {self.status}"


s = Server("Web", "192.168.1.10")
print(s)
# print(repr(s))

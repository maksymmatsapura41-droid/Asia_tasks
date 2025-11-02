class Server:
    def __init__(self, name, load):
        self.name = name
        self.load = load

    def __lt__(self, other):
        return self.load < other.load

    def __gt__(self, other):
        return self.load > other.load

servers = [Server("Web", 70), Server("DB", 40), Server("Cache", 55)]
servers.sort()
print([s.name for s in servers])

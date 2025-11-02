class Server:
    def __init__(self, name, processes):
        self.name = name
        self.processes = processes  # process list

    def __len__(self):
        return len(self.processes)


s = Server("Web", ["nginx", "uwsgi", "cron"])
print(len(s))  # 3

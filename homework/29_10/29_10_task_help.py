from abc import ABC, abstractmethod

# =====================
# Абстрактный класс
# =====================
class Server(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def status(self):
        pass

# =====================
# Реализация WebServer
# =====================
class WebServer(Server):
    def __init__(self, name, ip, load=0):
        self.name = name
        self.ip = ip
        self.load = load
        self.processes = {}  # словарь процессов
        self._status = "stopped"

    # TODO: __repr__, __str__
    # TODO: __eq__, __ne__, __lt__, __gt__
    # TODO: __add__
    # TODO: __len__
    # TODO: __getitem__, __setitem__
    # TODO: __call__
    # TODO: __enter__, __exit__
    # TODO: __and__, __or__
    # TODO: __hash__

    def start(self):
        self._status = "running"

    def stop(self):
        self._status = "stopped"

    def status(self):
        return self._status

# =====================
# Реализация DatabaseServer
# =====================
class DatabaseServer(Server):
    def __init__(self, name, ip, load=0):
        self.name = name
        self.ip = ip
        self.load = load
        self.processes = {}
        self._status = "stopped"

    # TODO: Реализовать все те же dunder методы, что и в WebServer

    def start(self):
        self._status = "running"

    def stop(self):
        self._status = "stopped"

    def status(self):
        return self._status

# =====================
# Функция-полиморфизм
# =====================
def manage_server(server: Server):
    server.start()
    print(f"{server.name} status: {server.status()}")
    server.stop()
    print(f"{server.name} status: {server.status()}")

# =====================
# Тестирование
# =====================
web = WebServer("Web1", "192.168.1.10", load=50)
db = DatabaseServer("DB1", "192.168.1.20", load=70)

manage_server(web)
manage_server(db)

# Пример использования dunder методов
# print(web)          # __str__
# print(repr(db))     # __repr__
# print(web == db)    # __eq__, __ne__
# print(web < db)     # __lt__, __gt__
# print(web + db)     # __add__
# print(len(web))     # __len__
# web["nginx"] = "running"  # __setitem__
# print(web["nginx"])        # __getitem__
# web("restart")      # __call__
# with db:            # __enter__ и __exit__
#     print(db.status())
# servers_set = {web, db}  # __hash__

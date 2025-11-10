# посмотреть dunder method: enter, exit, and, or, hash, ne

'''Что нужно сделать:
Создать абстрактный класс Server с методами start(), stop() и status().
Создать два наследника: WebServer и DatabaseServer.
Реализовать в этих классах dunder методы:
__init__, __repr__, __str__, __eq__, __ne__, __lt__, __gt__, __add__, __len__, 
__getitem__, __setitem__, __call__, __enter__,
 __exit__, __and__, __or__, __hash__.
Создать функцию manage_server(server: Server),
 которая будет работать с любым сервером,
   используя только интерфейс Server (полиморфизм).
Протестировать работу всех методов:
 объединение серверов, сравнение по нагрузке,
 доступ к процессам как к словарю, вызов сервера как функции,
 использование как контекстного менеджера и добавление серверов в множество.
При желании — придумать и реализовать
 1–2 своих dunder метода для расширения функционала.
---------------------------------------
HINT
Абстракция: используй ABC и @abstractmethod, чтобы создать общий интерфейс Server.
Полиморфизм: функция manage_server должна работать с любым объектом Server,
не зная его конкретного класса.
Dunder методы: подумай, как сервер можно сравнивать (__eq__, __lt__), объединять (__add__),
вызывать как функцию (__call__),
управлять процессами через словарь (__getitem__, __setitem__)
и использовать в контекстном менеджере (__enter__, __exit__).
Логические операции: можно реализовать __and__ и __or__, например, для объединения статусов серверов.
Хэширование: чтобы сервер можно было использовать в set или как ключ в dict, реализуй __hash__.
'''

from abc import ABC, abstractmethod
from random import randint

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

    def __get_ip__(self):
        return self.ip
    
    @staticmethod
    def __dhcp__():
        ip = str(randint(1, 254))
        print(ip)
        return ip

class WebServer(Server):
    def __init__(self, name, ip=None, load=0):
        self.name = name
        self.ip = ip
        self.load = load
        self.processes = {}
        self._status = 'stopped'

    def start(self):
        self._status = "running"

    def stop(self):
        self._status = "stopped"

    def status(self):
        return self._status
    
    def __str__(self):
        return f"{self.name}: {self.ip}, {self.load}"
    
    def __repr__(self):
        return (f"-> Server: {self.name}\n"
                f"Ip: {self.ip}\n"
                f"Load: {self.load}\n"
                f"Status: {self.status()}\n")
    
    def __eq__(self, other):
        if not isinstance(other, Server):
            return NotImplemented
        return self.load == other.load
    
    def __ne__(self, other):
        if not isinstance(other, Server):
            return NotImplemented
        return self.load != other.load
    
    def __lt__(self, other):
        if not isinstance(other, Server):
            return NotImplemented
        return self.load < other.load
    
    def __gt__(self, other):
        if not isinstance(other, Server):
            return NotImplemented
        return self.load > other.load
    
    def __add__(self, other):
        if not isinstance(other, Server):
            return NotImplemented
        return (WebServer(f"{self.name} + {other.name}", 
                        '192.168.1.' + Server.__dhcp__(),
                        self.load + other.load)
                )

    def __len__(self):
        return len(self.name)
    
    def __call__(self, action):
        return print(f"{self.name} executes {action}") 

    def __getitem__(self, key):
        return self.processes[key]

    def __setitem__(self, key, value):
        self.processes[key] = value
    
    def __enter__(self):
        print('Opening connection')
    
    def __exit__(self):
        print('Closing connection')

    def __and__(self, other):
        if not isinstance(other, WebServer):
            return NotImplemented
        else:
            if self.status() == 'running' and other.status() == 'running':
                return WebServer(f"{self.name}&{other.name}", '192.168.1.' + Server.__dhcp__(), (self.load + other.load) / 2)
            else: return 'Infrastructure is DEGRADED' # what (type) should we return in else case?

    def __or__(self, other):
        if not isinstance(other, WebServer):
            return NotImplemented        
        if self.status() == 'running' or other.status() == 'running':
            return WebServer(f"{self.name}|{other.name}", '192.168.1.' + Server.__dhcp__(), self.load + other.load)
        else: return 'Infrastructure is DEGRADED'

    def __hash__(self):
        return hash((self.name, self.ip))

class DatabaseServer(Server):
    def __init__(self, name, ip, load=0):
        self.name = name
        self.ip = ip
        self.load = load
        self.processes = {}

    def __str__(self):
        return f"{self.name}: {self.ip}"
    
    def __repr__(self):
        return (f"-> Server: {self.name}\n"
                f"Ip: {self.ip}\n"
                f"Load: {self.load}\n"
                f"Status: {self.status()}\n")

    def __eq__(self, other):
        if not isinstance(other, Server):
            return NotImplemented
        return self.load == other.load
    
    def __ne__(self, other):
        if not isinstance(other, Server):
            return NotImplemented
        return self.load != other.load
    
    def __lt__(self, other):
        if not isinstance(other, Server):
            return NotImplemented
        return self.load < other.load
    
    def __gt__(self, other):
        if not isinstance(other, Server):
            return NotImplemented
        return self.load > other.load
    
    def __add__(self, other):
        if not isinstance(other, Server):
            return NotImplemented
        return (DatabaseServer(f"{self.name} + {other.name}", 
                        '192.168.1.' + Server.__dhcp__(),
                        self.load + other.load)
                )

    def __and__(self, other):
        if not isinstance(other, DatabaseServer):
            return NotImplemented
        else:
            if self.status() == 'running' and other.status() == 'running':
                return DatabaseServer(f"{self.name}&{other.name}", self.ip, (self.load + other.load) / 2)
            else: return 'Infrastructure is DEGRADED' # what (type) should we return in else case?

    def __or__(self, other):
        if not isinstance(other, DatabaseServer):
            return NotImplemented        
        if self.status() == 'running' or other.status() == 'running':
            return DatabaseServer(f"{self.name}|{other.name}", self.ip, self.load + other.load)
        else: return 'Infrastructure is DEGRADED'

    def __len__(self):
        return len(self.name)
    
    def __call__(self, action):
        return print(f"{self.name} executes {action}")

    def __getitem__(self, key):
        return self.processes[key]

    def __setitem__(self, key, value):
        self.processes[key] = value  

    def __enter__(self):
        print('Opening connection')
    
    def __exit__(self, exc_type, exc_value, traceback):
        print('Closing connection')
    
    def start(self):
        self._status = "running"

    def stop(self):
        self._status = "stopped"

    def status(self):
        return self._status        

    def __hash__(self):
        return hash((self.name, self.ip))

def manage_server(server: Server, action = None):
    if action == 'start':
        server.start()
        print(f"{server.name} status: {server.status()}")
    elif action == 'stop':
        server.stop()
        print(f"{server.name} status: {server.status()}")
    else: 
        print('Action must be `start` or `stop`')


web = WebServer("Web1", "192.168.1.10", load=50)
web1 = WebServer("Web2", "192.168.1.11", load=50)
db = DatabaseServer("DB1", "192.168.1.20", load=70)
        
manage_server(web, 'start')
manage_server(web1, 'start')
manage_server(db, 'start')

# Testing
# print(web)          # __str__
# print(repr(db))     # __repr__
# print(web == db)    # __eq__, __ne__
# print(web < db)     # __lt__, __gt__
# print(web + db)     # __add__
# print(len(web))     # __len__
# web["nginx"] = "running"  # __setitem__
# web["haproxy"] = "stopped"
# print(web["nginx"])        # __getitem__
# web("restart")      # __call__
# with db:            # __enter__ и __exit__
#     print('Getting status: ', db.status())
# servers_set = {web, db}  # __hash__
# print(web & web1)
# print(web | web1)
# print(hash(web1))

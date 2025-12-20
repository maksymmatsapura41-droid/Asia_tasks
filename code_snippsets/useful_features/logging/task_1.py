class Server:
    def __init__(self, name, ip, status=None):
        self._name = name
        self._ip = ip
        self.status = status

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status in ['running', 'stopped']:
            self._status = status
        else:
            self._status = None
            print(f'Not valid status: `{status}`')

    def ping(self):
        if self._status == 'running':
            print(f'Server {self._name} is online')
        else:
            print(f'Server {self._name} is offline')

    def info(self):
        return f'server name {self._name}, ip {self._ip}, status {self._status}'


class WebServer(Server):
    def __init__(self, name, ip, status, requests_per_minute):
        super().__init__(name, ip, status)
        self.__requests_per_minute = requests_per_minute

    def info(self):
        return (
            f"server_name: {self._name},\n"
            f"ip: {self._ip},\n"
            f"status: {self._status},\n"
            f"requests_per_minute: {self.__requests_per_minute}"
        )


class DatabaseServer(Server):
    def __init__(self, name, ip, status, active_connections):
        super().__init__(name, ip, status)
        self.__active_connections = active_connections

    def info(self):
        return (
            f"server_name: {self._name},\n"
            f"ip: {self._ip},\n"
            f"status: {self._status},\n"
            f"active_connections: {self.__active_connections}"
        )


class FileServer(Server):
    def __init__(self, name, ip, status, storage_usage):
        super().__init__(name, ip, status)
        self.__storage_usage = storage_usage

    def info(self):
        return (
            f"server_name: {self._name},\n"
            f"ip: {self._ip},\n"
            f"status: {self._status},\n"
            f"storage_usage: {self.__storage_usage}"
        )


web1 = WebServer('jenkins', '192.168.10.2', 'running', 500)
print(web1.__dict__)
web2 = WebServer('nexus', '192.168.10.5', 'running', 1500)
print('----- WEB -----')
print(web1.info())
print('Current status:', web1.status)
web1.ping()
web1.status = 'running'
print('--------------')
print(web2.info())
web2.ping()
web2.status = 'stopped'
print('Current status:', web2.status)

# print('----- DB -----')
# db1 = DatabaseServer('d1', '192.168.10.10', 'degraded', 1000)
# db2 = DatabaseServer('d2', '192.168.10.11', 'running', 1200)
# print(db1.info())
# print('Current status:', db1.status)
# db1.ping()
# db1.status = 'failed'
# print('--------------')
# print(db2.info())
# db2.ping()
# db2.status = 'stopped'
# print('Current status:', db2.status)
#
# print('----- FS -----')
# fs1 = FileServer('fs1', '192.168.10.20', 'failed', 0)
# fs2 = FileServer('fs2', '192.168.10.21', 'running', 2000)
#
# print(fs1.info())
# print('Current status:', fs1.status)
# fs1.ping()
# fs1.status = 'failed'
# print('--------------')
# print(fs2.info())
# fs2.ping()
# fs2.status = 'stopped'
# print('Current status:', fs2.status)

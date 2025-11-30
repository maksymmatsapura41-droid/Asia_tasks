from loguru import logger
logger.add(
    "logs/servers.log",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    rotation="1 MB",
    retention="7 days"
)


class Server:
    def __init__(self, name, ip, status=None):
        self._name = name
        self._ip = ip
        self.status = status
        logger.info(f"Created server: name={name}, ip={ip}, status={status}")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status in ['running', 'stopped']:
            logger.info(f"Status changed: {self._name} -> {status}")
            self._status = status
        else:
            logger.warning(f"Invalid status '{status}' for server {self._name}")
            self._status = None

    def ping(self):
        if self._status == 'running':
            logger.info(f"Ping OK: {self._name} ({self._ip})")
            print(f"Server {self._name} is online")
        else:
            logger.error(f"Ping FAILED: {self._name} ({self._ip})")
            print(f"Server {self._name} is offline")

    def info(self):
        msg = f"server name {self._name}, ip {self._ip}, status {self._status}"
        logger.debug(f"Info requested: {msg}")
        return msg


class WebServer(Server):
    def __init__(self, name, ip, status, requests_per_minute):
        super().__init__(name, ip, status)
        self.__requests_per_minute = requests_per_minute
        logger.info(f"WebServer extra param: rpm={requests_per_minute}")

    def info(self):
        msg = (
            f"server_name: {self._name}, "
            f"ip: {self._ip}, "
            f"status: {self._status}, "
            f"requests_per_minute: {self.__requests_per_minute}"
        )
        logger.debug(f"Info requested: {msg}")
        return msg


class DatabaseServer(Server):
    def __init__(self, name, ip, status, active_connections):
        super().__init__(name, ip, status)
        self.__active_connections = active_connections
        logger.info(f"DatabaseServer extra param: active_connections={active_connections}")

    def info(self):
        msg = (
            f"server_name: {self._name}, "
            f"ip: {self._ip}, "
            f"status: {self._status}, "
            f"active_connections: {self.__active_connections}"
        )
        logger.debug(f"Info requested: {msg}")
        return msg


class FileServer(Server):
    def __init__(self, name, ip, status, storage_usage):
        super().__init__(name, ip, status)
        self.__storage_usage = storage_usage
        logger.info(f"FileServer extra param: storage_usage={storage_usage}")

    def info(self):
        msg = (
            f"server_name: {self._name}, "
            f"ip: {self._ip}, "
            f"status: {self._status}, "
            f"storage_usage: {self.__storage_usage}"
        )
        logger.debug(f"Info requested: {msg}")
        return msg



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

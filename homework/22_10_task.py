''' Описание
Представь, что ты разрабатываешь простую систему мониторинга ИТ-инфраструктуры.
 Есть разные типы серверов — веб-серверы, базы данных, файловые серверы.
 Все они имеют общие параметры (название, IP-адрес, статус), но также — свои специфические метрики.
Создай базовый класс Server, который имеет:
защищённые атрибуты _name, _ip, _status;
метод info() — возвращает короткую информацию о сервере;
метод ping() — имитирует проверку связи (например, возвращает "Server <name> is online").
Реализуй инкапсуляцию для _status:
разрешённые значения: "running" или "stopped";
если задано другое значение — вывести сообщение об ошибке.

Создай классы-наследники:
WebServer(Server) — приватный атрибут __requests_per_minute;
DatabaseServer(Server) — приватный атрибут __active_connections;
FileServer(Server) — приватный атрибут __storage_usage.

В каждом классе-наследнике:
переопредели метод info(), чтобы показывал и специфические метрики.'''

class Server:
    def __init__(self, name, ip, status):
        self._name = name
        self._ip = ip
        self._status = status
    
    @property
    def status(self):
        return self._status
    
    @status.setter # can setter exist without getter?
    def status(self, status):
        if status in ['running', 'stopped']:
            self._status = status
        else:
            print(f'Not valid status {self._status}')
    
    def ping(self):
        if self._status == 'running':
            print(f'Server {self._name} is online')
        else: 
            print(f'Server {self._name} is offline')

    def info(self):
        return f'server name {self._name}, ip {self._ip}, status {self._status}'

class WebServer(Server):
    def __init__(self, name, ip, status,  requests_per_minute):
        super().__init__(name, ip, status)
        self.__requests_per_minute = requests_per_minute
    
    def info(self):
        return f'''
                server_name: {self._name},
                ip: {self._ip}, 
                status: {self._status}, 
                requests_per_minute: {self.__requests_per_minute}
                '''
        # TODO: how to make multiline string look good

class DatabaseServer(Server):
    def __init__(self, name, ip, status, active_connections):
        super().__init__(name, ip, status)
        self.__active_connections = active_connections

    def info(self):
        return f'''
                server_name: {self._name}, 
                ip: {self._ip}, 
                status: {self._status}, 
                active_connections: {self.__active_connections}
                '''    

class FileServer(Server):
    def __init__(self, name, ip, status, storage_usage):
        super().__init__(name, ip, status)
        self.__storage_usage = storage_usage

    def info(self):
        return f'''
                server_name: {self._name},
                ip: {self._ip}, 
                status: {self._status}, 
                storage_usage: {self.__storage_usage}
                '''.strip()   


web1 = WebServer('jenkins', '192.168.10.2', 'running', 500)
web2 = WebServer('nexus', '192.168.10.5', 'running', 1500)
print('----- WEB -----')
print(web1.info())
print('Status:', web1.status)
web1.ping()
web1.status = 'failed'
print(web2.info())
web2.ping()
web2.status = 'stopped'
print('Status:', web2.status)

print('----- DB -----')
db1 = DatabaseServer('d1', '192.168.10.10', 'degraded', 1000)
db2 = DatabaseServer('d2', '192.168.10.11', 'running', 1200)
print(db1.info())
print('Status:', db1.status)
db1.ping()
db1.status = 'failed'
print(db2.info())
db2.ping()
db2.status = 'stopped'
print('Status:', db2.status)

print('----- FS -----')
fs1 = FileServer('fs1', '192.168.10.20', 'failed', 0)
fs2 = FileServer('fs2', '192.168.10.21', 'running', 2000)

print(fs1.info())
print('Status:', fs1.status)
fs1.ping()
fs1.status = 'failed'
print(fs2.info())
fs2.ping()
fs2.status = 'stopped'
print('Status:', fs2.status)
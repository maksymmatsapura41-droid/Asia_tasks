class Server:
    def __init__(self, name, ip, status):
        self._name = name
        self._ip = ip
        self._status = status

    # TODO: добавить геттер и сеттер для status (только "running" или "stopped")
    # TODO: метод info()
    # TODO: метод ping()


class WebServer(Server):
    def __init__(self, name, ip, status, requests_per_minute):
        # TODO: вызвать инициализацию Server
        # TODO: создать приватный атрибут __requests_per_minute
        pass

    # TODO: переопределить info()


# class DatabaseServer(Server): ...
# class FileServer(Server): ...


if __name__ == "__main__":
    # TODO: создать несколько серверов и проверить работу методов
    pass

from dataclasses import dataclass
from datetime import datetime

@dataclass
class Image:
    name: str
    tag: str
    size_mb: int
    created_at: datetime

    def __post_init__(self):
        # TODO: проверить, что size_mb > 0
        pass

    def full_name(self) -> str:
        # TODO: вернуть строку "<name>:<tag>"
        pass

    def age_days(self) -> int:
        # TODO: вернуть возраст образа в днях
        pass


class Repository:
    def __init__(self, name: str):
        # TODO: инициализировать name и список образов
        pass

    def add(self, image: Image):
        # TODO: добавить образ в список
        pass

    def remove(self, name: str, tag: str):
        # TODO: удалить образ по имени и тегу
        pass

    def find(self, name: str):
        # TODO: вернуть список образов с указанным именем
        pass

    def cleanup(self, max_age_days: int):
        # TODO: удалить образы старше max_age_days
        pass

    def total_size(self) -> int:
        # TODO: вернуть суммарный размер всех образов
        pass

    def list_all(self) -> list[str]:
        # TODO: вернуть список строк с информацией об образах
        pass


class Registry:
    def __init__(self):
        # TODO: инициализировать словарь репозиториев
        pass

    def add_repo(self, repo: Repository):
        # TODO: добавить репозиторий в словарь
        pass

    def get_repo(self, name: str):
        # TODO: вернуть репозиторий по имени или None
        pass

    def total_size(self) -> int:
        # TODO: вернуть суммарный размер всех образов всех репозиториев
        pass

    def list_all(self) -> list[str]:
        # TODO: вернуть список строк всех образов всех репозиториев
        pass


if __name__ == "__main__":
    # TODO: создайте несколько объектов Image
    # TODO: создайте репозитории и добавьте образы
    # TODO: создайте Registry и добавьте репозитории
    # TODO: протестируйте методы list_all и total_size
    pass

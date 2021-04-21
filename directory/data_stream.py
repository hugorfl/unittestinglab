from abc import ABC, abstractmethod
from directory.contact import Contact
from typing import Any


class DataStream(ABC):
    @abstractmethod
    def add(self, contact: Contact):
        pass

    @abstractmethod
    def remove(self, contact: Contact):
        pass

    @abstractmethod
    def search(self, key: str, val: Any) -> list[Contact]:
        pass

    @abstractmethod
    def has(self, contact: Contact) -> bool:
        pass

from abc import ABC, abstractmethod
from typing import Any, List
from directory.contact import Contact


class DataStream(ABC):
    @abstractmethod
    def add(self, contact: Contact):
        pass

    @abstractmethod
    def remove(self, contact: Contact):
        pass

    @abstractmethod
    def search(self, key: str, val: Any) -> List[Contact]:
        pass

    @abstractmethod
    def has(self, contact: Contact) -> bool:
        pass

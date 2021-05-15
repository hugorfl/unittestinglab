from directory.contact import Contact
from directory.data_stream import DataStream
from typing import Any, List


class SpyDataStream(DataStream):
    def __init__(self):
        self.__contacts = {}

    def add(self, contact: Contact):
        self.__contacts[contact.email] = contact

    def remove(self, contact: Contact):
        del self.__contacts[contact.email]

    def search(self, key: str, val: Any) -> List[Contact]:
        contacts = []

        for _, contact in self.__contacts.items():
            v = getattr(contact, key)
            if val == v:
                contacts.append(contact)

        return contacts

    def has(self, contact: Contact) -> bool:
        return contact.email in self.__contacts

    @property
    def contacts(self) -> List[Contact]:
        return list(self.__contacts.values())

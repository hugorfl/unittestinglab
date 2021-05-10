from typing import Optional
from .contact import Contact
from .data_stream import DataStream


class Directory:
    def __init__(self, stream: DataStream):
        self.__stream = stream

    def add_contact(self, contact: Contact):
        if self.__stream.has(contact):
            raise ValueError(f"Contact '{contact.email}' already added")

        self.__stream.add(contact)

    def remove_contact(self, contact: Contact):
        if not self.__stream.has(contact):
            raise ValueError(f"Contact '{contact.email}' does not exists")

        self.__stream.remove(contact)

    def contact_by_email(self, email: str) -> Optional[Contact]:
        contacts = self.__stream.search('email', email)
        return contacts[0] if contacts else None

    def contacts_by_age(self, age: int) -> list[Contact]:
        return self.__stream.search('age', age)

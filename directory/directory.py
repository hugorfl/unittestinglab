from typing import Optional, List
import logging
from .contact import Contact
from .data_stream import DataStream


class Directory:
    def __init__(self, stream: DataStream):
        self.__stream = stream

    def add_contact(self, contact: Contact):
        if self.__stream.has(contact):
            err_str = f"Contact '{contact}' already added"
            logging.error(err_str)
            raise ValueError(err_str)

        self.__stream.add(contact)
        logging.info("Contact '%s' added successfully", contact)

    def remove_contact(self, contact: Contact):
        if not self.__stream.has(contact):
            err_str = f"Contact '{contact}' does not exist"
            logging.error(err_str)
            raise ValueError(err_str)

        self.__stream.remove(contact)
        logging.info("Contact '%s' removed successfully", contact)

    def contact_by_email(self, email: str) -> Optional[Contact]:
        contacts = self.__stream.search('email', email)
        return contacts[0] if contacts else None

    def contacts_by_age(self, age: int) -> List[Contact]:
        return self.__stream.search('age', age)

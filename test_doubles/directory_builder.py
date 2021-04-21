from directory.contact import Contact
from directory.directory import Directory
from test_doubles.spy_data_stream import SpyDataStream


class DirectoryBuilder:
    def __init__(self):
        self.__contacts = []

    def with_contact(self, contact: Contact) -> 'DirectoryBuilder':
        self.__contacts.append(contact)

        return self

    def build(self, stream: SpyDataStream) -> Directory:
        d = Directory(stream)
        self.__add_all_contacts(d)

        return d

    def __add_all_contacts(self, d: Directory):
        for c in self.__contacts:
            d.add_contact(c)

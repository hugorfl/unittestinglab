"""
1 - Given the math.ceil function, Define a set of unit test cases that exercise the function
2 - Given the filecmp.cmp function, Define a set of test cases that exercise the function
3 - Implement a class that manages a directory that is saved in a text file. The data saved
    includes:
        a. Name
        b. Email
        d. Country of Origin
        c. Age
    The class should have capabilities to:
        - Add new record
        - Delete a record
        - Look for a record by mail and age
        - List on screen all record information

Note: Remember Right BICEP

:authors: - Hugo Rodríguez
"""

import unittest
from math import ceil
from filecmp import cmp
from typing import Any, Optional
from abc import ABC, abstractmethod

"""
Test Cases:

1 [TTP] Same zero and positive integer is returned
2 [TTP] Same negative integer is returned
3 [TTP] Zero and positive floats with several decimals rounds up
4 [TTP] Negative decimal floats with several decimals rounds up (E.g. -3.709 -> -3)
5 [TTF] Passing stringified zero and positive float number
6 [TTF] Passing stringified negative float number
7 [TTF] Passing other data types other than ints and floats
8 [TTF] Passing None
"""
class CeilTest(unittest.TestCase):
    def test_pass_same_passed_zero_n_positive_int_is_returned(self):
        self.assertEqual(0, ceil(0))
        self.assertEqual(4, ceil(4))
        self.assertEqual(2048, ceil(2048))
        self.assertEqual(9876543210, ceil(9876543210))
        
    def test_pass_same_negative_int_is_returned(self):
        self.assertEqual(-4, ceil(-4))
        self.assertEqual(-2048, ceil(-2048))
        self.assertEqual(-9876543210, ceil(-9876543210))

    def test_pass_zero_n_positive_floats_with_several_decimals_passed_rounds_up(self):
        self.assertEqual(1, ceil(0.000000000001))
        self.assertEqual(2, ceil(1.00000009))
        self.assertEqual(4, ceil(3.709))
        self.assertEqual(178, ceil(177.9876543210))
        self.assertEqual(5, ceil(4.55))
        self.assertEqual(9876543211, ceil(9876543210.9876543210))

    def test_pass_negative_floats_with_several_decimals_passed_rounds_up(self):
        self.assertEqual(0, ceil(-0.000000000009))
        self.assertEqual(-3, ceil(-3.709))
        self.assertEqual(-256, ceil(-256.9876543210))
        self.assertEqual(-4, ceil(-4.55))
        self.assertEqual(-9876543210, ceil(-9876543210.9876543210))

    def test_fail_stringified_zero_and_positive_float_numbers_passed(self):
        with self.assertRaises(TypeError):
            ceil("0")

        with self.assertRaises(TypeError):
            ceil("14.5")

        with self.assertRaises(TypeError):
            ceil("9876543210.9876543210")

    def test_fail_stringified_negative_float_numbers_passed(self):
        with self.assertRaises(TypeError):
            ceil("-14.5")

        with self.assertRaises(TypeError):
            ceil("-9876543210.9876543210")

    def test_fail_other_types_than_ints_or_floats_passed(self):
        with self.assertRaises(TypeError):
            ceil(-14.5+9j)

        with self.assertRaises(TypeError):
            ceil([14.5])

        with self.assertRaises(TypeError):
            ceil((14.5,))

        with self.assertRaises(TypeError):
            ceil({14.5: 14.5})

    def test_fail_none_passed(self):
        with self.assertRaises(TypeError):
            ceil(None)

"""
Test Cases:
1 [TTP] Identical files compared
2 [TTF] Non equal files compared
3 [TTF] Non existing file compared to an existing one
4 [TTF] Passing None
"""
class FileCmpTest(unittest.TestCase):
    def test_pass_identical_files_compared(self):
        self.assertTrue(cmp('./lorem-ipsum2.txt', './lorem-ipsum3.txt', False))

    def test_fail_non_equal_files_compared(self):
        self.assertFalse(cmp('./lorem-ipsum.txt', './lorem-ipsum2.txt', False))
    
    def test_fail_non_existing_file_compared_to_existing(self):
        with self.assertRaises(FileNotFoundError):
            cmp('./corporate-ipsum.txt', './lorem-ipsum.txt', False)

    def test_fail_none_passed(self):
        with self.assertRaises(TypeError):
            cmp(None, None, False)

class Contact:
    def __init__(self, name: str, email: str, country: str, age: int):
        self.__name = name
        self.__email = email
        self.__country = country
        self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email(self) -> str:
        return self.__email

    @property
    def country(self) -> str:
        return self.__country

    @property
    def age(self) -> int:
        return self.__age

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Contact):
            return NotImplemented

        return self.__name == o.__name \
            and self.__email == o.__email \
            and self.__country == o.__country \
            and self.__age == o.__age

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

class Directory:
    def __init__(self, stream: DataStream):
        self.__stream = stream

    def addContact(self, contact: Contact):
        if self.__stream.has(contact): raise ValueError(f"Contact '{contact.email}' already added")
        self.__stream.add(contact)

    def removeContact(self, contact: Contact):
        if not self.__stream.has(contact): raise ValueError(f"Contact '{contact.email}' does not exists")
        self.__stream.remove(contact)

    def contactByEmail(self, email: str) -> Optional[Contact]:
        contacts = self.__stream.search('email', email)
        return contacts[0] if contacts else None

    def contactsByAge(self, age: int) -> list[Contact]:
        return self.__stream.search('age', age)
        

class SpyDataStream(DataStream):
    def __init__(self):
        self.__contacts = {}

    def add(self, contact: Contact):
        self.__contacts[contact.email] = contact

    def remove(self, contact: Contact):
        del self.__contacts[contact.email]

    def search(self, key: str, val: Any) -> list[Contact]:
        contacts = []

        for email, contact in self.__contacts.items():
            v = getattr(contact, key)
            if val == v:
                contacts.append(contact)

        return contacts

    def has(self, contact: Contact) -> bool:
        return contact.email in self.__contacts

    @property
    def contacts(self) -> list[Contact]:
        return list(self.__contacts.values())


class DirectoryBuilder:
    def __init__(self):
        self.__contacts = []

    def withContact(self, contact: Contact) -> 'DirectoryBuilder':
        self.__contacts.append(contact)

        return self

    def build(self, stream: SpyDataStream) -> Directory:
        d = Directory(stream)
        self.__addAllContacts(d)

        return d

    def __addAllContacts(self, d: Directory):
        for c in self.__contacts:
            d.addContact(c)

"""
Test Cases:
1 [TTP] Can add new record
2 [TTP] No other records are added
3 [TTF] Cannot add same record more than once
4 [TTP] Can delete existing record
5 [TTP] Won't delete other records
6 [TTF] Cannot delete non-existing record
7 [TTP] Can retrieve record by mail
8 [TTP] Non matching email wont retrieve records
9 [TTP] Can retrieve record by age
10 [TTP] Non matching age wont retrieve records
"""
class DirectoryManagerTest(unittest.TestCase):

    def test_pass_can_add_new_record(self):
        s = SpyDataStream()
        d = self.__a_directory() \
            .build(s)

        d.addContact(self.__a_contact())

        self.assertEqual(s.contacts[0], self.__a_contact())

    def test_pass_no_other_records_are_added(self):
        s = SpyDataStream()
        d = self.__a_directory() \
            .build(s)

        d.addContact(self.__a_contact())

        self.assertEqual(len(s.contacts), 1)

    def test_fail_cannot_add_same_contact_twice(self):
        d = self.__a_directory() \
            .withContact(self.__a_contact()) \
            .build(SpyDataStream())

        with self.assertRaises(ValueError):
            d.addContact(self.__a_contact())

    def test_pass_can_delete_existing_record(self):
        s = SpyDataStream()
        d = self.__a_directory() \
            .withContact(self.__a_contact()) \
            .build(s)

        d.removeContact(self.__a_contact())

        self.assertFalse(s.has(self.__a_contact()))

    def test_pass_no_other_records_are_deleted(self):
        s = SpyDataStream()
        d = self.__a_directory() \
            .withContact(self.__a_contact()) \
            .withContact(self.__other_contact()) \
            .build(s)

        d.removeContact(self.__a_contact())

        self.assertEqual(len(s.contacts), 1)

    def test_fail_cannot_delete_non_existing_record(self):
        d = self.__a_directory() \
            .withContact(self.__other_contact()) \
            .build(SpyDataStream())
            
        with self.assertRaises(ValueError):
            d.removeContact(self.__a_contact())

    def test_pass_can_retrieve_record_by_email(self):
        d = self.__a_directory() \
            .withContact(self.__a_contact()) \
            .withContact(self.__other_contact()) \
            .build(SpyDataStream())

        c = d.contactByEmail('diana@test.com')

        self.assertEqual(c, self.__other_contact())

    def test_pass_non_matching_email_wont_retrieve_any_records(self):
        d = self.__a_directory() \
            .withContact(self.__a_contact()) \
            .withContact(self.__other_contact()) \
            .build(SpyDataStream())

        self.assertIsNone(d.contactByEmail('arturo@test.com'))

    def test_pass_can_retrieve_records_by_age(self):
        d = self.__a_directory() \
            .withContact(self.__a_contact()) \
            .withContact(self.__other_contact()) \
            .build(SpyDataStream())

        self.assertListEqual(d.contactsByAge(28), [self.__a_contact(), self.__other_contact()])

    def test_pass_non_matching_age_wont_retrieve_any_records(self):
        d = self.__a_directory() \
            .withContact(self.__a_contact()) \
            .withContact(self.__other_contact()) \
            .build(SpyDataStream())

        self.assertListEqual(d.contactsByAge(45), [])

    def __a_directory(self) -> DirectoryBuilder:
        return DirectoryBuilder()

    def __a_contact(self) -> Contact:
        return Contact('Hugo', 'hugo@test.com', 'Mexico', 28)

    def __other_contact(self) -> Contact:
        return Contact('Diana', 'diana@test.com', 'Mexico', 28)


if __name__ == '__main__':
    unittest.main()
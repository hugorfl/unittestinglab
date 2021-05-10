"""
1 - Given the math.ceil function, Define a set of unit test cases that
    exercise the function
2 - Given the filecmp.cmp function, Define a set of test cases that exercise
    the function
3 - Implement a class that manages a directory that is saved in a text file.
    The data saved includes:
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
from directory.contact import Contact
from test_doubles.directory_builder import DirectoryBuilder
from test_doubles.spy_data_stream import SpyDataStream

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
        datastream = SpyDataStream()
        directory = self.__a_directory()\
            .build(datastream)

        directory.add_contact(self.__a_contact())

        self.assertEqual(datastream.contacts[0], self.__a_contact())

    def test_pass_no_other_records_are_added(self):
        datastream = SpyDataStream()
        directory = self.__a_directory()\
            .build(datastream)

        directory.add_contact(self.__a_contact())

        self.assertEqual(len(datastream.contacts), 1)

    def test_fail_cannot_add_same_contact_twice(self):
        directory = self.__a_directory()\
            .with_contact(self.__a_contact())\
            .build(SpyDataStream())

        with self.assertRaises(ValueError):
            directory.add_contact(self.__a_contact())

    def test_pass_can_delete_existing_record(self):
        datastream = SpyDataStream()
        directory = self.__a_directory()\
            .with_contact(self.__a_contact())\
            .build(datastream)

        directory.remove_contact(self.__a_contact())

        self.assertFalse(datastream.has(self.__a_contact()))

    def test_pass_no_other_records_are_deleted(self):
        datastream = SpyDataStream()
        directory = self.__a_directory()\
            .with_contact(self.__a_contact())\
            .with_contact(self.__other_contact())\
            .build(datastream)

        directory.remove_contact(self.__a_contact())

        self.assertEqual(len(datastream.contacts), 1)

    def test_fail_cannot_delete_non_existing_record(self):
        directory = self.__a_directory()\
            .with_contact(self.__other_contact())\
            .build(SpyDataStream())

        with self.assertRaises(ValueError):
            directory.remove_contact(self.__a_contact())

    def test_pass_can_retrieve_record_by_email(self):
        directory = self.__a_directory()\
            .with_contact(self.__a_contact())\
            .with_contact(self.__other_contact())\
            .build(SpyDataStream())

        contact = directory.contact_by_email('diana@test.com')

        self.assertEqual(contact, self.__other_contact())

    def test_pass_non_matching_email_wont_retrieve_any_records(self):
        directory = self.__a_directory()\
            .with_contact(self.__a_contact())\
            .with_contact(self.__other_contact())\
            .build(SpyDataStream())

        self.assertIsNone(directory.contact_by_email('arturo@test.com'))

    def test_pass_can_retrieve_records_by_age(self):
        directory = self.__a_directory()\
            .with_contact(self.__a_contact())\
            .with_contact(self.__other_contact())\
            .build(SpyDataStream())

        self.assertListEqual(
            directory.contacts_by_age(28),
            [self.__a_contact(), self.__other_contact()]
        )

    def test_pass_non_matching_age_wont_retrieve_any_records(self):
        directory = self.__a_directory()\
            .with_contact(self.__a_contact())\
            .with_contact(self.__other_contact())\
            .build(SpyDataStream())

        self.assertListEqual(directory.contacts_by_age(45), [])

    @staticmethod
    def __a_directory() -> DirectoryBuilder:
        return DirectoryBuilder()

    @staticmethod
    def __a_contact() -> Contact:
        return Contact('Hugo', 'hugo@test.com', 'Mexico', 28)

    @staticmethod
    def __other_contact() -> Contact:
        return Contact('Diana', 'diana@test.com', 'Mexico', 28)


if __name__ == '__main__':
    unittest.main()

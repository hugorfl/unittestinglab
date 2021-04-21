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

        return self.__name == o.__name\
            and self.__email == o.__email\
            and self.__country == o.__country\
            and self.__age == o.__age

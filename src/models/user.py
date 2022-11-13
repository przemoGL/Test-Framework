class User:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        self.email = self.name.lower()+'.'+self.surname.lower()+'@globallogic.com'

    def __str__(self) -> str:
        return self.name + self.surname + f'\n{self.email}'
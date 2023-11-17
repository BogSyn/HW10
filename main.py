from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.valid()

    def valid(self):
        if len(self.value) == 10 and self.value.isdigit():
            pass
        else:
            raise ValueError(f'Phone {self.value} not valid')


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

        # метод додавання телефону
    def add_phone(self, input_phone: str):
        phone = Phone(input_phone)
        # phone.valid(input_phone)
        if phone.value not in [p.value for p in self.phones]:
            self.phones.append(phone)
            print(f"{phone} successfully added.")
        else:
            print(f"{phone} is already added.")

    # видаляє телефон, або виводить, що немає номеру в всписку
    def remove_phone(self, phone: str):
        if phone in [p.value for p in self.phones]:
            self.phones.remove(
                self.phones[[p.value for p in self.phones].index(phone)])
            print(f"{phone} successfully removed")
        else:
            print(f"{phone} not found in the list of phones.")

    # редагує номер
    def edit_phone(self, old_phone, new_phone):
        phone = Phone(new_phone)
        if old_phone in [p.value for p in self.phones]:
            position = [p.value for p in self.phones].index(old_phone)
            self.phones.remove(self.phones[position])
            self.phones.insert(position, phone)
            print(f"{phone} successfully adited.")
        else:
            raise ValueError(f"{phone} not found in the list of phones.")

    # пошук номеру телефону
    def find_phone(self, phone):
        phone = Phone(phone)
        if phone.value in [p.value for p in self.phones]:
            print(f"{self.name.value}: {phone}")
            return phone
        else:
            print(f"{phone} not in {self.name.value} contacts")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    # додає запис до self.data.
    def add_record(self, record):
        self.data[record.name.value] = record

    # знаходить за ім'ям.
    def find(self, name):
        if name in self.data.keys():
            return self.data[name]
        else:
            print(f"{name} not found")

    # видаляє запис за ім'ям.
    def delete(self, name):
        if name in self.data.keys():
            del self.data[name]
            print(f"{name} is delete")
        else:
            print(f"{name} not found")



"""
3 ways to type dictionary
"""
# pros: less setup
# cons: difficult to read, difficult to access the data
type Person = dict[str, str | int | dict[str, str] | dict[str, list[str] | dict[str, str]]]

def solution1():
    person: Person = {
        'name': 'Bob',
        'age': 29,
        'email': 'bob@email.com',
        'address': {
            'street': '42 Bob Avenue',
            'city': 'Sydney',
            'state': 'NSW',
            'postal_code': '2000',
            'country': 'Australia'
        },
        'contacts': {
            'phone_numbers': ['+61 808 123 456', '+61 808 654 321'],
            'emergency_contact': {
                'name': 'Bob',
                'relationship': 'Father',
                'phone': '+61 808 111 222'
            }
        }
    }

    print(person['name'])
    print(person['contacts']['emergency_contact']['name'])

# pros: easy to read
# cons: a lot of setup, difficult to access the data
from typing import TypedDict
class EmergencyContact(TypedDict):
    name: str
    relationship: str
    phone: str

class Contacts(TypedDict):
    phone_numbers: list[str]
    emergency_contact: EmergencyContact

class Address(TypedDict):
    street: str
    city: str
    state: str
    postal_code: str
    country: str

class Person(TypedDict):
    name: str
    age: int
    email: str
    address: Address
    contacts: Contacts

def solution2():
    person: Person = {
        'name': 'Bob',
        'age': 29,
        'email': 'bob@email.com',
        'address': {
            'street': '42 Bob Avenue',
            'city': 'Sydney',
            'state': 'NSW',
            'postal_code': '2000',
            'country': 'Australia'
        },
        'contacts': {
            'phone_numbers': ['+61 808 123 456', '+61 808 654 321'],
            'emergency_contact': {
                'name': 'Bob',
                'relationship': 'Father',
                'phone': '+61 808 111 222'
            }
        }
    }

    print(person['name'])
    print(person['contacts']['emergency_contact']['name'])

# pros: easy to access the data
# cons: a lot of setup
from dataclasses import dataclass
@dataclass
class EmergencyContact:
    name: str
    relationship: str
    phone: str

@dataclass
class Contacts:
    phone_numbers: list[str]
    emergency_contact: EmergencyContact

@dataclass
class Address:
    street: str
    city: str
    state: str
    postal_code: str
    country: str

@dataclass
class Person:
    name: str
    age: int
    email: str
    address: Address
    contacts: Contacts

def solution3():
    data = {
        'name': 'Bob',
        'age': 29,
        'email': 'bob@email.com',
        'address': {
            'street': '42 Bob Avenue',
            'city': 'Sydney',
            'state': 'NSW',
            'postal_code': '2000',
            'country': 'Australia'
        },
        'contacts': {
            'phone_numbers': ['+61 808 123 456', '+61 808 654 321'],
            'emergency_contact': {
                'name': 'Bob',
                'relationship': 'Father',
                'phone': '+61 808 111 222'
            }
        }
    }

    person: Person = Person(
        name=data['name'], 
        age=data['age'],
        email=data['email'],
        address=Address(
            street=data['address']['street'],
            city=data['address']['city'],
            state=data['address']['state'],
            postal_code=data['address']['postal_code'],
            country=data['address']['country']
        ),
        contacts=Contacts(
            phone_numbers=data['contacts']['phone_numbers'],
            emergency_contact=EmergencyContact(
                name=data['contacts']['emergency_contact']['name'],
                relationship=data['contacts']['emergency_contact']['relationship'],
                phone=data['contacts']['emergency_contact']['phone']
            )
        )
    )

    print(person.name)
    print(person.contacts.emergency_contact.name)

if __name__ == "__main__":
    solution1()
    solution2()
    solution3()

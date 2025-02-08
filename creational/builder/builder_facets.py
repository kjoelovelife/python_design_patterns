#!/usr/bin/env pytohn3
##########################################################################
# Copyright 2025 Wei-Chih Lin
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Wei-Chih Lin (weichih.lin@protonmail.com)
##########################################################################


class Person:
    def __init__(self):
        print('Creating an instance of Person')
        # address
        self.street_address = None
        self.postcode = None
        self.city = None
        # employment info
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self) -> str:
        return f'Address: {self.street_address}, {self.postcode}, {self.city}\n' +\
            f'Employed at {self.company_name} as a {self.postcode} earning {self.annual_income}'


class PersonBuilder:  # facade
    def __init__(self, person: Person = None):
        if person is None:
            self.person = Person()
        else:
            self.person = person

    @property
    def lives(self) -> 'PersonAddressBuilder':
        return PersonAddressBuilder(self.person)

    @property
    def works(self) -> 'PersonJobBuilder':
        return PersonJobBuilder(self.person)

    def build(self) -> Person:
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person: Person):
        super().__init__(person)

    def at(self, company_name: str) -> 'PersonJobBuilder':
        self.person.company_name = company_name
        return self

    def as_a(self, position: str) -> 'PersonJobBuilder':
        self.person.position = position
        return self

    def earning(self, annual_income: float) -> 'PersonJobBuilder':
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person: Person):
        super().__init__(person)

    def at(self, street_address: str):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode: str):
        self.person.postcode = postcode
        return self

    def in_city(self, city: str):
        self.person.city = city
        return self


if __name__ == '__main__':
    person_builder = PersonBuilder()
    person = person_builder\
        .lives\
            .at('123 London Road')\
            .in_city('London')\
            .with_postcode('SW12BC')\
        .works\
            .at('Fabrikam')\
            .as_a('Engineer')\
            .earning(123000)\
        .build()
    print(person)
    person2 = PersonBuilder().build()
    print(person2)

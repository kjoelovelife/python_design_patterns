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

from typing import Any

class CEO:
    __shared_state = {
        'name': 'Steve Jobs',
        'company': 'Apple',
        'salary': 1000000
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self) -> str:
        return f"{self.name} is the CEO of \
            {self.company} and makes {self.salary}"

class Monostate:
    __shared_state = {}
    def __new__(class_: 'Monostate', *args: Any, **kwargs: Any) -> 'CFO':
        obj = super(Monostate, class_).__new__(class_, *args, **kwargs)
        obj.__dict__ = class_.__shared_state
        return obj

class CFO(Monostate):
    def __init__(self):
        self.name = ''
        self.money_managed = 0

    def __str__(self) -> str:
        return f"{self.name} manages ${self.money_managed}"

def session_of_monostate_pattern():
    ceo1 = CEO()
    print(ceo1)

    ceo2 = CEO()
    ceo2.name = 'Tim Cook'
    print(ceo1)
    print(ceo2)

def monostate_into_a_base_class():
    cfo1 = CFO()
    cfo1.name = 'Sheryl Sandberg'
    cfo1.money_managed = 1000000
    print(cfo1)

    cfo2 = CFO()
    cfo2.name = 'Ruth Porat'
    cfo2.money_managed = 2000000
    print(cfo1)
    print(cfo2)

if __name__ == '__main__':
    #session_of_monostate_pattern()
    monostate_into_a_base_class()



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

from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('This tea is nice but I\'d prefer it with milk')


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount) -> Tea:
        print(f'Put in tea bag, boil water, pour {amount}ml, enjoy!')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount) -> Coffee:
        print(f'Grind some beans, boil water, pour {amount}ml, enjoy!')
        return Coffee()

class HotDrinkMachine:
    class AvailableDrink(Enum):  # violates OCP, have to modify this class to add more drinks
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            drink: Enum
            for drink in self.AvailableDrink:
                name = drink.name[0] + drink.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self) -> HotDrink:
        print('Available drinks:')
        factory: HotDrinkFactory
        for factory in self.factories:
            print(factory[0])

        drink_index = int(input(f'Please pick drink (0-{len(self.factories)-1}): '))
        amount = int(input(f'Specify amount: '))
        return self.factories[drink_index][1].prepare(amount)


def simle_approach():
    def make_drink(type: str):
        if type == 'tea':
            return TeaFactory().prepare(200)
        if type == 'coffee':
            return CoffeeFactory().prepare(50)
        return None
    
    entry = input('What kind of drink would you like?')
    drink = make_drink(entry)
    drink.consume()

if __name__ == '__main__':
    # simple_approach()

    hot_drink_machine = HotDrinkMachine()
    drink = hot_drink_machine.make_drink()
    drink.consume()

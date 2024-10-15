#!/usr/bin/env pytohn3
##########################################################################
# Copyright 2024 Wei-Chih Lin
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

from abc import ABC, abstractmethod
from enum import Enum
import typing

# Create Base calss for Relationship

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name

"""The following classes violates the dependency inversion principle.

class Relationships(list):
    def __init__(self):
        super().__init__()

    def add_parent_and_child(self, parent, child):
        self.append((parent, Relationship.PARENT, child))
        self.append((child, Relationship.CHILD, parent))

# dependency on a low-level module directly
# bad because strongly dependent on e.g. storage type
class Research:
    def __init__(self, relationships: Relationships):
        relation: typing.Tuple[Person, Relationship, Person]
        for relation in relationships:
            if relation[0].name == "John" and relation[1] == Relationship.PARENT:
                print(f"John has a child called {relation[2].name}")
"""

# The following classes follow the dependency inversion principle.
class RelationshipBrowser(ABC):
    @abstractmethod
    def find_all_children_of(self, name):
        pass

# This is a low-level module
class Relationships(list, RelationshipBrowser):
    def __init__(self):
        super().__init__()

    def add_parent_and_child(self, parent, child):
        self.append((parent, Relationship.PARENT, child))
        self.append((child, Relationship.CHILD, parent))
    
    def find_all_children_of(self, name):
        relation: typing.Tuple[Person, Relationship, Person]
        for relation in self:
            if relation[0].name == name and relation[1] == Relationship.PARENT:
                yield relation[2].name

class Research:
    def __init__(self, browser: RelationshipBrowser):
        for child in browser.find_all_children_of("Lucas"):
            print(f"Lucas has a child called {child}")

if __name__ == "__main__":
    parent = Person("Lucas")
    child1 = Person("Emma")
    child2 = Person("Copper")

    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)

    Research(relationships)
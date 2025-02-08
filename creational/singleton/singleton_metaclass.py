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

from typing import Type, TypeVar, Callable, Any
import random

ClassType = TypeVar('ClassType')

class Singleton(type):
    _instances = {}
    def __call__(class_: 'Singleton', *args: Any, **kwargs: Any) -> ClassType:
        if class_ not in class_._instances:
            class_._instances[class_] = \
                super(Singleton, class_).__call__(*args, **kwargs)
        return class_._instances[class_]
    
class Database(metaclass=Singleton):
    def __init__(self):
        self.id = random.randint(1, 101)
        print(f"Loading dataBase")

if __name__ == '__main__':
    database1 = Database()
    database2 = Database()
    print(database1.id, database2.id)
    print(database1 == database2)
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

import random

class Database:
    _instance = None

    def __init__(self):
        self.id = random.randint(1,101)
        print('Generated an id of ', self.id)
        print('Loading database from file')

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls)\
                .__new__(cls, *args, **kwargs)

        return cls._instance


    #def __init__(self):
    #    if not hasattr(self, 'id'):
    #        self.id = random.randint(1, 101)
    #        print('Generated an id of', self.id)
    #        print('Loading database from file')

database = Database()

if __name__ == '__main__':
    database1 = Database()
    database2 = Database()

    print(database1.id, database2.id)
    print(database1 == database2)
    print(database == database1)
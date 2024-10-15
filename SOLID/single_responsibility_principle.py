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

class Journal(list):
    def __init__(self):
        super().__init__()
        self.count = 0
    
    def add_entry(self, text):
        self.append(f'{self.count}: {text}')
        self.count += 1

    def remove_entry(self, index):
        del self[index]
    
    def __str__(self) -> str:
        return "\n".join(self)
    
    # the following methods are break the single responsibility principle
    def save(self, filename):
        with open(filename, "w") as file:
            file.write(str(self))
    
    def load(self, filename):
        pass

    def load_from_web(self, uri):
        pass

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, "w" ) as file:
            file.write(str(journal))

if __name__ == "__main__":
    journal = Journal()
    journal.add_entry("I cried today")
    journal.add_entry("I ate a bug")
    print(journal)

    PersistenceManager.save_to_file(journal, "journal.txt")
    with open("journal.txt") as file:
        print("After saving, read the content form the file:")
        print(file.read())
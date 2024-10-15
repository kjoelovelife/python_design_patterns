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

from abc import (ABC, abstractmethod)

# The following classes violates the interface segregation principle.
class Machine:
    def print_document(self, document: str):
        raise NotImplementedError

    def fax_document(self, document: str):
        raise NotImplementedError

    def scan_document(self, document: str):
        raise NotImplementedError

class MultiFunctionPrinter(Machine):
    def print_document(self, document: str):
        print(f"MutilFunctionPrinter is printing: {document}")

    def fax_document(self, document: str):
        print(f"MutilFunctionPrinter is faxing: {document}")

    def scan_document(self, document: str):
        print(f"MutilFunctionPrinter is scanning: {document}")

class OldFashionedPrinter(Machine):
    def print_document(self, document: str):
        print(f"OldFashionedPrinter is printing: {document}")

    def fax_document(self, document: str):
        raise NotImplementedError("OldFashionedPrinter cannot fax!")

    def scan_document(self, document: str):
        raise NotImplementedError("OldFashionedPrinter cannot scan!")

# The following class follows the interface segregation principle.
class Printer(ABC):
    @abstractmethod
    def print_document(self, document: str):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self, document: str):
        pass

class MyPrinter(Printer):
    def print_document(self, document: str):
        print(f"MyPrinter is printing: {document}")

class MyScanner(Scanner):
    def scan_document(self, document: str):
        print(f"MyScanner is scanning: {document}")

class Photocopier(Printer, Scanner):
    def print_document(self, document: str):
        print(f"Photocopier is printing: {document}")

    def scan_document(self, document: str):
        print(f"Photocopier is scanning: {document}")
    

# Or you can combine the two classes into one interface
class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print_document(self, document: str):
        pass

    @abstractmethod
    def scan_document(self, document: str):
        pass

class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer: Printer, scanner: Scanner):
        self.printer = printer
        self.scanner = scanner

    def print_document(self, document: str):
        self.printer.print_document(document)

    def scan_document(self, document: str):
        self.scanner.scan_document(document)

if __name__ == "__main__":
    old_fashion_printer = OldFashionedPrinter()
    old_fashion_printer.print_document("Hello")
    #old_fashion_printer.fax_document("Hello")
    #old_fashion_printer.scan_document("Hello")

    my_printer = MyPrinter()
    my_scanner = MyScanner()
    multi_function_machine = MultiFunctionMachine(my_printer, my_scanner)
    multi_function_machine.print_document("Hello")
    multi_function_machine.scan_document("Hello")
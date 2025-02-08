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

import typing

def before_using_builder_to_construct_html():
    ## simple scenario
    text = "hello"
    parts = ["<p>", text, "</p>"]
    print("".join(parts))

    ## completicated scenario
    words = ["hello", "world"]
    parts = ["<ul>"]
    for word in words:
        parts.append(f"  <li>{word}</li>")
    parts.append("</ul>")
    print("\n".join(parts))


class HtmlElement:
    indent_size: int = 2

    def __init__(self, name: str="", text: str=""):
        self.name: str = name
        self.text: str = text
        self.elements: typing.List[HtmlElement] = []

    def __str(self, indent: int):
        lines: typing.List[str] = []
        indent_text: str = " " * (indent * self.indent_size)
        lines.append(f"{indent_text}<{self.name}>")

        if self.text:
            indent1_text: str = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{indent1_text}{self.text}")

        for element in self.elements:
            lines.append(element.__str(indent + 1))

        lines.append(f"{indent_text}</{self.name}>")
        return "\n".join(lines)

    def __str__(self) -> str:
        return self.__str(0)

    @staticmethod
    def create():
        return HtmlBuilder("html")

class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root: HtmlElement = HtmlElement(name=root_name)

    ## not fluent
    def add_child(self, child_name: str, child_text: str):
        self.__root.elements.append(
            HtmlElement(child_name, child_text))

    ## fluent
    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text))
        return self

    def clear(self):
        self.__root = HtmlElement(name=self.root_name)

    def __str__(self):
        return str(self.__root)

def using_builder_to_construct_html():
    builder = HtmlBuilder("ul")
    builder.add_child("li", "hello")
    builder.add_child("li", "world")
    print("\nordinary builder:")
    print(builder)

    builder.clear()
    builder.add_child_fluent("li", "hello").add_child_fluent("li", "world")
    print("\nfluent builder:")
    print(builder)


if __name__ == "__main__":
    #before_using_builder_to_construct_html()
    using_builder_to_construct_html()


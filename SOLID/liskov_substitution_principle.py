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

class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: float):
        self._width = value
    
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = value
    
    @property
    def area(self):
        return self._width * self._height

    def __str__(self) -> str:
        return f"Width: {self._width}, Height: {self._height}"

class Square(Rectangle):
    def __init__(self, size: float):
        super().__init__(size, size)
    
    @Rectangle.width.setter
    def width(self, value: float):
        self._width = self._height = value
    
    @Rectangle.height.setter
    def height(self, value: float):
        self._width = self._height = value

def use_it(rectangle: Rectangle):
    width = rectangle.width
    rectangle.height = 10 # This will change the width of the rectangle. It will cause unpleasant side effect
    expected = width * 10
    print(f"Expected an area of {expected}, got {rectangle.area}")


if __name__ == "__main__":
    rectangle = Rectangle(2, 3)
    use_it(rectangle)

    square = Square(5)
    use_it(square)
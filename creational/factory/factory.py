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

from enum import Enum
import math

def without_factory_method():
    class CoordinateSystem(Enum):
        CARTESIAN = 1
        POLAR = 2

    class Point:
        def __init__(
                self, a: float, 
                b: float, 
                system: CoordinateSystem = CoordinateSystem.CARTESIAN):
            if system == CoordinateSystem.CARTESIAN:
                self.x = a
                self.y = b
            elif system == CoordinateSystem.POLAR:
                self.x = a * math.sin(b)
                self.y = a * math.cos(b)
        def __str__(self) -> str:
            return f'x: {self.x}, y: {self.y}'

    point1 = Point(2, 3, CoordinateSystem.CARTESIAN)
    print(point1)
    point2 = Point(2, 3, CoordinateSystem.POLAR)
    print(point2)

def with_factory_method():
    class Point:
        def __init__(self, x: float, y: float):
            self.x = x
            self.y = y

        def __str__(self) -> str:
            return f'x: {self.x}, y: {self.y}'
        
        @staticmethod
        def new_cartesian_point(x: float, y: float) -> 'Point':
            return Point(x, y)

        @staticmethod
        def new_polar_point(rho: float, theta: float) -> 'Point':
            return Point(rho * math.cos(theta), rho * math.sin(theta))

    point1 = Point.new_cartesian_point(2, 3)
    print(point1)
    point2 = Point.new_polar_point(2, 3)
    print(point2)

def with_factory():
    class Point:
        def __init__(self, x: float=0.0, y: float=0.0):
            self.x = x
            self.y = y

        def __str__(self) -> str:
            return f'x: {self.x}, y: {self.y}'
        
    class PointFactory:
        @staticmethod
        def new_cartesian_point(x: float, y: float) -> Point:
            point = Point()
            point.x = x
            point.y = y
            return point

        @staticmethod
        def new_polar_point(rho: float, theta: float) -> Point:
            return Point(rho * math.cos(theta), rho * math.sin(theta))

    point1 = PointFactory.new_cartesian_point(2, 3)
    print(point1)
    point2 = PointFactory.new_polar_point(2, 3)
    print(point2)

def with_factory_as_inner_class():
    class Point:
        def __init__(self, x: float=0.0, y: float=0.0):
            self.x = x
            self.y = y

        def __str__(self) -> str:
            return f'x: {self.x}, y: {self.y}'
        
        class PointFactory:
            def new_cartesian_point(self, x: float, y: float) -> 'Point':
                point = Point()
                point.x = x
                point.y = y
                return point

            def new_polar_point(self, rho: float, theta: float) -> 'Point':
                return Point(rho * math.cos(theta), rho * math.sin(theta))

        factory = PointFactory()

    point1 = Point.factory.new_cartesian_point(2, 3)
    print(point1)
    point2 = Point.factory.new_polar_point(2, 3)
    print(point2)

if __name__ == '__main__':
    with_factory_as_inner_class()

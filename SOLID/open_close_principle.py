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

from enum import Enum
import typing

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name: str, color: Color, size: Size):
        self.name = name
        self.color = color
        self.size = size

# The following class called ProductFilter violates the open-close principle
# This will cause state space explosion
# If we have 3 creteria, color, width and size, we may have the following methods:
# - filter_by_color
# - filter_by_width
# - filter_by_size
# - filter_by_color_and_width
# - filter_by_color_and_size
# - filter_by_width_and_size
# - filter_by_color_and_width_and_size
class ProductFilter:
    def filter_by_color(self, all_products: typing.List[Product], color: Color):
        single_product: Product
        for single_product in all_products:
            if single_product.color == color:
                yield single_product

    def filter_by_size(self, all_products: typing.List[Product], size: Size):
        single_product: Product
        for single_product in all_products:
            if single_product.size == size:
                yield single_product

    def filter_by_size_and_color(self, all_products: typing.List[Product], size: Size, color: Color):
        single_product: Product
        for single_product in all_products:
            if single_product.size == size and single_product.color == color:
                yield single_product

# The following classes are a better way to implement the open-close principle
# Specification is an abstract class that has a method called is_satisfied
class Specification:
    def is_satisfied(self, item: Product) -> bool:
        raise NotImplementedError

# ColorSpecification and SizeSpecification are concrete classes that inherit from Specification
class ColorSpecification(Specification):
    def __init__(self, color: Color):
        self.color = color

    def is_satisfied(self, item: Product) -> bool:
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size: Size):
        self.size = size

    def is_satisfied(self, item: Product) -> bool:
        return item.size == self.size

# AndSpecification is a concrete class that inherits from Specification
class AndSpecification(Specification):
    def __init__(self, *args: Specification):
        self.args = args

    def is_satisfied(self, item: Product) -> bool:
        return all(map(lambda spec: spec.is_satisfied(item), self.args))

# Now we can create a class called Filter that has a abstract method called filter
class Filter:
    def filter(self, items: typing.List[Product], spec: Specification):
        raise NotImplementedError
    
# BetterFilter is a concrete class that inherits from Filter
class BetterFilter(Filter):
    def filter(self, items: typing.List[Product], spec: Specification):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    # Create some products
    product1 = Product("Apple", Color.RED, Size.SMALL)
    product2 = Product("Doraemon doll", Color.BLUE, Size.MEDIUM)
    product3 = Product("Tree", Color.GREEN, Size.LARGE)
    products = [product1, product2, product3]

    print("The following is the old way to filter products that violates the open-close principle")
    product_filter = ProductFilter()
    product: Product
    for product in product_filter.filter_by_color(products, Color.RED):
        print(f"{product.name} is red")

    print("\nThe following is the new way to filter products that follows the open-close principle")
    better_filter = BetterFilter()
    green_specification = ColorSpecification(Color.GREEN)
    for product in better_filter.filter(products, green_specification):
        print(f"{product.name} is green")
    
    large_specification = SizeSpecification(Size.LARGE)
    for product in better_filter.filter(products, large_specification):
        print(f"{product.name} is large")

    large_blue = AndSpecification(large_specification, green_specification)
    for product in better_filter.filter(products, large_blue):
        print(f"{product.name} is large and green")

    
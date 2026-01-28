from abc import ABC
import snoop


class TypeValidation(ABC):
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def set_name(self, attribute_name):
        self.attribute_name = attribute_name
    
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise ValueError(
                f"В атрибут {self.attribute_name} можно сохранять только тип {self.expected_type.__name__}"
            )
        instance.__dict__[self.attribute_name] = value

    def __get__(self, instance):
        if instance is None:
            return self
        return instance.__dict__.get(self.attribute_name, None)

class Person:
    age = TypeValidation(int)
    height = TypeValidation(float)
    name = TypeValidation(str)
    hobbies = TypeValidation(list)

mike = Person()
try:
    mike.name = 100
except ValueError as e:
    print(e)
try:
    mike.height = (1, 2, 3)
except ValueError as e:
    print(e)
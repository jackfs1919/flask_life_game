##%%
class StringValidation:

    def __set_name__(self, owner_class, attribute_name):
        self.attribute_name = attribute_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'В атрибут {self.attribute_name} можно сохранять только строки.')
        instance.__dict__[self.attribute_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.attribute_name, None)
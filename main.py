# В main.py
class Bank:
    def __init__(self, name, age, money, key):
        self._name = name
        self._age = age
        self.__money = money
        self.__key = key

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

class ExtendedBank(Bank):
    def __init__(self, name, age, money, key, additional_property):
        super().__init__(name, age, money, key)
        self._additional_property = additional_property

    def get_additional_property(self):
        return self._additional_property

    def set_additional_property(self, value):
        self._additional_property = value

class CustomExtendedBank(ExtendedBank):
    def __init__(self, name, age, money, key, additional_property, custom_argument1, custom_argument2):
        super().__init__(name, age, money, key, additional_property)
        self._custom_argument1 = custom_argument1
        self._custom_argument2 = custom_argument2

    @property
    def custom_argument1(self):
        return self._custom_argument1

    @custom_argument1.setter
    def custom_argument1(self, value):
        self._custom_argument1 = value

    @property
    def custom_argument2(self):
        return self._custom_argument2

    @custom_argument2.setter
    def custom_argument2(self, value):
        self._custom_argument2 = value

# Если этот файл запускается как основной модуль
if __name__ == "__main__":
    from users import custom_extended_bank_instance

    # Изменяем значения аргументов с использованием property
    custom_extended_bank_instance.custom_argument1 = "new_value1"
    custom_extended_bank_instance.set_name("New Bob")

    # Выводим значения аргументов
    print("Name:", custom_extended_bank_instance.get_name())
    print("Additional Property:", custom_extended_bank_instance.get_additional_property())
    print("Custom Argument 1:", custom_extended_bank_instance.custom_argument1)
    print("Custom Argument 2:", custom_extended_bank_instance.custom_argument2)

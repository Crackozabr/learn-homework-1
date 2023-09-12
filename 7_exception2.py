"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
        if max_discount >= 100:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except (TypeError, ValueError) as err:
        return f'Ошибка ввода: {err}.'


if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))

    # Следующий пример был добавлен, чтобы проверить что исключение TypeError будет вызываться.
    # Так как в предыдущих шести примерах ошибка преобразования строки во float или int могло вызвать только ValueError.
    print(discounted([100.0], 5, "10"))
    # Пример ниже, вызывает исключение с пользовательским текстом, так как скидка выше 100%.
    # Нужен для проверки того, что пользовательский текст из функции так же выводится верно.
    print(discounted(100.0, 5, "300"))

    """
    Если передавать в функцию больше аргументов, чем в ней есть, например
        print(discounted(100.0, 5, "10", 12))
    будет вызвана ошибка
    TypeError: discounted() takes from 2 to 3 positional arguments but 4 were given
    При последовательном запуске print() с вызовом функций (как в коде выше), такая строка остановит программу.
    
    Если обернуть строки с print() в try except, то это так же не спасет от прекращения выполнения кода,
    потому что из except обратно в try уже не вернуться.

    Как вариант: запихнуть значения аргументов из последовательных print() в список кортежей, после чего 
    в цикле передавать очередной кортеж, и при вызове отлавливать ошибки.

    префикс * используется для распаковки кортежа в аргументы, подробнее по ссылке
    https://tproger.ru/translations/asterisks-in-python-what-they-are-and-how-to-use-them/
    
    Собственно код:

    examples = [(100, 2), (100, "3"), ("100", "4.5"), ("five", 5), (100.0, 5, "300"), (100.0, 5, "10", 12), ("сто", "десять"), (100.0, 5, "10")]

    for example in range(0,len(examples)):
        try:
            print(discounted(*examples[example]))
        except TypeError as error:
            print(f"Слишком много аргументов в примере {examples[example]}. Описание ошибкиЖ {error})
   
    """

"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(one, two):
    if isinstance(one, str) and isinstance(two, str):
      if one == two:
         return 1
      elif len(one) > len(two) and two == 'learn': # По условию 2 решения для такого варианта
         pass
      elif len(one) > len(two):
         return 2
      elif two == 'learn':
         return 3
      else: pass
    else: return 0
    
if __name__ == "__main__":
    print(main('one', 'two')) # None
    print(main('one', 'one')) # 1
    print(main('one', 'five')) # None
    print(main('five', 'one')) # 2
    print(main('one', 'learn')) # 3
    print(main('nineteen', 'learn')) # None
    print(main(12, 'two')) # 0
    print(main('one', 12.5)) # 0
    print(main('one', ['two'])) # 0

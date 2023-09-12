"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main(phones_sales):
    message = ''
    all_summ = 0
    all_len = 0
    for phone in phones_sales:
        summ = 0
        for item in phone['items_sold']:
            summ += item
        summ_avg = round(summ/len(phone["items_sold"]), 2)
        message += f'Суммарные продажи телефона {phone["product"]} составляют {summ}. Средние продажи {summ_avg}\n'
        all_summ += summ
        all_len += len(phone["items_sold"])
    message += f'Суммарные продажи всех телефонов {all_summ}. Средние продажи {all_summ/all_len}'
    return message
    
    
if __name__ == "__main__":
    phones_sales = [{'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
                        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
                        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]}
                        ]
    
    print(main(phones_sales))

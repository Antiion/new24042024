goods = {'Лампа': '12345', #коды товаров
         'Стол': '23456',
         'Диван': '34567',
         'Стул': '45678'
         }
store = {                                   #Количество и цена
    '12345': [{'quantity': 27, 'price': 42},
              ],
    '23456': [{'quantity': 22, 'price': 510},
              {'quantity': 32, 'price': 520},
              ],
    '34567': [{'quantity': 2, 'price': 1200},
              {'quantity': 1, 'price': 1150},
              ],
    '45678': [{'quantity': 50, 'price': 100},
              {'quantity': 12, 'price': 95},
              {'quantity': 43, 'price': 97}
              ]
}

for g_key in goods:
    amount, total_price = 0, 0
    for i_store in store[goods[g_key]]:
        amount += i_store['quantity']
        total_price += amount * i_store['price']
    print(f'{g_key} - {amount} шт, стоимость {total_price} руб.')
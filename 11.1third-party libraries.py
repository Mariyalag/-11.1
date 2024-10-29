import pandas as pd

data = {'Продукт': ['Соль', 'Сахар', 'Мука'], # данные
    'Количество': [15, 23, 12],
    'Цена': [79.99, 65.99, 89.99]}

df = pd.DataFrame(data) # таблица

df.to_csv('sales_data.csv', index=False) # сохраняю
print('Файл sales_data.csv успешно создан.')

data = pd.read_csv('sales_data.csv') # данные из CSV-файла

print("Товар:") # вывожу
print(data.head())

data['Total'] = data['Количество'] * data['Цена'] # рассчитываю
total_revenue = data['Total'].sum()
print(f'Общая сумма: {total_revenue}')


import matplotlib.pyplot as plt

products = data['Продукт'] # данные для графика
quantities = data['Количество']

plt.figure(figsize=(10, 6)) # график
plt.bar(products, quantities, color='blue')
plt.title('Количество проданных товаров')
plt.xlabel('Товары')
plt.ylabel('Количество')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()


import numpy as np

prices = data['Цена'].to_numpy()
rounded_prices = np.round(prices, 2)

average_price = np.mean(rounded_prices)
print(f'Средняя цена товара: {average_price:.2f}')



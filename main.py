import pandas as pd

df = pd.read_csv('Cleaned_Dataset.csv')
print("Первое задание\n")
print("Пять первых строк таблицы")
print(df.head())
print("Информация о таблице")
print(df.info())
print("Общая статистика")
print(df.describe())
print("\n")

df = pd.read_csv('dz.csv')
print("Второе задание\n")
print(df)
group = df.groupby('City')['Salary'].mean()
print(f"\nСредняя зарплата в {group}")

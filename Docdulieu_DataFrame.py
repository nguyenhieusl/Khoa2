import pandas as pd
df = pd.read_csv(filepath_or_buffer='Data\FoodPrice_in_Turkey.csv',sep=',')
print(df.head())
# Doc file CSV bằng ghi tường minh tham số

df = pd.read_csv('Data\FoodPrice_in_Turkey.csv')
df.head
# Doc file SCV bằng cách không tường minh tham số

df = pd.read_excel('Data\house_price_dống-da.xlsx')
print(df.head(2))
# Doc file Excel bằng cách không tường minh tham số

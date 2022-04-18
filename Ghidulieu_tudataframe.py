import pandas as pd
df = pd.read_csv('Data\FoodPrice_in_Turkey.csv')
print(df.head())
# Doc file CSV bằng ghi tường minh tham số

df.to_csv('Data\FoodPrice_in_Turkey_to_new_file.csv')
df.to_excel('Data\FoodPrice_in_Turkey_to_new_file.xlsx')
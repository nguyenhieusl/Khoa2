import pandas as dp
db = dp.read_csv('Data\GDPlist.csv',encoding='ISO-8859-1')
print(db.head())
# Import data và show 5 dòng dầu tiên

db.info()
# Show thông tin của dữ liệu (data bao gồm 125 dòng và 3 cột)
# Thang đo dữ liệu country, continent là nominal, GDP là ratio

print("số lượng quốc gia mỗi châu lục là")
print(db.groupby('Continent')['Country'].size().head())

print("GDP của châu lục là: ")
print(db.groupby('Continent')['GDP (millions of US$)'].sum().head())
# GDP của từng châu lục

print(db.sort_values('GDP (millions of US$)',ascending = False).head(10))
# Top 10 quốc gia có GDP cao nhất

import matplotlib.pyplot as plt
data_clean = db['GDP (millions of US$)']
plt.hist(data_clean, bins = 100)
plt.title("Báo cáo GDP")
plt.xlabel("sô lượng quốc gia")
plt.ylabel("GDP")
plt.show()
# Vẽ biểu đồ histagram
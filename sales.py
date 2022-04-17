import pandas as pd
# Import thư viện
data = pd.read_csv('Data\OnlineRetail.csv',encoding="ISO-8859-1")
# Mở file csv theo chuẩn ISO-8859-1
data.head()
# Đọc 5 dòng đầu tiên của dữ liệu

country = data.Country.unique()
print(country)
# In không trùng lặp tên các quốc gia

print("So luong cac quoc gia la: " + str(country.size))
# In ra số lượng các quốc gia

data['total'] = data['Quantity'] * data['UnitPrice']
# Thêm cột total và tính giá trị = số lượng * đơn giá

print(data.head())
# In 5 dòng đầu tiên của total

total_invoices = data['total'].sum()
print("Số lượng hóa đơn bán ra là: " + str(total_invoices.size))
print("Tổng doanh thu là: " + str(total_invoices.sum()))
# Tỉnh tổng số lượng hóa đơn và doanh thu

quantity_product = data.groupby(['StockCode', 'Description'])['Quantity'].sum().sort_values(ascending= False)
quantity_product.head(7)
print(quantity_product)
# Gom nhóm và in ra dữ liệu sau khi gom

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

data = pd.read_csv("C:\\Users\\Center\\Downloads\\1632300362534233.csv")

data['Area'] = pd.to_numeric(data['Area'], errors='coerce')
data = data[data['Area'] <= 100]

data['Room'] = data['Room'].astype(int)
data['Parking'] = data['Parking'].astype(int)
data['Warehouse'] = data['Warehouse'].astype(int)
data['Elevator'] = data['Elevator'].astype(int)

top = data['Address'].value_counts().nlargest(20).index

data['Address'] = data['Address'].where(data['Address'].isin(top), 'other')

data = pd.get_dummies(data, columns=['Address'], drop_first=True)

data = data.dropna()

address_cols = [col for col in data.columns if col.startswith('Address_')]

cols_x = ['Area', 'Room', 'Parking', 'Warehouse', 'Elevator'] + address_cols

reg = linear_model.LinearRegression()

X = data[cols_x]
y = data[['Price(USD)']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
print('R2 Score:', r2_score(y_test, y_pred))

plt.scatter(y_test,y_pred)
plt.xlabel("Actual Price (USD)")
plt.ylabel("Predicted Price (USD)")
plt.show()

top_list = list(top)

def predict(area, room, parking, warehouse, elevator, address):
    row = pd.DataFrame({
        'Area': [area],
        'Room': [room],
        'Parking': [parking],
        'Warehouse': [warehouse],
        'Elevator': [elevator],
        'Address': [address]
    })
    
    row['Address'] = row['Address'].where(row['Address'].isin(top_list), 'other')
    
    row = pd.get_dummies(row, columns=['Address'], drop_first=True)
    
    row = row.reindex(columns=cols_x, fill_value=0)
    
    pred = reg.predict(row)
    return pred[0][0]


while True:
    entry = input("house's information:\nArea Room Parking Warehouse Elevator Address\n").split()
    area = float(entry[0])
    room = int(entry[1])
    parking = int(entry[2])
    warehouse = int(entry[3])
    elevator = int(entry[4])
    address = entry[5]
    
    price = predict(area, room, parking, warehouse, elevator, address)
    print("Predicted Price:", price)
    break
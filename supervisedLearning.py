import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

np.random.seed(42)
sizes = np.random.randint(1000, 3000, size =50)
bedrooms = np.random.randint(2, 6, size =50)
ages = np.random.randint(0 , 40, size =50)

prices =0.3*sizes +10*bedrooms -2*ages +np.random.randint(0,10,size =50)
prices = np.round(prices).astype(int)

df= pd.DataFrame({
    'Size' :sizes,
    'Bedroom' : bedrooms,
    'Age' : ages,
    'Price' :prices
})

X =df[['Size','Bedroom','Age']]
Y =df['Price']
X_train, X_test, Y_train, Y_test =train_test_split(X,Y, test_size=0.3 ,random_state=42)

model =LinearRegression()
model.fit(X_train,Y_train)
Y_predict =model.predict(X_test)
mean_squared_error = mean_squared_error(Y_test,Y_predict)
r2_score = r2_score(Y_test,Y_predict)
# print(model.coef_)
# print(mean_squared_error)
# print(r2_score)


size = int(input ("Enter the size of the room"))
bedroom = int(input ("Enter the number of bedroom"))
age = int(input ("enter how old is the house"))

input_data =[[size, bedroom, age]]
price =model.predict(input_data)[0]
print(price)
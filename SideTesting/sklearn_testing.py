import numpy as np
# import sklearn
from sklearn.model_selection import train_test_split

X, y = np.arange(10).reshape((5, 2)), range(5)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
print(X_train)
print(y_train)

X1 = ['i', 'ii', 'iii', 'iv', 'v']
x_train, x_test = train_test_split(X1, test_size=0.33, random_state=42)
print(x_train)
print(x_test)

print("end!!")
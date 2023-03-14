import numpy as np
from sklearn.model_selection import KFold
# X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
X = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii']
y = np.array([1, 2, 3, 4, 5, 6, 7])

kf = KFold(n_splits=3)
kf.get_n_splits(X)

print('*')
print(kf)
print('**')
KFold(n_splits=2, random_state=None, shuffle=False)
for i, (train_index, test_index) in enumerate(kf.split(X)):
    print(f"Fold {i}:")
    print(f"  Train: index={train_index}")
    print(f"  Test:  index={test_index}")

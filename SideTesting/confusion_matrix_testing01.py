import os
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

y_true = ["cat", "ant", "cat", "cat", "ant", "bird"]
y_pred = ["ant", "ant", "cat", "cat", "ant", "cat"]
cm = confusion_matrix(y_true, y_pred, labels=["ant", "bird", "cat"])
print(cm)
disp = ConfusionMatrixDisplay(cm, display_labels=["ant", "bird", "cat"])
disp.plot()
plt.savefig(os.path.join('..', 'Products', 'Figures', 'test_confusion_matrix.png'))
plt.show()
# plt.savefig('test_confusion_matrix')
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split 
import matplotlib.pyplot as plt 
import pandas as pd
import mglearn
from sklearn.datasets.samples_generator import make_blobs

cancer = load_breast_cancer()
#print(cancer.DESCR)
print(cancer.feature_names)
print(cancer.target_names) 
print(type(cancer.data))
print(cancer.data)
print(cancer.data.shape)
print("\n================================")

raw_data = pd.read_csv('C:/Users/N0009/Downloads/breast-cancer-wisconsin-data.csv')
print(raw_data.tail)
#mglearn.plots.plot_knn_classification(n_neighbors=7)
#plt.show()

X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42)
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
print('Accuracy of KNN n-5, on the training set: {:.2f}'.format(knn.score(X_train, y_train)))
print('Accuracy of KNN n-5, on the training set: {:.2f}'.format(knn.score(X_test, y_test)))
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=65)

training_accuracy = []
test_accuracy = []

neighbors_setting = range(1,51)
for n_neighbors in neighbors_setting:
    clf = KNeighborsClassifier(n_neighbors = n_neighbors)
    clf.fit(X_train, y_train)
    training_accuracy.append(clf.score(X_train, y_train))
    test_accuracy.append(clf.score(X_test, y_test))

plt.plot(neighbors_setting, training_accuracy, label="Train accuracy")
plt.plot(neighbors_setting, test_accuracy, label="Test accuracy")
plt.ylabel('Accuracy')
plt.xlabel('Number of Neighbors')
plt.legend()
plt.show()
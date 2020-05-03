# %matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

wine_data = pd.read_csv('./wine.csv', delimiter=',', dtype=float, header=None)
wine_data.columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residualsugar', 'chlorides', 'free sulfur dioxide','total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality', 'class']
print(wine_data.head(10))

print(wine_data.iloc[:,-3])

print(wine_data.iloc[0, :])

print(wine_data.iloc[1:3, 1:5])

x_data = wine_data.iloc[:, 0:-1]
y_data = wine_data.iloc[:, -1]

print(x_data.head(1))
print(y_data.head(1))


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

train_x, test_x, train_y, test_y = train_test_split(x_data, y_data, test_size = 0.3, random_state = 42)
print(train_x.shape)
print(test_x.shape)

wine_tree = DecisionTreeClassifier(criterion='gini', max_depth=5, splitter='random')
wine_tree.fit(train_x, train_y)
print(wine_tree)


y_pred_train = wine_tree.predict(train_x)
y_pred_test = wine_tree.predict(test_x)
print("Train Data:", accuracy_score(train_y, y_pred_train))
print("Test Data", accuracy_score(test_y, y_pred_test))


from sklearn.metrics import classification_report
y_true, y_pred = test_y, wine_tree.predict(test_x)
print(classification_report(y_true, y_pred))



import os
import pydotplus
from sklearn.tree import export_graphviz
from IPython.display import Image
# path 설정 - 자신의 설치한 경로.
os.environ["PATH"] += os.pathsep + r'E:\util\gra\bin'
# os_path = r'E:\util\gra'
# print(os.pathsep)
# print(os_path)
dot_data = export_graphviz(wine_tree, out_file=None,feature_names=x_data.columns, class_names=['White', 'Red'], filled=True, rounded=True, special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
# 이미지의 depth 는 모델 학습의 depth의 영향을 받음.
print(graph)
# 현재 이미지는 depth = 5
print(Image(graph.create_png()))
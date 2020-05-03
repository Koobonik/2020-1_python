import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")
df_train = pd.read_csv("./titanic_train.csv")
df_test = pd.read_csv("./titanic_test.csv")
print(df_train.info())  # 데이터 프레임의 정보를 읽어옴

df_train = df_train.drop(['name', 'ticket', 'body', 'cabin', 'home.dest'], axis=1)
df_test = df_test.drop(['name', 'ticket', 'body', 'cabin', 'home.dest'], axis=1)


print(df_train.info())

print(df_train['survived'].value_counts())
df_train['survived'].value_counts().plot.bar()

import seaborn as sns
ax = sns.countplot(x = 'pclass', hue = 'survived', data=df_train)
print(ax)
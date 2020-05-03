import pandas as pd

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]
custom = [1,5,25,13,23232]

BabyDataSet = list(zip(names, births))
df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
df.head()


print(df)
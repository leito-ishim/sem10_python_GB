import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# pd.get_dummies(data['whoAmI'])

print(pd.get_dummies(data['whoAmI']))

# Попробовал сделать без get_dummies, если я правильно понял что требовалось сделать
data.loc[data['whoAmI'] == 'robot', 'robot'] = True
data.loc[data['whoAmI'] == 'human', 'human'] = True
data.loc[data['whoAmI'] != 'robot', 'robot'] = False
data.loc[data['whoAmI'] != 'human', 'human'] = False

print(data[['robot', 'human']])

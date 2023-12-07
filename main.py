import pandas as pd

data=pd.read_csv('movies.csv')

budget = data['budget']
revenue = data['revenue']

print(data)
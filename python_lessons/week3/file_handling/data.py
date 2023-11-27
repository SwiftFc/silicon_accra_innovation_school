#loading data files with pandas
import pandas as pd

file_path = './resources/movies.csv'
#read csv
df = pd.read_csv(file_path)
#print 1-5 rows of data
print(df.head())
#print(df.tail())
print(df.describe())

import pandas as pd

i = pd.read_excel('data.xlsx', 'Sheet1', 0).to_sql()


print(i)

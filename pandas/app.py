import pandas as pd

csv_df = pd.read_csv('pandas/data.csv')

print(csv_df)
print('size',pd.options.display.max_rows) 

json_df = pd.read_json('pandas/data.json')
print(pd.options.display.max_rows) 
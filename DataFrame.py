import pandas as pd
import numpy as np

values = [['A', 1, 100], ['A', 3, 150], ['A', 2, 120]]
df = pd.DataFrame(columns=['Test', 'Value'])

# for line in values:
data = [1,2,3,4,7]

for inp in data:
    df.loc[inp, 'Test'] = inp
# df = pd.DataFrame(values, columns=['Session', 'Step', 'Time'])

# df['test'] = df['Session']+df['Step']

print(df)
df.reindex(list(range(df.index.min(),df.index.max()+1)),fill_value=0)
print(df)
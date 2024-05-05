import seaborn as sns
import pandas as pd

flights = sns.load_dataset("flights")

print(flights.loc[flights['passengers'].idxmax(), ['month'] ])


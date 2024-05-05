import seaborn as sns
import pandas as pd

flights = sns.load_dataset("flights")

print('with the most amount of passengers: ' + flights.loc[flights['passengers'].idxmax(), ['month'] ])


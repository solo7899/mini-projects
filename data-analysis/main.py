import requests
import pandas as pd
from matplotlib import pyplot as plt

params = {}
response = requests.get(
    "https://hub.dummyapis.com/employee?noofRecords=10&idStarts=1001", params=params
)
df = pd.read_json(response.text)  # this is gonna be deprecated
# print(df.info()) # shows attributes
x = df["salary"].mean()
df["salary"].fillna(x, inplace=True)

plt.bar(df["firstName"], df["salary"])
plt.xticks(rotation=45)
plt.show()
print("done.")

import pandas as pd
import numpy as np

s = pd.Series([1,2,3,np.nan,1,2])
#print(s)

dates = pd.date_range("20130101",periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list("ABCD"))

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)),dtype="float32"),
        "D": np.array([3]*4, dtype="int32"),
        "E": pd.Categorical(["test","train","test","train"]),
        "F": "foo",
    }
)

#df and dfs are Class instances

# <Class instance>.sort_index(axis= 1 OR 0, ascending= True OR False) to sort an array by axis
## E.g print(df2.sort_index(axis=0, ascending=False))


print(df.sort_values(by="B"))

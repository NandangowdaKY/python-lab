import pandas as pd

data = {
    "Name": ["Nandan Gowda", "Charit"],
    "Age": [20, 22]
}

temp = pd.DataFrame(data)

print(temp)
temp.to_csv("Stud.csv", index=False)

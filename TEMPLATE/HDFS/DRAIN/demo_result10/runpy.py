import pandas as pd

def to_int(s):
    try:
        return int(s)
    except ValueError:
        return 0

# Tạo đường dẫn đến file Excel
file_path = "A.xlsx"

df = pd.read_excel(file_path)

# In dữ liệu
print(df)

set_template = set(df["EventTemplate"])
result = []
for i in set_template:
    summ = 0
    hash1 = ""
    for j in range(len(df)):
        if df["EventTemplate"][j] == i:
            summ = summ + to_int(df["Occurrences"][j])
            hash1 = df["EventId"][j]
    result.append([hash1, i, summ])
print("Success!" + str(len(set_template)))
columns = ["EventId","Template", "Occurrences"]

# Tạo dataframe
df_res = pd.DataFrame(result, columns=columns)
df_res.to_csv("Aoutput.csv", index=True)
print(df_res)

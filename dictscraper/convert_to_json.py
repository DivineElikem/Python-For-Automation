import pandas as pd

file_path = 'IT_Dictionary.xlsx'
df = pd.read_excel(file_path)

df.columns = df.columns.str.strip()

json_data = df.to_json(orient='records', indent=4)

json_file_path = 'IT_Dictionary.json'

with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)

print(f"Conversion complete. Data saved to {json_file_path}")

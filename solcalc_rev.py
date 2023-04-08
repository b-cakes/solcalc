import pandas as pd

mfg = 'REC'
print(mfg)

models = ['TP4', 'NP3', 'AA-PURE-R']
models_series = pd.Series(models)
print(models_series)

watt_class = [365, 400, 420]
watt_class_series = pd.Series(watt_class)
print(watt_class_series)

cost_watt = [0.68, 0.71, 0.88]
cost_watt_series = pd.Series(cost_watt)
print(cost_watt_series)

cost_unit = watt_class_series * cost_watt_series
cost_unit_series = pd.Series(cost_unit)
print(cost_unit_series)

df_data = {
    'Model': models_series, 'Rating': watt_class_series,
    'Cost/W': cost_watt_series, 'Cost/ea': cost_unit_series
    }

print(df_data)
df_table = pd.DataFrame(df_data)
print(df_table)

df_table_2 = df_table.rename(index=lambda x: mfg)
print(df_table_2)

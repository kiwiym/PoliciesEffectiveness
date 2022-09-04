import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

from load_data import *

print("-"*5 + "13th Five-Year Plan" + "-"*5)

# Policy Value
v_16 = {}
for i, prov in enumerate(provs):
    s = [[], [], [intensity_16[i]]]
    for p, m in zip(p_prov_16[i], m_prov_16[i]):
        if m > 2:
            continue
        s[m-1].append(alphas_16[p-1])
    s = np.array([np.mean(t) if len(t) > 0 else 0.0 for _, t in enumerate(s)])
    v_16[prov] = s

# Prepare x for Linear Regression
x = np.array([v_16[p] for p in prov_19])
y = np.array(int_dec_rate)
x = np.concatenate([x[:, 0], 
                    x[:, 1],
                    x[:, 0] * x[:, 2], 
                    x[:, 1] * x[:, 2]]).reshape(4, 19).T

# Fit Model
model = LinearRegression(fit_intercept=True) # With Constant
model.fit(x, y)
print("Model:")
print(model.coef_, model.intercept_)
result_135 = model.predict(x)

print("Result:")
print(result_135)

# Use Model to Predict for 14^th Five Year Plan

print("-"*5 + "14th Five-Year Plan" + "-"*5)

# Policy Value
v_21 = {}
for i, prov in enumerate(provs):
    s = [[], [], [intensity_19[i]]]
    for p, m in zip(p_prov_21[i], m_prov_21[i]):
        if m > 2:
            continue
        s[m-1].append(alphas_21[p-1])
    s = np.array([np.mean(t) if len(t) > 0 else 0.0 for _, t in enumerate(s)])
    v_21[prov] = s

# Prepare x for test
x_21 = np.array([v_21[p] for p in prov_19])
x_21 = np.concatenate([x_21[:, 0], 
                        x_21[:, 1],
                        x_21[:, 0] * x_21[:, 2], 
                        x_21[:, 1] * x_21[:, 2]]).reshape(4, 19).T

result_145 = model.predict(x_21)

print("Result:")
print(result_145)

# Output Result into File
df = pd.DataFrame(data={
    "Province": prov_19_eng,
    "13th": result_135,
    "14th": result_145
}).set_index("Province")
df.to_csv("result_model_1.csv")
print("\nResult dumped into file `result_model_1.csv`")
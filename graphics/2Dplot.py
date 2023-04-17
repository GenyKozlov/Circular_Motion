import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

plt.rcParams["figure.autolayout"] = True

df = pd.read_csv(r'CircularMotion-main/data/most valuable/3 copters with a constant center/20221217-111008_setpos.csv', header=0, delimiter=';')

cols = df.columns
for col in cols:
    df[col] = df[col].astype(float)

print(df.columns)


# ax = df.plot(x='i', y=['p_12', 'p_23'])
# ax.set(xlabel='Time, [ds]', ylabel='Phase shifts, [rad]')

# ax = df.plot(x='i', y=['d_1','d_2', 'd_3'])
# ax.set(xlabel='Time, [ds]', ylabel='Distances to the center, [m]')


# fig, axes = plt.subplots(nrows=3, ncols=1)
# ax=df.plot(x='px_1', y=['py_1'], ax=axes[0])
# ax.set(xlabel='px_1, [m]', ylabel='py_1, [m]')

# ax=df.plot(x='px_2', y=['py_2'], ax=axes[1])
# ax.set(xlabel='px_2, [m]', ylabel='py_2, [m]')

# ax=df.plot(x='px_3', y=['py_3'], ax=axes[2])
# ax.set(xlabel='px_3, [m]', ylabel='py_3, [m]')


ax = df.plot(x='px_1', y=['py_1'])
ax.set(xlabel='Time, [ds]', ylabel='Phase shifts, [rad]')

ax=df.plot(x='i', y=['pz_2'])
ax.set(xlabel='px_1, [m]', ylabel='py_1, [m]')

ax=df.plot(x='i', y=['pz_3'])
ax.set(xlabel='px_2, [m]', ylabel='py_2, [m]')

# df.plot(x='i', y=['setPx1','setPx2'])
# df.plot(x='i', y=['setPy1','setPy2'])

# ax = df.plot(x='i', y=['d_1','d_2'])
# ax.set(xlabel='Time, [ds]', ylabel='Distances to the center, [m]')

plt.show()

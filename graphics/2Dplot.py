import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

plt.rcParams["figure.autolayout"] = True

df = pd.read_csv(r'data/Sim_cf/sim3_20230610-230139_.csv', header=0, delimiter=';')

cols = df.columns
for col in cols:
    df[col] = df[col].astype(float)

print(df.columns)


ax=df.plot(x='i', y=['pz_1'])
ax.set(xlabel='Steps', ylabel='z coordinate 1-d copter, [m]')

ax=df.plot(x='i', y=['pz_2'])
ax.set(xlabel='Steps', ylabel='z coordinate 2-d copter, [m]')

ax=df.plot(x='i', y=['pz_3'])
ax.set(xlabel='Steps', ylabel='z coordinate 3-d copter, [m]')

ax = df.plot(x='px_1', y=['py_1'])
ax.set(xlabel='x coordinate 1-d copter, [m]', ylabel='y coordinate 1-d copter, [m]')

ax = df.plot(x='px_2', y=['py_2'])
ax.set(xlabel='x coordinate 2-d copter, [m]', ylabel='y coordinate 2-d copter, [m]')

ax = df.plot(x='px_3', y=['py_3'])
ax.set(xlabel='x coordinate 3-d copter, [m]', ylabel='y coordinate 3-d copter, [m]')

ax = df.plot(x='i', y=['p_12','p_23'])
ax.set(xlabel='Steps', ylabel='Phase shifts, [rad]')

ax = df.plot(x='i', y=['d_1','d_2', 'd_3'])
ax.set(xlabel='Steps', ylabel='Distances to the center, [m]')

# ax = df.plot(x='i', y=['distance_12'])
# ax.set(xlabel='Steps', ylabel='Distance between UAVs, [m]')

# ax = df.plot(x='setPx1', y=['setPy1'], x='px_1', y=['py_1'])
# ax.set(xlabel='x coordinate 1-d copter, [m]', ylabel='y coordinate 1-d copter, [m]')

# ax = df.plot(x='setPx2', y=['setPy2'])
# ax.set(xlabel='x coordinate 2-d copter, [m]', ylabel='y coordinate 2-d copter, [m]')

# ax = df.plot(x='setPx3', y=['setPy3'])
# ax.set(xlabel='x coordinate 3-d copter, [m]', ylabel='y coordinate 3-d copter, [m]')

# fig, axes = plt.subplots(nrows=3, ncols=1)
# ax=df.plot(x='px_1', y=['py_1'], ax=axes[0])
# ax.set(xlabel='px_1, [m]', ylabel='py_1, [m]')

# ax=df.plot(x='px_2', y=['py_2'], ax=axes[1])
# ax.set(xlabel='px_2, [m]', ylabel='py_2, [m]')

# ax=df.plot(x='px_3', y=['py_3'], ax=axes[2])
# ax.set(xlabel='px_3, [m]', ylabel='py_3, [m]')

plt.show()

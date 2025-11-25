import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Q8_logs = pd.read_csv("Q8 logs.csv")
Q8_pos_and_encoders = Q8_logs.iloc[:,2:5].to_numpy()
Q8_pos_and_encoders[:,0] = Q8_pos_and_encoders[:,0] / 2.0
print("Q8 file", Q8_logs)
print("Q8 pos and encoder values", Q8_pos_and_encoders)

sample_rate = 14 # Hz
pos = []
counts_per_second = []
counts = []
RPM = []

for i in range(len(Q8_pos_and_encoders)-1):
    pos.append(Q8_pos_and_encoders[i+1,0] - Q8_pos_and_encoders[i,0])
    counts_per_second.append(pos[i] * sample_rate) # to get counts / second
    counts.append(i+1)
    RPM.append(counts_per_second[i] * 60 / 5281) # to get RPM

fig, ax = plt.subplots(nrows=3, ncols=1)

ax[0].plot(counts, pos)
ax[0].set_xlabel('Sample Count')
ax[0].set_ylabel('change in pos variable (counts)')

ax[1].plot(counts, counts_per_second)
ax[1].set_xlabel('Sample Count')
ax[1].set_ylabel('encoder shaft angular speed (counts/second)')

ax[2].plot(counts, RPM)
ax[2].set_xlabel('Sample Count')
ax[2].set_ylabel('output shaft angular speed (RPM)')


plt.show()
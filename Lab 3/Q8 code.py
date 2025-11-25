## Display your graphs, functions and calculations here
## Use print() to display your final answer

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
EncoderA = []
EncoderB = []
counts = []
rot_speed = [] # in units of output shaft degrees / second

for i in range(len(Q8_pos_and_encoders)-1):
    pos.append(Q8_pos_and_encoders[i+1,0] - Q8_pos_and_encoders[i,0])
    rot_speed.append(pos[i] * sample_rate * 360 / 5281) # to get output shaft degrees/second
    EncoderA.append(Q8_pos_and_encoders[i,1])
    EncoderB.append(Q8_pos_and_encoders[i,2])
    counts.append(i+1)

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(12,8))
ax[0].plot(counts[:100], EncoderA[:100])
ax[0].plot(counts[:100], EncoderB[:100])
ax[0].set_xlabel('Sample Count')
ax[1].plot(counts, rot_speed)
ax[1].set_xlabel('Sample Count')
ax[1].set_ylabel('output shaft angular speed (degrees/second)')

plt.show()
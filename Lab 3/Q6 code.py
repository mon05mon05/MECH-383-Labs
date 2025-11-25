## Display your graphs, functions and calculations here
## Use print() to display your final answer

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

slowCW_logs = pd.read_csv("log_slowSpeedCW.csv")
slowCCW_logs = pd.read_csv("log_slowSpeedCCW.csv")
medCW_logs = pd.read_csv("log_medSpeedCW.csv")
medCCW_logs = pd.read_csv("log_medSpeedCCW.csv")
fastCW_logs = pd.read_csv("log_highSpeedCW.csv")
fastCCW_logs = pd.read_csv("log_highSpeedCCW.csv")

slow_CW_pos_and_encoders = slowCW_logs.iloc[:,2:5].to_numpy()
slow_CW_pos_and_encoders[:,0] = slow_CW_pos_and_encoders[:,0] / 2.0
slow_CCW_pos_and_encoders = slowCCW_logs.iloc[:,2:5].to_numpy()
slow_CCW_pos_and_encoders[:,0] = slow_CCW_pos_and_encoders[:,0] / 2.0
med_CW_pos_and_encoders = medCW_logs.iloc[:,2:5].to_numpy()
med_CW_pos_and_encoders[:,0] = med_CW_pos_and_encoders[:,0] / 2.0
med_CCW_pos_and_encoders = medCCW_logs.iloc[:,2:5].to_numpy()
med_CCW_pos_and_encoders[:,0] = med_CCW_pos_and_encoders[:,0] / 2.0
fast_CW_pos_and_encoders = fastCW_logs.iloc[:,2:5].to_numpy()
fast_CW_pos_and_encoders[:,0] = fast_CW_pos_and_encoders[:,0] / 2.0
fast_CCW_pos_and_encoders = fastCCW_logs.iloc[:,2:5].to_numpy()
fast_CCW_pos_and_encoders[:,0] = fast_CCW_pos_and_encoders[:,0] / 2.0

sample_rate = 14 # Hz
pos = {'slowCW': [], 'slowCCW': [], 'medCW': [], 'medCCW': [], 'fastCW': [], 'fastCCW': []}
EncoderA = {'slowCW': [], 'slowCCW': [], 'medCW': [], 'medCCW': [], 'fastCW': [], 'fastCCW': []}
EncoderB = {'slowCW': [], 'slowCCW': [], 'medCW': [], 'medCCW': [], 'fastCW': [], 'fastCCW': []}
counts = {'slowCW': [], 'slowCCW': [], 'medCW': [], 'medCCW': [], 'fastCW': [], 'fastCCW': []}

# in units of output shaft degrees / second
rot_speed = {'slowCW': [], 'slowCCW': [], 'medCW': [], 'medCCW': [], 'fastCW': [], 'fastCCW': []}

log_list = [slow_CW_pos_and_encoders, slow_CCW_pos_and_encoders, med_CW_pos_and_encoders,
            med_CCW_pos_and_encoders, fast_CW_pos_and_encoders, fast_CCW_pos_and_encoders]

for k in range(6):
    x = list(pos.keys())[k]
    for i in range(len(log_list[k])-5):
        pos[x].append(log_list[k][i+1,0] - log_list[k][i,0])
        rot_speed[x].append(pos[x][i] * sample_rate * 360 / 5281) # to get output shaft degrees/second
        EncoderA[x].append(log_list[k][i,1])
        EncoderB[x].append(log_list[k][i,2])
        counts[x].append(i+1)

slow_fig, slow_ax = plt.subplots(nrows=4, ncols=1, figsize=(11,11), layout='constrained')
slow_ax[0].set_title('CW Slow Speed Encoder Values')
slow_ax[0].plot(counts['slowCW'][:100], EncoderA['slowCW'][:100])
slow_ax[0].plot(counts['slowCW'][:100], EncoderB['slowCW'][:100])
slow_ax[0].set_xlabel('Sample Count')
slow_ax[0].set_ylabel('Encoder Values')
slow_ax[2].set_title('CCW Slow Speed Encoder Values')
slow_ax[2].plot(counts['slowCCW'][:100], EncoderA['slowCCW'][:100])
slow_ax[2].plot(counts['slowCCW'][:100], EncoderB['slowCCW'][:100])
slow_ax[2].set_xlabel('Sample Count')
slow_ax[2].set_ylabel('Encoder Values')
slow_ax[1].set_title('CW Slow Speed Output Shaft Angular Speed')
slow_ax[1].plot(counts['slowCW'][:100], rot_speed['slowCW'][:100])
slow_ax[1].set_xlabel('Sample Count')
slow_ax[1].set_ylabel('Output Shaft Angular Speed (degrees/second)')
slow_ax[3].set_title('CCW Slow Speed Output Shaft Angular Speed')
slow_ax[3].plot(counts['slowCCW'][:100], rot_speed['slowCCW'][:100])
slow_ax[3].set_xlabel('Sample Count')
slow_ax[3].set_ylabel('Output Shaft Angular Speed (degrees/second)')

med_fig, med_ax = plt.subplots(nrows=4, ncols=1, figsize=(11,11), layout='constrained')
med_ax[0].set_title('CW Medium Speed Encoder Values')
med_ax[0].plot(counts['medCW'][:100], EncoderA['medCW'][:100])
med_ax[0].plot(counts['medCW'][:100], EncoderB['medCW'][:100])
med_ax[0].set_xlabel('Sample Count')
med_ax[0].set_ylabel('Encoder Values')
med_ax[2].set_title('CCW Medium Speed Encoder Values')
med_ax[2].plot(counts['medCCW'][:100], EncoderA['medCCW'][:100])
med_ax[2].plot(counts['medCCW'][:100], EncoderB['medCCW'][:100])
med_ax[2].set_xlabel('Sample Count')
med_ax[2].set_ylabel('Encoder Values')
med_ax[1].set_title('CW Medium Speed Output Shaft Angular Speed')
med_ax[1].plot(counts['medCW'][:100], rot_speed['medCW'][:100])
med_ax[1].set_xlabel('Sample Count')
med_ax[1].set_ylabel('Output Shaft Angular Speed (degrees/second)')
med_ax[3].set_title('CCW Medium Speed Output Shaft Angular Speed')
med_ax[3].plot(counts['medCCW'][:100], rot_speed['medCCW'][:100])
med_ax[3].set_xlabel('Sample Count')
med_ax[3].set_ylabel('Output Shaft Angular Speed (degrees/second)')

fast_fig, fast_ax = plt.subplots(nrows=4, ncols=1, figsize=(11,11), layout='constrained')
fast_ax[0].set_title('CW Fast Speed Encoder Values')
fast_ax[0].plot(counts['fastCW'][:100], EncoderA['fastCW'][:100])
fast_ax[0].plot(counts['fastCW'][:100], EncoderB['fastCW'][:100])
fast_ax[0].set_xlabel('Sample Count')
fast_ax[0].set_ylabel('Encoder Values')
fast_ax[1].set_title('CW Fast Speed Output Shaft Angular Speed')
fast_ax[1].plot(counts['fastCW'][:100], rot_speed['fastCW'][:100])
fast_ax[1].set_xlabel('Sample Count')
fast_ax[1].set_ylabel('Output Shaft Angular Speed (degrees/second)')
fast_ax[2].set_title('CCW Fast Speed Encoder Values')
fast_ax[2].plot(counts['fastCCW'][:100], EncoderA['fastCCW'][:100])
fast_ax[2].plot(counts['fastCCW'][:100], EncoderB['fastCCW'][:100])
fast_ax[2].set_xlabel('Sample Count')
fast_ax[2].set_ylabel('Encoder Values')
fast_ax[3].set_title('CCW Fast Speed Output Shaft Angular Speed')
fast_ax[3].plot(counts['fastCCW'][:100], rot_speed['fastCCW'][:100])
fast_ax[3].set_xlabel('Sample Count')
fast_ax[3].set_ylabel('Output Shaft Angular Speed (degrees/second)')

plt.show()


# ax[2].plot(counts['medCW'], EncoderA['medCW'])
# ax[2].plot(counts['medCW'], EncoderB['medCW'])
# ax[2].set_xlabel('Sample Count')
# ax[2].set_ylabel('Encoder Values')

# ax[3].plot(counts['medCCW'], EncoderA['medCCW'])
# ax[3].plot(counts['medCCW'], EncoderB['medCCW'])
# ax[3].set_xlabel('Sample Count')
# ax[3].set_ylabel('Encoder Values')

# ax[4].plot(counts['fastCW'], EncoderA['fastCW'])
# ax[4].plot(counts['fastCW'], EncoderB['fastCW'])
# ax[4].set_xlabel('Sample Count')
# ax[4].set_ylabel('Encoder Values')

# ax[5].plot(counts['fastCCW'], EncoderA['fastCCW'])
# ax[5].plot(counts['fastCCW'], EncoderB['fastCCW'])
# ax[5].set_xlabel('Sample Count')
# ax[5].set_ylabel('Encoder Values')

plt.show()

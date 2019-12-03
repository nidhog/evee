import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np



fig = plt.figure()
fig.canvas.draw()
track_general = pd.read_csv('data/track_general.csv')
track_hbts = pd.read_csv('data/track_hbts.csv')
all = pd.merge(left=track_general,right=track_hbts, left_on='DAY', right_on='DAY')
print(track_general.describe())
print(all.describe())
#sns.set()
#c = sns.lineplot(x=track_general.DAY, y=track_general['SLEEP SUBJECTIVE'])
#c.invert_yaxis()
#print([x for x in c.get_yticklabels()])
#plt.show()
#track_general = track_general[track_general['Workout (subjective)'] >= 5]
track_general = track_general[track_general['SLEEP SUBJECTIVE'] >= 5]
track_general['LATEST MEAL TIME'] = pd.to_datetime(track_general['LATEST MEAL TIME'], format='%H:%M')
track_general['LATEST MEAL TIME'] = [x.hour+x.minute/60.0 for x in track_general['LATEST MEAL TIME']]

track_general['BREAK FAST TIME'] = pd.to_datetime(track_general['BREAK FAST TIME'], format='%H:%M')
track_general['BREAK FAST TIME'] = [x.hour+x.minute/60.0 for x in track_general['BREAK FAST TIME']]
#track_general['Workout (subjective)'] = track_general['Workout (subjective)'].shift(1)
ax = sns.regplot(y=track_general['PRODUCTIVITY (SUBJECTIVE)'], x=track_general['SLEEP SUBJECTIVE'],
                 #scatter_kws={"s": 80}, order=6, ci=None, truncate=True)
                 x_estimator=np.mean, logx=True, truncate=True)
                 #x_estimator=np.mean, logx=True, truncate=True)
#ax2 = sns.lineplot(y=track_general['LATEST MEAL TIME'], x=track_general['LATEST MEAL TIME'])
plt.show()
#c.set_xticklabels(labels=c.get_xticklabels(), rotation=90)

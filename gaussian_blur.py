from scipy.ndimage import gaussian_filter1d
import pandas as pd
import glob
import ast
import numpy as np
import matplotlib.pyplot as plt
from pykalman import KalmanFilter

for filename in glob.glob('lab2_rss/*.txt'):
    start_df = pd.DataFrame.from_dict(ast.literal_eval(open(filename, 'r').read()))
    start_df['rss'] = start_df['rss'].astype(np.float64)
    for (name, df) in start_df.groupby('mac'):
        # kf = KalmanFilter()
        # kf = kf.em(df['rss'])
        # (fsm, fsv) = kf.filter(df['rss'])
        # (ssm, ssv) = kf.smooth(df['rss'])
        # df['rss fsm'] = fsm
        # df['rss ssm'] = ssm
        df['rss gf'] = gaussian_filter1d(df['rss'].values, 5)

        # plt.scatter(x=df['time'], y=fsm)
        # plt.scatter(x=df['time'], y=ssm)
        plt.scatter(x=df['time'], y=df['rss'])
        plt.scatter(x=df['time'], y=df['rss gf'])
        plt.show()
    exit(0)
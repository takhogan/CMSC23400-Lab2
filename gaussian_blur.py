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
    kf = KalmanFilter()
    kf = kf.em(start_df['rss'])
    (fsm, fsv) = kf.filter(start_df['rss'])
    (ssm, ssv) = kf.smooth(start_df['rss'])
    start_df['rss fsm'] = fsm
    start_df['rss ssm'] = ssm
    start_df['rss gf'] = gaussian_filter1d(start_df['rss'].values, 10)

    plt.scatter(x=start_df['time'], y=fsm)
    plt.scatter(x=start_df['time'], y=ssm)
    plt.scatter(x=start_df['time'], y=start_df['rss'])
    plt.scatter(x=start_df['time'], y=start_df['rss gf'])
    plt.show()
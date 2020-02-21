import pandas as pd
import ast
import json
import matplotlib.pyplot as plt
import numpy as np
import glob

for filename in glob.glob('lab2_rss/*.txt'):
    start_df = pd.DataFrame.from_dict(ast.literal_eval(open(filename, 'r').read()))
    start_df['rss'] = start_df['rss'].astype(np.float64)
    start_df.plot(x='time', y='rss')
    # print(start_df.dtypes)
    plt.show()


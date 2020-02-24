import pandas as pd
import glob
import ast
import numpy as np
import os
from sklearn.linear_model import LogisticRegression

def parse_training_data_file(filename):
    file_df = pd.DataFrame.from_dict(ast.literal_eval(open(filename, 'r').read()))
    # file_df.columns = ['rss', 'ypos', 'macid', 'xpos', 'time']
    file_df['rss'] = file_df['rss'].astype(np.float64)
    # file_df.drop(file_df[file_df.macid == 'f8:a9:d0:1c:b4:34'].index, inplace=True)
    # print(file_df.head())
    return file_df

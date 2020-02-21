import pandas as pd
import glob
import ast
import os
from sklearn.linear_model import LogisticRegression

def parse_training_data_file(filename):
    filename_split = os.path.splitext(os.path.basename(filename))[0]
    filename_split = filename_split.split('-')
    xpos = filename_split[3]
    ypos = filename_split[1]
    rss = filename_split[0]
    macid = filename_split[2]
    time = filename_split[4]
    with open(filename, 'r') as f:
        file_data_dict = ast.literal_eval(f.read())['seq']
        file_timestamps = [{'time': data_point['time']} for data_point in file_data_dict]
        file_data = [{key: value for key, value in data_point['data'].items()} for data_point in file_data_dict]
        for (timestamp, data_point) in zip(file_timestamps, file_data):
            timestamp.update(data_point)
        file_data_flat = file_timestamps
        file_df = pd.DataFrame.from_dict(file_data_flat)
        file_df['xpos'] = xpos
        file_df['ypos'] = ypos
        file_df['rss'] = rss
        file_df['macid'] = macid
        fild_df['time'] = time
        #file_df = file_df.drop(file_df.index[(file_df['time'] < 0.25)])
    return file_df

#!/usr/bin/python3

import pandas as pd
import columns
from math import log10, sqrt
import statsmodels.api as sm

COORDS = {
    "f8:cf:c5:97:e0:9e" : (304, 0),
    "ec:d0:9f:db:e8:1f" : (0, 0),
    "cc:fa:00:cb:f4:1d" : (168, 317)
}

def dist(p1, p2):
    return sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))

def main():
    # import data
    # columns: xpos | ypos | rss | macid
    dataframe = columns.parse_training_data_file(FILE)
    # calc logd
    logd = []
    for i, row in dataframe.iterrows():
        d = dist(COORDS[row['macid']], (row['xpos'], row['ypos']))
        logd.append(log10(d))
    dataframe['logd'] = logd
    # now let's do a linear regression! rss = B + A[logd]
    X = sm.add_constant(dataframe['logd']) 
    Y = dataframe['rss']

    model = sm.OLS(Y.astype(float), X.astype(float)).fit()
    predictions = model.predict(X)

    print(model.summary())


if __name__ == '__main__':
    main()

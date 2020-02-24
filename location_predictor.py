import glob
import ast
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn import linear_model
import matplotlib.pyplot as plt
from calcpathloss import *
from gaussian_blur import blur_df


for filename in glob.glob('lab2_rss/*.txt'):
    # start_df = pd.DataFrame.from_dict(ast.literal_eval(open(filename, 'r').read()))
    # start_df['rss'] = start_df['rss'].astype(np.float64)
    # start_df['log distances'] = 0
    dataframe = columns.parse_training_data_file(filename)
    # calc logd
    for i, row in dataframe.iterrows():
        if row['mac'] == 'f8:a9:d0:1c:b4:34':
            continue
        dataframe.loc[dataframe.index[i], 'logd'] = log10(dist(COORDS[row['mac']], (row['loc_x'], row['loc_y'])))
    dataframe = blur_df(dataframe)
    # print(dataframe[dataframe['mac'] == 'f8:a9:d0:1c:b4:34'])

    regression_df = dataframe[dataframe['mac'] != 'f8:a9:d0:1c:b4:34']

    x = np.expand_dims(regression_df['logd'].values, axis=1)
    y = np.expand_dims(regression_df['rss gf'], axis=1)
    # x = sm.add_constant(x)

    # Note the difference in argument order
    # model = sm.OLS(y, x).fit()
    # predictions = model.predict(x)
    lm = linear_model.LinearRegression(fit_intercept=True)
    model = lm.fit(x, y)
    predictions = model.predict(x)
    # print(regression_df['logd'])
    # print(regression_df['rss gf'])
    plt.scatter(x=regression_df['logd'], y=regression_df['rss gf'])
    plt.scatter(x=regression_df['logd'], y=predictions)
    plt.show()

    coefficients = (model.intercept_, model.coef_)
    print(coefficients)
    exit(0)




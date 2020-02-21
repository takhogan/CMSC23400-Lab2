import glob
import ast
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn import linear_model
import matplotlib.pyplot as plt


for filename in glob.glob('lab2_rss/*.txt'):
    start_df = pd.DataFrame.from_dict(ast.literal_eval(open(filename, 'r').read()))
    start_df['rss'] = start_df['rss'].astype(np.float64)

    # start_df['log distances'] = 0

    x = start_df['log distances']
    y = start_df['rss']
    # x = sm.add_constant(x)

    # Note the difference in argument order
    # model = sm.OLS(y, x).fit()
    # predictions = model.predict(x)
    lm = linear_model.LinearRegression(fit_intercept=True)
    model = lm.fit(x, y)
    predictions = model.predict(x)
    plt.scatter(start_df['time'])

    # Print out the statistics
    print(type(model))

    exit(0)



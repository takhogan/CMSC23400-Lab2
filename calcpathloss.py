#!/usr/bin/python3

import pandas as pd

FILE="datafixed.txt"

def main():
    # import data
    # columns: xpos | ypos | rss | macid
    dataframe = pd.read_csv(FILE)
    # calculate regression from 


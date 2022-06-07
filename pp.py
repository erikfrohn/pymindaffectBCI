import csv
import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def pp():
    
    #path2 = "csv/"
    #dir_list2 = os.listdir(path2)
    
    original= "csv/"
    dir_list_o = os.listdir(original)

    path1 = []

    for i in dir_list_o:
        path1.append(original+i+'/')

    path2 = []

    for i in range(len(path1)):
        DatasetsPerCommit = os.listdir(path1[i])
        for j in range(len(DatasetsPerCommit)):
            path2.append(path1[i]+DatasetsPerCommit[j])
    
    #list_csv = glob.glob('csv/*/*.csv')
    #dfs = []

    path_list = []

    for path in path2:
        path_list.append(path.split(os.sep))

    time = [path[1] for path in path_list]

    for i in (path2):
        df = pd.read_csv(i)
        dfs.append(df)

    column_names = dfs[0].columns.tolist()
    columns_names2 = dfs[4].columns.tolist()

    #list_csv2 = glob.glob('csv/**/metadata.csv')

    #mds = []

    #for i in (list_csv2):
        #md = pd.read_csv(i, index_col=False)
        #mds.append(md)

    #column_names3 = mds[0].columns.tolist()

    return dfs, column_names, columns_names2, path_list, time #mds column_names3

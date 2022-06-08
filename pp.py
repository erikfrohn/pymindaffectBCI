import csv
import pandas as pd
import numpy as np
import os

def pp():
    
    ''' it returns generic variables (dataframes, paths, column names of the dataframes and sha keys) of the csv files, 
    that are created by the pipelines '''
    
    #it finds the children of the grandparents 
    original= "csv/"
    dir_list_o = os.listdir(original)

    path1 = []

    #it creates the path for grandparents and parents; example: csv/ed235sdf/
    for i in dir_list_o:
        path1.append(original+i+'/')

    path2 = []
    
    #it finds the children of parents and it creates the final path; example: csv/ed235sdf/kaggle.csv
    for i in range(len(path1)):
        DatasetsPerCommit = os.listdir(path1[i])
        for j in range(len(DatasetsPerCommit)):
            path2.append(path1[i]+DatasetsPerCommit[j])
    
    dfs = []
    path_list = []
    
    
    #it tokenizes/seperates the paths; csv/ed235sdf/kaggle.csv -> [csv, ed235sdf, kaggle.csv]
    for path in path2:
        path_list.append(path.split(os.sep))

    #it finds the commit sha keys 
    sha = [path[1] for path in path_list]

    #it creates the pandas dataframes of the csv files 
    for i in (path2):
        df = pd.read_csv(i)
        dfs.append(df)

    #headers of the csv files
    column_names = dfs[0].columns.tolist()
    columns_names2 = dfs[4].columns.tolist()

    return dfs, column_names, columns_names2, path_list, sha  

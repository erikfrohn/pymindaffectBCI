import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from pp import pp

def app():
    '''it plots the different metrics of a dataset (id) and the dataset of the next commit (id2) in the dashboard:
    the generic variables are preprocessed until they are formatted correctly for the charts '''

    dfs, column_names, columns_names2, path_list, time  = pp()  
    
    #first dataset (your first commit)
    perr = []
    perr_e = []
    se = []
    ste = []
    id = 4
    
    #it appends the different metrics(perr, perr_e, se and st) of the dataset (id)
    perr.append(dfs[id]['prob_err'])
    perr_e.append (dfs[id]['prob_err_est'])
    se.append(dfs[id]['se'] )
    ste.append(dfs[id]['st'])

    new_perr = np.array(perr)
    new_perr_e = np.array(perr_e)
    new_se = np.array(se)
    new_st = np.array(ste)
    
    #it finds the file name 
    file = [path[2] for path in path_list]
    name = file[id]

    #the final data for the chart; reshaped to 2 dimensions.
    input = np.array([new_perr, new_perr_e, new_se, new_st]).reshape(4,30)

    #it creates the line chart
    source = pd.DataFrame(np.transpose(input), columns=['Perr', 'Perr_est', 'Se', 'St'])
    st.header(name)
    st.line_chart(source)
    
    #second dataset (the commit after the first commit above); same steps applied as above
    perr2 = []
    perr_e2 = []
    se2 = []
    ste2 = []
    
    id2 = id+18 

    perr2.append(dfs[id2]['prob_err'])
    perr_e2.append(dfs[id2]['prob_err_est'])
    se2.append(dfs[id2]['se'])
    ste2.append(dfs[id2]['st'])

    new_perr2 = np.array(perr2)
    new_perr_e2 = np.array(perr_e2)
    new_se2 = np.array(se2)
    new_st2 = np.array(ste2)

    file2 = [path[2] for path in path_list]
    name2 = file[id2]

    input2 = np.array([new_perr2, new_perr_e2, new_se2, new_st2]).reshape(4,30)

    source2 = pd.DataFrame(np.transpose(input2), columns=['Perr', 'Perr_est', 'Se', 'St'])
    st.header(name2)
    st.line_chart(source2)

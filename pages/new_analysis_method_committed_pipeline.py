import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from pp import pp

def app():
    
    '''it plots the average audc of kaggle, lowlands, plos_one over the commits you make in order:
    the generic variables are preprocessed until they are formatted correctly for the charts'''
    
    st.header("Performance tracking")

    dfs, column_names, columns_names2, path_list, sha  = pp() 

    avg_k_audc = []
    avg_l_audc = []
    avg_p_audc = []
    
    #it finds the csv names
    id = [path[2] for path in path_list]

    id_array = np.array([id])
    
    #it finds all indices of specific csv file names
    id_k = np.where(id_array == 'kaggle.csv')[1]
    
    id_l = np.where(id_array == 'lowlands.csv')[1]
    
    id_p = np.where(id_array == 'plos_one.csv')[1]
    
    l_k = id_k.tolist()
    l_l = id_l.tolist()
    l_p = id_p.tolist()
    
    #it finds all the occured csv files of a specific name
    for i in range(len(l_k)):
        id1 = id_k[i]
        id2 = id_l[i]
        id3 = id_p[i]
        avg_k_audc.append( dfs[id1]['ave-AUDC']) 
        avg_l_audc.append( dfs[id2]['ave-AUDC'])
        avg_p_audc.append( dfs[id3]['ave-AUDC']) 

    new_k_audc = np.array(avg_k_audc)
    new_l_audc = np.array(avg_l_audc)
    new_p_audc = np.array(avg_p_audc)

    input = np.array([new_k_audc[:,0], new_l_audc[:,0], new_p_audc[:,0]])
    
    #it creates the chart; first dataframe and secondly manipulations on the charts (title, x-axis and y-axis)
    source = pd.DataFrame(np.transpose(input),
                          columns=['Kaggle', 'Lowlands', 'Plos_one'], index=pd.RangeIndex(1, len(avg_k_audc)+1, name='Commit-ID'))
    source = source.reset_index().melt('Commit-ID', var_name='dataset', value_name='avg-AUDC')
    line = alt.Chart(source).mark_line(interpolate='basis').encode(
        x='Commit-ID:Q',
        y='avg-AUDC:Q',
        color='dataset:N'
    ).properties(
    title='Average AUDC across commits'
)
    st.altair_chart(line, use_container_width=True)
    
    #it creates a table with the commit ids and the corresponding sha keys
    col1, col2 = st.columns([2, 1])
    col1.write(pd.DataFrame({'Commit-ID': range(1, len(sha)+1),
         'SHA': sha
     }))

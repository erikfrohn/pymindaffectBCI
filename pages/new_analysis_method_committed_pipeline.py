import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from pp import pp

def app():
    st.header("Performance tracking")

    # df = pd.DataFrame([[20.500, 15.513, 90.667], [57.833, 23.077, 34.667],[46.000, 32.436, 30.333],[36.667, 20.256, 25.222],[46.000, 28.718, 33.456]], columns=['kaggle', 'plos_one', 'lowlands'])
    # df.index.name = "Dataset-ID"
    # df.set_index([pd.Index([1, 2, 3, 4,5])])
    # data = df.reset_index().melt('Dataset-ID')
    # c = alt.Chart(data).mark_line().encode(
    #     x='Dataset-ID',
    #     y='value',
    #     color='variable'
    # )
    #test

    dfs, column_names, columns_names2, columns_names2, path_list, time, mds = pp()

    k_audc = dfs[0]['AUDC']
    l_audc = dfs[1]['AUDC']
    p_audc = dfs[3]['AUDC']

    new_k_audc = np.array(k_audc).transpose()
    new_l_audc = np.array(l_audc).transpose()
    new_p_audc = np.array(p_audc).transpose()

    source = pd.DataFrame(new_k_audc,
                          columns=['Kaggle'])

    source2 = pd.DataFrame(new_l_audc,
                          columns=['Lowlands'])
    
    source3 = pd.DataFrame(new_p_audc,
                          columns=['Plosone'])

    st.line_chart(source)
    st.line_chart(source2)
    st.line_chart(source3)

    #source = source.reset_index().melt('Commit-ID', var_name='dataset', value_name='avg-AUDC')
    #line = alt.Chart(source).mark_line(interpolate='basis').encode(
    #   x='Commit-ID',
    #    y='avg-AUDC',
    #).properties(
    #title='Average AUDC across commits'
#)
    #st.altair_chart(line, use_container_width=True)
    # col1, col2 = st.columns(2)


    branch = []
    #time = []

    for i in mds:
        branch.append(i['branch'])
        #time.append(i['current_date_and_time'])

    sha = np.unique(np.array(time))

    col1, col2 = st.columns([2, 1])
    col1.write(pd.DataFrame({'Commit-ID': range(len(sha)),
        'SHA': sha
    }))
    # col1.write(pd.DataFrame({'Data source': ['Kaggle', 'Plos_one', 'Lowlands'],
    #     'Dataset name': ['mindaffectBCI_noisetag_bci_201029_1340_ganglion.txt','Perr_plos_one_supervised_...','LL_eng_02_20170818_tr_train_1.mat']
    # }))

    unique_branches = np.unique(np.array(branch))

    count_branch = []

    #for br in unique_branches:
        #count_branch.append(branch.count(br))
        
    source = pd.DataFrame({
        'Branch': unique_branches,
        '#commits': 2 
    })

    c= alt.Chart(source).mark_bar().encode(
        x='Branch',
        y='#commits'
    )
    col2.altair_chart(c, use_container_width=True)

    # col1, col2 = st.columns(2)
    # chart_data = pd.DataFrame(
    #     np.array([[1, 2, 3], [4, 5, 6],[4, 5, 6]]),
    #     columns=['open_source', 'master', 'wip'])
    #
    # col1.line_chart(chart_data)
    # #col2.chart_data.
    #
    # col2.write(pd.DataFrame({
    #     'first column': [1, 2, 3, 4],
    #     'second column': [10, 20, 30, 40]
    # }))
    #
    # col3, col4 = st.columns(2)
    # chart_data2 = pd.DataFrame(
    #     np.array([[20.500, 15.513, 90.667], [57.833, 23.077, 34.667],[46.000, 32.436, 30.333],[36.667, 20.256, 25.222],[46.000, 28.718, 33.456]]),
    #     columns=['kaggle', 'plos_one', 'lowlands'])
    #
    # # col3.line_chart(chart_data2)
    #
    # line_chart = alt.Chart(chart_data2).mark_line(interpolate='basis').encode(
    # alt.X('x', title='Year'),
    # alt.Y('y', title='Amount in liters'),
    # color='category:N'
    # ).properties(
    # title='Sales of consumer goods'
    # )
    #
    # st.altair_chart(line_chart)

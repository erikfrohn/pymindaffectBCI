import datetime
from git import Repo
import csv
import os
import numpy as np
from mindaffectBCI.decoder.decodingCurveSupervised import score_decoding_curve, flatten_decoding_curves
from mindaffectBCI.decoder.analyse_datasets import average_results_per_config


def get_metadata():
    '''
    Computes metadata (current time, sha, branch)
    '''
    current_date_and_time = datetime.datetime.now()
    repo = Repo(search_parent_directories=True)
    sha = repo.head.object.hexsha
    branch = repo.active_branch.name
    return current_date_and_time, sha, branch

def meta2csv():
    '''
    Computes metadata and converts to metadata.csv file
    '''
    current_date_and_time, sha, branch = get_metadata()
    try:
        os.mkdir('csv/' + sha)
    except:
        print("Overwriting sha directory, it already exists: "+sha)
    with open('csv/'+ sha +'/metadata.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['current_date_and_time', 'sha', 'branch'])
        writer.writerow([current_date_and_time, sha, branch])
    
    return sha

def save_csv_summaries(dataset, filenames, clsfr, res, dir):
    '''
    Saves csv files for the dataset summaries in csv/current-sha folder.
    It saves: filename, classifier, audc, ave-audc, baseline-audc
    File examples: kaggle.csv, lowlands.csv, etc
    '''
    ## ---------------------------
    ## ---------------------------
    # SAVE SUMMARY PER DATA REPO (kaggle, lowlands, etc.)
    ## ---------------------------
    ## ---------------------------

    # Save to a CSV file
    # Find where the data came from
    name_file = dataset+'.csv'

    # Clean up string
    string_clsfr = str(clsfr).replace('\n', '')
    string_clsfr = string_clsfr.replace(',', ';')
    string_clsfr = string_clsfr.replace('  ', '')

    # Get data into csv file.
    ave_dc = score_decoding_curve(*(average_results_per_config(res)['decoding_curve'][0]))['audc']
    data_int = np.transpose(np.array([filenames, [string_clsfr]*len(filenames), [str("%.3f" % x) for x in res['audc']], [str("%.3f" % ave_dc)]*len(filenames), [51.9]*len(filenames)]))
    with open('csv/'+dir+ name_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['file', 'clsfr', 'AUDC', 'ave-AUDC', 'baseline-AUDC'])
        writer.writerows(data_int)

def save_csv_separate_files(filenames, res, dir):
    '''
    Saves csv files for separate datafiles in csv/current-sha folder.
    It saves the decoding information table summary (int_len, prob_err, prob_err_est, se, st).
    File example: _LL_eng_02_20170818_tr_train_1_mat.csv
    '''
    ## ---------------------------
    ## ---------------------------
    # SAVE TABLE PER DATASET FILE
    ## ---------------------------
    ## ---------------------------

    for i,file in enumerate(filenames):
        # Parse filename such that it becomes e.g. '_LL_eng_02_20170818_tr_train_1_mat.csv'
        fn = 'file'
        ll = file.split('lowlands')
        kg = file.split('kaggle')
        p1 = file.split('plos_one')
        if len(ll) > 1:
            fn = ll[1]
            fn = fn.replace('\\', '_')
            fn = fn.replace('.', '_')+'.csv'
        if len(kg) > 1:
            fn = kg[1]
            fn = fn.replace('\\', '_')
            fn = fn.replace('.', '_')+'.csv'
        if len(p1) > 1:
            fn = p1[1]
            fn = fn.replace('\\', '_')
            fn = fn.replace('.', '_')+'.csv'
        fn = dir + fn

        # Try writing the csv file with the name of the file that is analysed
        data_int = np.transpose(((np.array([flatten_decoding_curves(res['decoding_curve'])])[:,:,i]).flatten()).reshape(5,30))
        try:
            with open('csv/'+fn, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["int_len", "prob_err", "prob_err_est", "se", "st"])
                writer.writerows(data_int)
        except:
            print("Error writing "+file)

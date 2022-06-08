import csv
import pandas as pd
import os

def find_newest_sha():
    '''
    Finds the newest sha according to its datetime stored in metadata.csv
    Returns the sha of the newest sha folder.
    '''

    times = []
    shas = []
    for root, dirs, files in os.walk("csv"):
        # Search directories in the csv folder
        for dir in dirs:
            # Look in metadata.csv and store the datetimes
            metadata = pd.read_csv("csv/"+dir+"/metadata.csv")
            times.append(metadata['current_date_and_time'][0])
            shas.append(metadata['sha'][0])

    # Find the maximum datetime (the newest)
    m = max(times)
    newest_idx = times.index(m)
    sha = shas[newest_idx]
    # And return the corresponding sha
    return sha


def convert():
    '''
    Reads the generated csv files from csv/'the newest sha' and converts 
    them to .txt files, with markdown table format, in the same directory
    Also saves a summary of these .txt files in metrics.txt, which are these
    files appended below eachother.
    
    The files read are e.g. kaggle.csv, lowlands.csv, plos_one.csv
    Output files are e.g. kaggle.txt, lowlands.txt, plos_one.txt
    '''

    sha = find_newest_sha()

    files = ['kaggle', 'lowlands', 'plos_one']
    # Convert .csv into .txt with markdown for a table
    try:
        for fn in files:
            csv_file = sha+'/'+fn+'.csv'
            txt_file = fn+'.txt'
            with open(txt_file, "w") as my_output_file:
                with open('csv/'+csv_file, "r") as my_input_file:
                    [ my_output_file.write("|"+" | ".join(row)+' |\n') for row in csv.reader(my_input_file)]
                my_output_file.close()

            with open(fn+'.txt', 'r') as f:
                contents = f.readlines()
            contents.insert(1, '|---|---|---|---|---|\n')
            with open(fn+'.txt', 'w') as f:
                contents = "".join(contents)
                f.write(contents)
    except:
        print("Error opening file: "+fn)
        
    # Clear the file
    output = 'metrics.txt'
    open(output, 'w').close()

    try:
        for fn in files:
            input = fn+'.txt'
            
            # Write metrics for each data (kaggle, plos_one, etc)
            with open(output, "a") as my_output_file:
                with open(input, "r") as my_input_file:
                    my_output_file.write("## "+fn+"\n")
                    [ my_output_file.write("".join(row)+'\n') for row in csv.reader(my_input_file)]
    except:
        print("Error opening file: "+fn)

if __name__ == "__main__":
    convert()
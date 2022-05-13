from simpledbf import Dbf5
from os import listdir
from os.path import isfile, join, isdir
import pandas as pd
import argparse

# Encoding for your dbf files
ENCODING = 'ISO8859-1'

# Args
parser = argparse.ArgumentParser()
parser.add_argument("--path", help="Dir or file path", required=True)
args = parser.parse_args()

# Func to convert dbf to csv using simpledbf
def dbf_to_csv(path):
    dir = path.split('\\')[-2]
    file_name = path.split('\\')[-1].split('.')[0]
    print(f'Converting {file_name}.dbf...')
    try:
        dbf = Dbf5(path, codec=ENCODING)
        df = dbf.to_dataframe()
        df.to_csv(f'{dir}\{file_name}.csv', index=False)
        print(f'Conversion to {file_name}.csv successful')
    except Exception as err:
        print(f'ERROR IN FILE {file_name}.dbf: {err}')

def main():
    # If path ends with \, remove it
    path = args.path[:-1] if args.path.endswith("\\") else args.path

    # If path is a folder
    if isdir(path):
        # Getting all DBF files from folder
        files = [f for f in listdir(path) if isfile(join(path, f)) and f.lower().endswith('dbf')]
        for file in files:
            dbf_to_csv(path + "\\" + file)
    # If path is a file
    elif isfile(path):
        dbf_to_csv(path)
    else:
        print(f'Invalid path: {path}')

if __name__ == "__main__":
    main()
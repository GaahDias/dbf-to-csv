from simpledbf import Dbf5
from os import listdir
from os.path import isfile, join, isdir
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--path", help="Dir or file path", required=True)
args = parser.parse_args()

def dbf_to_csv(path):
    dir = path.split('\\')[-2]
    file_name = path.split('\\')[-1].split('.')[0]
    print(f'Converting {file_name}.dbf...')
    try:
        dbf = Dbf5(path, codec='unicode_escape')
        dbf.to_csv(f'{dir}\{file_name}.csv')
        print(f'Conversion to {file_name}.csv successful')
    except Exception as err:
        print(f'ERROR IN FILE {file_name}.dbf: {err}')

def main():
    path = args.path[:-1] if args.path.endswith("\\") else args.path
    if isdir(path):
        files = [f for f in listdir(path) if isfile(join(path, f)) and f.lower().endswith('dbf')]
        for file in files:
            dbf_to_csv(path + "\\" + file)
    elif isfile(path):
        dbf_to_csv(path)
    else:
        print(f'Invalid path: {path}')

if __name__ == "__main__":
    main()
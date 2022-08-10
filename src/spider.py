import argparse
from os.path import abspath
from os import getcwd

# Target default directory of downloads
default_path = abspath(getcwd())+"/data"

# Main
def run_spyder():
    args = config_args()
    print(args)

# Flags configurations
def config_args():
    parse = argparse.ArgumentParser(
        description= "*** Arachnida - Spider ***"
    )
    parse.add_argument("-r","--recursive", default=None, help="[-r URL] Recursive mode.")
    parse.add_argument("-l","--level", default=5, help="[-r URL -l N] Recursive mode + level of scanning.")
    parse.add_argument("-p","--path", default=default_path, help="[-r URL -p path] Dyrectory of downloads.")
    parse.add_argument("-S","--silent", default=False, action="store_true", help="Silent mode.")
    return parse.parse_args()

print(default_path)

if __name__=="__main__":
    run_spyder()
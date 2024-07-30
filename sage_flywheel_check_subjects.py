#!/usr/bin/env python
import flywheel
import argparse
from subprocess import call
import os

#Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("api_key_file", help="file that has flywheel api key")
args = parser.parse_args()
api_key_file = args.api_key_file
code_dir = os.path.dirname(os.path.realpath(__file__))

with open(api_key_file,'r') as file:
    api_key = file.read().replace('\n','')

#Set up the flywheel API
fw = flywheel.Client(api_key)

#Get the SAGE project
project_id = "64935df4a60b3a64d6add007"
project = fw.get(project_id)

to_exclude = ["12834"]

to_bidsify = []
for subject in project.subjects():
    session = subject.sessions()[0]
    if 'BIDS' not in session.info.keys() and subject not in to_exclude:
        to_bidsify.append(subject.code)
    else:
        #first run we just do them all
        to_bidsify.append(subject.code)


print("The following subjects will need to have the Curate BIDS gear run:")
print(to_bidsify)

for subject in to_bidsify:
    # command = "%s/sage_flywheel_fixbids.py %s" % (code_dir,subject)
    # print(command)
    # call(command,shell=True)
    files = os.listdir("/Volumes/BCI/SAGE/BIDS_data/sub-%s/ses-EichSAGE/anat/" % subject)
    print(files)

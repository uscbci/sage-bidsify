#!/usr/bin/env python
import argparse
from subprocess import call
import flywheel
import os

#Command line arguments
parser = argparse.ArgumentParser()
# parser.add_argument("subject", help="subject to be processed")
parser.add_argument("api_key", help="flywheel api key")
args = parser.parse_args()
# subject_code = args.subject
api_key = args.api_key

#Set up the flywheel API
fw = flywheel.Client(api_key)

#Get the SAGE project
project_id = "64935df4a60b3a64d6add007"
project = fw.get(project_id)

to_exclude = ["12834"]

to_bidsify = []
for subject in project.subjects():
    session = subject.sessions()[0]
    print("subject %s" % subject.code)
    if 'BIDS' in session.info.keys():
        print("BIDS already done")
        to_bidsify.append("sub-%s" % subject.code)
    else:
        print("Do BIDS first")



#destination for data to be saved
dest_folder = "/Volumes/BCI/SAGE/BIDS_data/"

donefolders = os.listdir(dest_folder)
donefolders.sort()
to_bidsify.sort()

numdone = len(to_bidsify)
print("BIDS Done (%d):" % numdone)
print(to_bidsify)

numdone = len(donefolders)
print("Already exported (%d):" % numdone)
print(donefolders)


to_bidsify = [elem[4:9] for elem in to_bidsify if elem not in donefolders]
numdone = len(to_bidsify)
print("Remaining to export (%d):" % numdone)
print(to_bidsify)

for subject_code in to_bidsify:


    #construct command line command
    command = "fw export bids --project \"SAGE\" --group \"teich\" --subject \"%s\" %s" %(subject_code,dest_folder)

    #run it
    print(command)
    call(command,shell=True)
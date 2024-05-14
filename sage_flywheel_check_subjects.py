#!/usr/bin/env python
import flywheel
import argparse

#Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("api_key", help="flywheel api key")
args = parser.parse_args()
api_key = args.api_key

#Set up the flywheel API
fw = flywheel.Client(api_key)

#Get the SAGE project
project_id = "64935df4a60b3a64d6add007"
project = fw.get(project_id)

to_bidsify = []
for subject in project.subjects():
    session = subject.sessions()[0]
    if 'BIDS' not in session.info.keys():
        to_bidsify.append(subject.code)

print(to_bidsify)
#!/usr/bin/env python
import flywheel
import argparse

#Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("api_key_file", help="flywheel api key file")
args = parser.parse_args()
api_key_file = args.api_key_file

with open(api_key_file,'r') as file:
    api_key = file.read().replace('\n','')

#Set up the flywheel API
fw = flywheel.Client(api_key)

#Get the SAGE project
project_id = "64935df4a60b3a64d6add007"
project = fw.get(project_id)

#Get the BIDS curation gear
bids_gear = fw.lookup("gears/curate-bids/2.1.5_1.1.5.2")

#Find the BIDS curation template
for file in project.files:
    if file.name == 'sage_bids_template_0.1.json':
        template_file = file


to_exclude = ["12834"]

to_bidsify = []
for subject in project.subjects():
    session = subject.sessions()[0]
    print("subject %s" % subject.code)
    if 'BIDS' in session.info.keys():
        print("BIDS already done")
    else:
        if subject not in to_exclude:
            to_bidsify.append(subject)
        else:
            print("Excluding this subject")

for subject in to_bidsify:
    print("Working on subject %s" % subject.code)

    #Set up the gear
    analysis_label = "bids curate"
    inputs = {'template':template_file}
    dest = subject

    #Run the gear
    job_id = bids_gear.run(analysis_label=analysis_label, inputs=inputs, destination=dest, config={'reset': True})

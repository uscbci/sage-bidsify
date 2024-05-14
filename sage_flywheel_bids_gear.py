#!/usr/bin/env python
import flywheel
import argparse

#Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("subject", help="subject to be processed")
parser.add_argument("api_key", help="flywheel api key")
args = parser.parse_args()
subject_code = args.subject
api_key = args.api_key

#Set up the flywheel API
fw = flywheel.Client(api_key)

#Get the SAGE project
project_id = "64935df4a60b3a64d6add007"
project = fw.get(project_id)

#Get the BIDS curation gear
bids_gear = fw.lookup("gears/curate-bids")

#Find the BIDS curation template
for file in project.files:
    if file.name == 'sage_bids_template_0.1.json':
        template_file = file

#Find the subject
subjects = project.subjects()
for subj in subjects:
    if subj.code == subject_code:
        subject = subj

#Set up the gear
analysis_label = "bids curate"
inputs = {'template':template_file}
dest = subject

#Run the gear
job_id = bids_gear.run(analysis_label=analysis_label, inputs=inputs, destination=dest, config={'reset': True})

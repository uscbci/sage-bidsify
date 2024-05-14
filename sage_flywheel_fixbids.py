#!/usr/bin/env python
import argparse
import os
import shutil
from subprocess import call

#Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("subject", help="subject to be processed")
args = parser.parse_args()
subject_code = args.subject

bids_folder = "/Users/jonask/fMRI/SAGE/data"
subject_folder = "%s/sub-%s" % (bids_folder,subject_code)
inner_folder = "%s/ses-EichSAGE" % subject_folder
fmap_folder = "%s/fmap" % inner_folder
code_dir = os.path.dirname(os.path.realpath(__file__))

if not os.path.exists(fmap_folder):
    os.mkdir(fmap_folder)

src_file = "%s/func/sub-%s_ses-EichSAGE_task-hiAP_run-01_bold.nii.gz" % (inner_folder,subject_code)
dest_file = "%s/sub-%s_ses-EichSAGE_dir-1_epi.nii.gz" % (fmap_folder,subject_code)
shutil.copyfile(src_file,dest_file)

src_file = "%s/func/sub-%s_ses-EichSAGE_task-hiPA_run-01_bold.nii.gz" % (inner_folder,subject_code)
dest_file = "%s/sub-%s_ses-EichSAGE_dir-2_epi.nii.gz" % (fmap_folder,subject_code)
shutil.copyfile(src_file,dest_file)

src_file = "%s/dir-1_epi.json" % code_dir
dest_file = "%s/sub-%s_ses-EichSAGE_dir-1_epi.json" % (fmap_folder,subject_code)
command = "sed 's/DEFINESUBJECT/%s/g' %s > %s" % (subject_code,src_file,dest_file)
print(command)
call(command,shell=True)


src_file = "%s/dir-2_epi.json" % code_dir
dest_file = "%s/sub-%s_ses-EichSAGE_dir-2_epi.json" % (fmap_folder,subject_code)
command = "sed 's/DEFINESUBJECT/%s/g' %s > %s" % (subject_code,src_file,dest_file)
print(command)
call(command,shell=True)
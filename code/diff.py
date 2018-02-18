""" Run diff on two files (the regular old 'diff' terminal command).  Report the results. """
import os
import subprocess
import re


def diff(file_path_1, file_path_2):
	cmd = ['diff', file_path_1, file_path_2]
	completed_process = subprocess.run(
		cmd,
		check=False,
		stdout=subprocess.PIPE,
		universal_newlines=True)
	out = completed_process.stdout
	return out

def is_different(fp1, fp2):
	if os.path.exists(fp1) and os.path.exists(fp2):
		# if the files exist
		raw_diff = diff(fp1, fp2)
		files_exist = True
		# see if the files are different
		if raw_diff == '':
			files_are_different = False
		else:
			files_are_different = True
	else:
		# if a file is missing
			files_exist = False
			files_are_different = None
	return (files_exist, files_are_different)

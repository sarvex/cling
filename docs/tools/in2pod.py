#!/usr/bin/env python

# A tool to parse cling.pod.in and generate cling.pod dynamically

from __future__ import print_function
import subprocess
import sys
import os
import inspect

SCRIPT_DIR=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
cling_binary=sys.argv[1]

cmd = subprocess.Popen(
	[f"echo .help | {cling_binary} --nologo"],
	stdout=subprocess.PIPE,
	shell=True,
)
(out, err) = cmd.communicate()
if not err:
	with open(f'{SCRIPT_DIR}/cling.pod', 'w') as pod_out:
		file_handler = open(f'{SCRIPT_DIR}/cling.pod.in')
		pod_in=file_handler.read()
		print(pod_in.replace("%help_msg%", out.decode()), file=pod_out)
	file_handler.close()

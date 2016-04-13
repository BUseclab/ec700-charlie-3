#! /usr/bin/env python

import sys, subprocess
from subprocess import check_output,CalledProcessError

return1 = None
return2 = None
return3 = None

try:
	return1 = subprocess.check_output(
		"dmesg | grep -i virtual",
		stderr=subprocess.STDOUT,
		shell=True)
except CalledProcessError as e:
    return1 = e.output
try:
	return2 = subprocess.check_output(
        	"dmidecode | egrep -i 'manufacturer|product'",
        	stderr=subprocess.STDOUT,
        	shell=True)
except CalledProcessError as e:
    return2 = e.output
try:
	return3 = subprocess.check_output(
        	"cat /proc/ide/hd*/model",
	        stderr=subprocess.STDOUT,
        	shell=True)
except CalledProcessError as e:
    return3 = e.output

print return1
print return2
print return3

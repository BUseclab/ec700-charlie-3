#! /usr/bin/env python

import subprocess, sys

return1 = subprocess.check_output(
	"dmesg | grep -i virtual",
	stderr=subprocess.STDOUT,
	shell=True)
#return2 = subprocess.check_output(
#        "dmidecode | egrep -i 'manufacturer|product'",
#        stderr=subprocess.STDOUT,
#        shell=True)

#return3 = subprocess.check_output(
#        "cat /proc/ide/hd*/model",
#        stderr=subprocess.STDOUT,
#        shell=True)


print return1
#print return2
#print return3

#! /usr/bin/env python3
import os, sys, re

def IOExample():
	output = os.open("shell-output.txt", os.O_CREAT | os.O_WRONLY)
	input = os.open("input.txt", os.O_RDONLY)

	while 1:
		read = os.read(input, 10000)
		if len(read) == 0: break
		lines = re.split(b"\n", read)
		for line in lines:
			strPrint = f"{line.decode()}\n"
			os.write(output, strPrint.encode())

def forkExample():
	pid = os.getpid()
	rc = os.fork()

	if rc == 0:
		print("Child id = %d" % (os.getpid()))
	else:
		print("Parent id = %d" % pid)

forkExample()

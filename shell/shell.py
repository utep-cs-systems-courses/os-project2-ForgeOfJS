#! /usr/bin/env python3
import os, sys, re, time

PS1 = "$"
dir = os.getcwd()

def awaitCommand():
	print(dir + PS1, end = " ")
	command = input()
	realCommand = command.split(" ")
	return realCommand

if len(sys.argv) > 1:
	bashCommand = ""
	for arg in sys.argv[1:]:
		bashCommand += arg
	os.system(bashCommand)

while True:
	command = awaitCommand()
	if command[0] == "exit": sys.exit("Shell Exit.")
	if command[0] == "cd":
		if len(command) == 2:
			if command[1] == "..":
				dir = os.path.abspath(os.path.join(dir, os.pardir))
			else:
				if  os.path.isdir(dir+"/"+command[1]): dir += "/"+command[1]
				else: print(f"'/{command[1]}' is not a valid path")
		if len(command) == 1:
			dir = "/"+dir.split("/")[1]
	elif command[0][0:2] == "./":
		print(f"{command} is to be executed")
		rc = os.fork()
		if rc < 0:
			sys.exit(f"Fork failed, returning '{rc}'")
		elif rc == 0:
			for directory in re.split(":", dir):
				try:
					os.execve(dir+"/"+command[0][2:], command[1:], os.environ)
				except FileNotFoundError:
					print(f"File {command[0][2:]} not found.")
		else:
			os.wait()

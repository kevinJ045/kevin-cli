import os
import cmd
import sys
import time
import math
import random
from clint.textui import progress
import hashlib
from threading import Timer

def joinArgs(a):
	return " ".join(a)

def cpr(text, color = "green"):
	ccode = 2
	if color == "blue":
		ccode = 4
	elif color == "red":
		ccode = 1
	elif color == "black":
		ccode = 0
	elif color == "white":
		ccode = 9
	elif color == "purple":
		ccode = 5
	elif color == "aqua":
		ccode = 6
	else:
		ccode = 2
	print("\033[3"+str(ccode)+"m"+text+"\033[39m")

def validbn(text):
	ext = text.split(".").pop()
	return ext == "brain" or ext == "session" or ext == "memory" or ext == "memories"

def loading(label = '', delay = 0.2, size = 20):
	with progress.Bar(label=label, expected_size=size, filled_char = '█') as bar:
		last_val = 0
		for val in range(1, size+1):
			time.sleep(delay * (val - last_val))
			bar.show(val)
			last_val = val

def loadBars(label = ''):
	for i in progress.mill(range(100), label = label):
		time.sleep(random.random() * 0.2)

def md5(t):
	return hashlib.md5(t.encode()).hexdigest()

def setTimeout(fn, s):
	Timer(s, fn).start()

def cls():
	os.system('cls' if os.name == 'nt' else 'clear')
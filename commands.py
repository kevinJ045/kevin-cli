import os
import cmd
import sys
import signal
import time
import math
import random
import utils
import cmdsdir as _cmds

interface_text = {
	'i': "\033[36m$\033[39m",
	'def': "\033[36m$\033[39m",
	'logged': "\033[36m[\033[31mSudo\033[36m]\033[36m─╼$\033[39m",
}

user = {
	'uname': 'kevin',
	'pwd': '0cc175b9c0f1b6a831c399e269772661',
	'logged_in': False
}

__dir = os.path.dirname(__file__)

boots = ['normal', 'crazy', 'half']

cpr = utils.cpr

running = False

# Helper Functions

def listenPO():
	a = input("")
	if(a == 'startup'):
		utils.cls()
		startup()
	else:
		listenPO()

def _exec(cmds, opts = {}):
	running = True
	defs = {
		'sudo': False, 
		'utils': utils,
		'login': login,
		'exec': _exec,
		'interface': interface,
		'user': user,
		'intfc': intfc
	}
	args = defs.copy()
	for i in opts:
		args[i] = opts[i]
	cmd = cmds.pop(0)
	cmds_dir = os.listdir("./cmdsdir")
	if cmd in CommandList:
		CommandList[cmd](cmds, args)
	elif cmd+'.py' in cmds_dir:
		_cmds.cmds[cmd].main(cmds, args)
		try:
			_cmds.cmds[cmd].main(cmds, args)
		except:
			print("stderr")
	else:
		cpr("Error: Command Not Found","red")
	running = False

def interface():
	return interface_text['i']

def intfc(a):
	interface_text['i'] = a

def login():
	if user['logged_in'] == True:
		return True
	uname = input("Username: ")
	pwd = input("Password: ")
	if user['uname'] == uname and user['pwd'] == utils.md5(pwd):
		logged_in()
		return True
	else:
		cpr("Error: wrong user credentials", "red")
		return login()

def unlogin():
	user['logged_in'] = False
	intfc(interface_text['def'])

def logged_in():
	user['logged_in'] = True
	intfc(interface_text['logged'])
	utils.setTimeout(unlogin, 20)

def startup():
	cpr("Starting Up...", 'aqua')
	time.sleep(2)
	print("Choose Boot:")
	print("[0] Normal Boot")
	print("[1] Crazy Boot")
	print("[2] Half Boot")
	booti = int(input("Put number: "))
	boot = boots[booti]
	cpr("Booting "+boot+" mode...")
	utils.loadBars('Starting up ')
	cpr('Logging in...', 'aqua')
	cpr('Logged in!!')
	time.sleep(3)
	utils.cls()

def stop_running():
	exit()

# Commands...

def echo(text, opt):
	print(utils.joinArgs(text))

def exit_scr(a, opt):
	exit()

def install(a, opt):
	err = "Error: installable Object required"
	if opt['sudo'] != True:
		cpr("Error: root access needed", "red")
		return
	if len(a) > 0:
		if utils.validbn(a[0]):
			name = a[0]
			print('\nInstalling '+name+' into kevin\'s brain:')
			utils.loading(delay = 0.5)
			cpr("\nInstalled "+name)
		else:
			cpr(err, 'red')
	else:
		cpr(err, 'red')

def sudo(a, opt):
	if len(a) < 1:
		return
	if a[0] and a[0] == 'sudo':
		return
	
	if login() == True:
		_exec(a, {'sudo': True})
	else:
		cpr("Error: not logged in", "red")

def shutdown(a, opt):
	if opt['sudo'] != True:
		cpr("Error: root access needed", "red")
		return
	cpr("Shutting Down...", 'aqua')
	time.sleep(5)
	utils.cls()
	listenPO()

def clear(a, opt):
	utils.cls()
		
def mem(a, opt):
	if opt['sudo'] != True:
		cpr("Error: root access needed", "red")
		return

def loadmods(a, opt):
	_cmds.loadmods()

def brak(a, opt):
	ls = []
	def vv():
		for i in ls:
			_exec(i.split(" "))
	def add():
		a = input('> ')
		if a == ")":
			vv()
			return
		ls.append(a)
		add()
	add()

def cmdman(args, opts):
	if opts['sudo'] != True:
		cpr("Error: root access needed", "red")
		return
	if len(args) > 1:
		cmd = args[0]
		name = args[1]
		if cmd == 'add':
			print('Creating command '+name)
			file = open(__dir+"/cmdsdir/"+name+".py", 'w')
			file.write("def main(args, opts):\n\tprint(\'...\')")
			file.close()
			print('Creating files and links')
			utils.loading()
			print('Updating command list')
			_cmds.loadmods()
			cpr('Command '+name+' created successfully')
		elif cmd == 'remove':
			print('Deleting command '+name)
			os.remove(__dir+"/cmdsdir/"+name+".py")
			cpr('Reoved command '+name)
		else:
			cpr("Error: invalid arg "+cmd,'red')
	else:
		cpr("Error: too little args passed",'red')


CommandList = {
	'(': brak,
	'echo': echo,
	'exit': exit_scr,
	'install': install,
	'sudo': sudo,
	'shutdown': shutdown,
	'clear': clear,
	'cmd': cmdman,
	'loadmods': loadmods
}

# Signal shit

osig = signal.getsignal(signal.SIGINT)

def exit_s(signum, frame):
	if running == True:
		stop_running()

signal.signal(signal.SIGINT, exit_s)

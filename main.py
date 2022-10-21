import commands
import utils

cpr = utils.cpr

cpr("Hello. this is the kevin terminal. how u can control kevin's mind", "white")
cpr("Note: if kevin's is not in a 4m radius ntg will work", "white")

commandsl = commands.CommandList

def ask(s):
	cmdl = input(s)
	cmds = cmdl.split(" ")
	commands._exec(cmds)
	ask(commands.interface()+" ")

ask(commands.interface()+" ")
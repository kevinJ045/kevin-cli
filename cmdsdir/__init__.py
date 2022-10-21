import os
import imp
cmds = {}
def loadmods():
	for module in os.listdir(os.path.dirname(__file__)):
		if module == '__init__.py' or module[-3:] != ".py":
			continue
		cmds[module[:-3]] = imp.load_source(module[:-3], os.path.dirname(__file__)+"/"+module)
	del module
loadmods()
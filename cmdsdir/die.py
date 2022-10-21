def main(args, opts):
    if opts['sudo'] == True:
        opts['utils'].cpr('Killing','red')
        opts['utils'].loading(10)
        opts['utils'].cpr('Killing Failed')
    else:
        opts['utils'].cpr('Error: root access needed', 'red')

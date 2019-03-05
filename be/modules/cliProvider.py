from modules.clis import terminal

clis = {
    "terminal-cli": terminal.TerminalCLI
}

def createCli(type):
	cli = clis[type]

	return cli()

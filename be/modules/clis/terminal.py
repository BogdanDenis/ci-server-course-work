import subprocess

class TerminalCLI:
	def setOutputListener(self, listener):
		self.listener = listener

	def copy(self, what, where, cwd):
		commandTemplate = 'cp -r {what} {where}'
		command = commandTemplate.format(what=what, where=where)
		try:
			retval = self.run(command, cwd)

			return retval
		except ValueError as e:
			raise e

	def workdir(self, directory, cwd):
		commandTemplate = 'cd {directory}'
		command = commandTemplate.format(directory=directory)
		try:
			retval = self.run(command, cwd)

			return retval
		except ValueError as e:
			raise e

	def run(self, command, cwd):
		p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd)
		output = ''


		for line in iter(p.stdout.readline, ''):
			strippedLine = line.rstrip().decode('utf-8')
			
			if strippedLine == '':
				break

			output += strippedLine
			
			if self.listener != None:
				self.listener(strippedLine)

		lines = p.stdout.readlines()
		returnCode = p.poll()

		if returnCode != 0 and returnCode != None:
			raise ValueError(output, returnCode)

		return output

import threading
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

class Notifier (WebSocket):
	def handleMessage(self):
		self.sendMessage(self.data)

	def handleConnected(self):
		print (self.address, 'connected')

	def handleClose(self):
		print (self.address, 'closed')

def createServer():
	return SimpleWebSocketServer('', 5679, Notifier)

def startServer():
	server = createServer()
	print (server)
	thread = threading.Thread(target=server.serveforever)
	thread.start()

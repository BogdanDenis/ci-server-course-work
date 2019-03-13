import threading
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

from modules.eventBus import EVENT_BUS as EventBus
from constants.events import EVENTS

clients = []
class Notifier(WebSocket):
	def handleMessage(self):
		for client in clients:
			if client != self:
				client.sendMessage(self.data)

	def handleConnected(self):
		clients.append(self)
		print (self.address, 'connected')

	def handleClose(self):
		clients.remove(self)
		print (self.address, 'closed')

def notifyClients(message):
	for client in clients:
		client.sendMessage(message)

def createServer():
	return SimpleWebSocketServer('', 4570, Notifier)

def startServer():
	server = createServer()
	thread = threading.Thread(target=server.serveforever)
	thread.start()

	EventBus.subscribe(EVENTS['WS_NOTIFY'], notifyClients)

	return server

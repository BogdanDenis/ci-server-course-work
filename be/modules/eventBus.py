class EventBus:
	def __init__(self):
		self.listeners = {}
	
	def subscribe(self, event, listener):
		if self.listeners.get(event) == None:
			self.listeners[event] = []

		self.listeners.get(event).append(listener)

	def publish(self, event, data):
		if self.listeners.get(event) == None:
			print ('No listeners for {event} was found!'.format(event=event))
			return

		for listener in self.listeners.get(event):
			listener(data)
	
	def unsubscribe(self, event, listener):
		if self.listeners.get(event) == None:
			print ('No listeners for {event} was found!'.format(event=event))
			return
		
		self.listeners.get(event).remove(listener)

EVENT_BUS = EventBus()
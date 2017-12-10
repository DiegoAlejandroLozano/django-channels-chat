from channels.routing import route
from chat_app import consumers

channel_routing = [
	route('websocket.connect', 		consumers.ws_add,			path=r'^/chat/$'),
	route('websocket.receive', 		consumers.ws_message,		path=r'^/chat/$'),
	route('websocket.disconnect',	consumers.ws_disconnect, 	path=r'^/chat/$'),
]
from channels import Group

def ws_add(message):
	print('Conexión recibida')
	message.reply_channel.send({'accept':True})
	Group('chat').add(message.reply_channel)

def ws_message(message):
	print('Mensaje recibido:{}'.format(message.content['text']))
	Group('chat').send({'text': message.content['text']})

def ws_disconnect(message):
	print('Conexión cerrada')
	Group('chat').discard(message.reply_channel)
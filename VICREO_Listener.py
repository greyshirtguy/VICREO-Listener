from pynput.keyboard import Key, Controller
import socket
import sys

keyboard = Controller()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10001)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

#only for testing
connectionUP = True

#logic and variables
#https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key
modifier = {
	'alt': Key.alt,
	'ctrl': Key.ctrl,
	'tab': Key.tab,
	'shift': Key.shift,
	'cmd': Key.cmd,
	'alt_gr': Key.alt_gr,
	'backspace': Key.backspace,
	'caps_lock': Key.caps_lock,
	'end': Key.end,
	'enter': Key.enter,
	'esc': Key.esc,
	'f1': Key.f1,
	'f2': Key.f2,
	'f3': Key.f3,
	'f4': Key.f4,
	'f5': Key.f5,
	'f6': Key.f6,
	'f7': Key.f7,
	'f8': Key.f8,
	'f9': Key.f9,
	'f10': Key.f10,
	'home': Key.home,
	'insert': Key.insert,
	'left': Key.left,
	'right': Key.right,
	'up': Key.up,
	'down': Key.down,
	'num_lock': Key.num_lock,
	'page_up': Key.page_up,
	'page_down': Key.page_down
	}

def pressAndRelease(key):
	keyboard.press(key)
	keyboard.release(key)

while connectionUP:
	# Wait for a connection
	print('waiting for a connection')
	connection, client_address = sock.accept()
	try:
		print('connection from', client_address)

		# Receive the data and retransmit it
		while True:
			data = connection.recv(1024)
			if data:
				tcpString = data.decode()
				print('Receiving: ', tcpString)

				# Single key command
				if tcpString[0:4] == '<SK>':
					pressAndRelease(tcpString[4])
				#combination of two keys
				elif tcpString[0:8] == '<KCOMBO>':
					#find first command
					command1 = tcpString[8:tcpString.index('<AND>')]
					if len(command1)>1:
						command1 = modifier.get(command1.lower(), 'err')
					#find second
					command2 = tcpString[tcpString.index('<AND>')+5:]
					if len(command2)>1:
						command2 = modifier.get(command2.lower(), 'err')

					#if no error send the keycombo
					if command1 != 'err' and command2 != 'err':
						print('modifier: ', command1)
						keyboard.press(command1)
						keyboard.press(command2)
						keyboard.release(command2)
						keyboard.release(command1)
					else:
						print('wrong key')

				#only key down
				elif tcpString[0:8] == '<KPRESS>':
					pressed = tcpString[8:]
					if len(pressed)>1:
						pressed = modifier.get(pressed.lower(), 'err')
					if pressed != 'err':
						keyboard.press(pressed)
					else:
						print('wrong key')

				#only key up
				elif tcpString[0:10] == '<KRELEASE>':
					released = tcpString[10:]
					if len(released)>1:
						released = modifier.get(released.lower(), 'err')
					if released != 'err':
						keyboard.release(released)
					else:
						print('wrong key')

				print('sending data back to the client')
				msg = 'done'
				connection.sendall(msg.encode())
				#only for testing
				#connectionUP = False
			else:
				print('no more data from', client_address)
				break

	finally:
		# Clean up the connection
		print('closing connection')
		connection.close()

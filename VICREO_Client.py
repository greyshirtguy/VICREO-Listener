import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 10001)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:

	# Send data
	#message = '<SK>T'
	message = '<KCOMBO>cmd<AND>tab'
	#message = '<STOP>'

	#FIRST
	print('sending "%s"' % message)
	sock.sendall(message.encode())

	data = sock.recv(160)
	print('received back: ', data.decode())

finally:
	print('closing socket')
	sock.close()

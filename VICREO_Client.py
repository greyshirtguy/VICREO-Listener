import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10001)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:

	# Send data
	#message = '<SK>N<END>'
	message = '<KPRESS>alt'
	message2 = '<KPRESS>tab'
	message3 = '<KRELEASE>tab'
	message4 = '<KRELEASE>alt'
	print('sending "%s"' % message)
	sock.sendall(message.encode())

	# Look for the response
	amount_received = 0
	amount_expected = len(message)

	while amount_received < amount_expected:
		data = sock.recv(1024)
		amount_received += len(data)
		print('received back: ', data.decode())

	print('sending "%s"' % message2)
	sock.sendall(message2.encode())

	# Look for the response
	amount_received = 0
	amount_expected = len(message2)

	while amount_received < amount_expected:
		data = sock.recv(1024)
		amount_received += len(data)
		print('received back: ', data.decode())

	print('sending "%s"' % message3)
	sock.sendall(message3.encode())

	# Look for the response
	amount_received = 0
	amount_expected = len(message3)

	while amount_received < amount_expected:
		data = sock.recv(1024)
		amount_received += len(data)
		print('received back: ', data.decode())

	print('sending "%s"' % message4)
	sock.sendall(message4.encode())

	# Look for the response
	amount_received = 0
	amount_expected = len(message4)

	while amount_received < amount_expected:
		data = sock.recv(1024)
		amount_received += len(data)
		print('received back: ', data.decode())

finally:
	print('closing socket')
	sock.close()

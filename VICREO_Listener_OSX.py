# TCP handling
import socket
import sys
# file handling
import os
#RUMPS for menu
import rumps
import time

#keyboard
from pynput.keyboard import Key, Controller
keyboard = Controller()

def resource_path(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")

		return os.path.join(base_path, relative_path)

Logo = resource_path("icon.icns")

rumps.debug_mode(False) # turn on command line logging information for development - default is off

from threading import Thread

def myRumps():
	@rumps.clicked("About")
	def about(sender):
		rumps.alert("Welcome at the VICREO Listener")

	@rumps.notifications
	def notifications(notification):  # function that reacts to incoming notification dicts
		print(notification)


	def onebitcallback(sender):  # functions don't have to be decorated to serve as callbacks for buttons
		print(4848484) # this function is specified as a callback when creating a MenuItem below

	def pressAndRelease(key):
		keyboard.press(key)
		keyboard.release(key)

	app = rumps.App("VICREO Listener", title='VICREO')
	app.menu = [
		rumps.MenuItem('About', icon=Logo, dimensions=(18, 18)),  # can specify an icon to be placed near text
		None
	]
	app.run()

def myListener():
	#https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key
	modifier = {
		'alt': Key.alt,
		'ctrl': Key.ctrl,
		'tab': Key.tab,
		'shift': Key.shift,
		'cmd': Key.cmd,
		'alt_gr': Key.alt_gr,
		'delete': Key.delete,
		'space': Key.space,
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
		'f11': Key.f11,
		'f12': Key.f12,
		'home': Key.home,
		'left': Key.left,
		'right': Key.right,
		'up': Key.up,
		'down': Key.down,
		'page_up': Key.page_up,
		'page_down': Key.page_down
		}


	_LOOP = True

	def openFile(path):
		os.startfile(path)

	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Bind the socket to the port
	server_address = ('', 10001)
	print('Listening to port 10001')
	sock.bind(server_address)
	# Listen for incoming connections
	sock.listen(1)

	#Start main function
	while _LOOP:
		# Wait for a connection
		print('waiting for a connection')
		connection, client_address = sock.accept()
		try:
			# Receive the data and retransmit it
			print('connection from', client_address)
			while _LOOP:
				data = connection.recv(160)
				if data:
					tcpString = data.decode()
					print('Receiving: ', tcpString)
					# Single key command
					if tcpString[0:4] == '<SK>':
						#somehow on mac capital letters returns: a
						sendedKey = tcpString[4]
						if sendedKey.isupper():
							keyboard.press(Key.shift)
							keyboard.press(sendedKey.lower())
							keyboard.release(sendedKey.lower())
							keyboard.release(Key.shift)
						else:
							pressAndRelease(sendedKey)
					#Special key
					elif tcpString[0:5] == '<SPK>':
						specialKey = tcpString[5:]
						specialKey = modifier.get(specialKey.lower(), 'err')
						if specialKey != 'err':
							pressAndRelease(specialKey)
						else:
							print('wrong key')
					#combination of two keys
					elif tcpString[0:8] == '<KCOMBO>':
						#find first command
						command1 = tcpString[8:tcpString.index('<AND>')]
						if len(command1)>1:
							command1 = modifier.get(command1.lower(), 'err')
						#find second
						command2 = tcpString[tcpString.index('<AND>')+5:].rstrip()
						if len(command2)>1:
							command2 = modifier.get(command2.lower(), 'err')

						#if no error send the keycombo
						if command1 != 'err' and command2 != 'err':
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

					#send message
					elif tcpString[0:5] == '<MSG>':
						try:
							keyboard.type(tcpString[5:])
						except:
							print("NOT ALLOWED")

					#open file
					elif tcpString[0:6] == '<FILE>':
						try:
							openFile(tcpString[6:])
						except:
							print("error")

					#only for testing/debug
					elif tcpString[0:6] == '<STOP>':
						msg = 'You have closed the application'
						connection.sendall(msg.encode())
						_LOOP = False

					msg = 'ok'
					connection.sendall(msg.encode())

				else:
					print('no more data from', client_address)
					break

		finally:
			# Clean up the connection
			print('finalize this transmition')
			connection.close()

	print('shutdown program')

if __name__ == "__main__":
	#Put the listener in a Thread so we can do other stuff
	t2 = Thread(target = myListener)
	t2.setDaemon(True)
	t2.start()
	#Start the GUI part
	myRumps()
	while True:
		pass

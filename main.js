/* eslint no-console: 'off' */
if (process.env.NODE_ENV !== 'production') {
	require('dotenv').config();
}
const { app, BrowserWindow, Menu, Tray } = require("electron") // app
const net = require("net") // TCP server
const robot = require('robotjs') // keyboard and mouse events
const os = require('os') // for appple script
const { exec, execFile } = require('child_process') // Shell and file actions
const path = require('path')
var iconpath = path.join(__dirname, 'img/favicon.png')
let tray = null

let server
let win
let port = 10001;
// var cmd = '{ "key":"tab", "type":"press", "modifiers":["alt"] }'
// var cmd = '{ "key":"tab", "type":"processOSX","processName":"Powerpoint" "modifier":["alt"] }'
// var cmd = '{ "type":"shell","shell":"dir" }'
// var cmd = '{ "type":"file","path":"C:/Barco/InfoT1413.pdf" }'
// var cmd = '{ "type":"string","msg":"C:/Barco/InfoT1413.pdf" }'

function createWindow() {
	// create window
	win = new BrowserWindow({
		width: 410,
		height: 600,
		resizable: false,
		icon: iconpath,
		webPreferences: {
			nodeIntegration: true
		}
	})

	win.setMenu(null)
	// load the index.html of the app
	win.loadFile('index.html')

	win.on('minimize', function (event) {
		event.preventDefault();
		win.hide();
	});

	win.on('close', function (event) {
		if (!app.isQuiting) {
			event.preventDefault();
			win.hide();
		}

		return false;
	});

	win.on('activate', function () {
		// appIcon.setHighlightMode('always')
		win.show()
	})

	win.on('closed', () => {
		// kill windows or so
		win = null
	})

	let contents = win.webContents
	console.log(contents)
	
	createListener()
}

// Catch messages from front-ed.
const { ipcMain } = require('electron')
ipcMain.on('asynchronous-message', (event, arg) => {
	console.log(arg)
	if (arg != port) {
		port = arg;
		console.log('port number changed, closing server');
		server.close();
		createListener();
		event.reply('asynchronous-reply', 'ok')
	}
})


app.whenReady().then(() => {
	tray = new Tray(path.join(__dirname, 'img/favicon.png'));
	createWindow();
	var contextMenu = Menu.buildFromTemplate([
		{
			label: 'Show App', click: function () {
				win.show()
			}
		},
		{
			label: 'Quit', click: function () {
				app.isQuiting = true;
				server.close()
				console.log('user quit')
				app.quit();
				win.destroy()
			}
		}
	])
	tray.setContextMenu(contextMenu)
})
app.on('before_quit', () => {
	isQuiting = true
	server.close()
	console.log('user quit')
})

app.on('windows-all-closed', () => {
	// On macOS it is common for applications and their menu bar
	// to stay active until the user quits explicitly with Cmd + Q
	if (os.platform() !== 'darwin') {
		app.quit()
	}
})

app.on('activate', () => {
	// On macOS it's common to re-create a window in the app when the
	// dock icon is clicked and there are no other windows open.
	if (win === null) {
		createWindow()
	}
})
if (process.platform == "darwin") {app.dock.setIcon(path.join(__dirname, 'img/logo.png'))};

function createListener() {
	// Load socket
	console.log('waiting for connection...')
	portInUse(port, function (returnValue) {
		console.log('Port already active?', returnValue);
	});
}

var portInUse = function (port, callback) {
	console.log('port', port)
	server = net.createServer((socket) => {
		socket.write('Listener active\r\n');
		socket.pipe(socket);
		console.log("connected")
		socket.on('end', () => {
			console.log('client ended connection, waiting for connection...')
		})
		socket.on('connect', () => {
			console.log("connected")
		})
		socket.on('data', (data) => {
			try {
				processIncomingData(JSON.parse(data))
			} catch (e) {
				console.log("error parsing JSON, trying old way")
				try {
					processIncomingData2(data)
				} catch (e) {
					console.error(e)
				}
			}
		})
		server.on('error', function (e) {
			callback(true);
		});
		server.on('listening', function (e) {
			server.close();
			callback(false);
		});
	});
	server.listen(port, '0.0.0.0');

};

function processIncomingData(data) {
	console.log(data)
	switch (data.type) {
		case 'press':
			robot.keyTap(data.key, data.modifiers)
			break;

		case 'down':
			robot.keyToggle(data.key, 'down', data.modifiers)
			break;

		case 'up':
			robot.keyToggle(data.key, 'up', data.modifiers)
			break;

		case 'processOSX':
			if (os.type() === 'Darwin') {
				if (data.modifiers[0]) {
					return exec(`Script="tell app \\"${processName}\\" to keystroke ${data.key} using ${data.modifiers[0]} down" osascript -e "$Script"`)
				} else {
					return exec(`Script="tell app \\"${processName}\\" to keystroke ${data.key}" osascript -e "$Script"`)
				}
			}
			break;

		case 'shell':
			exec(data.shell, (error, stdout, stderr) => {
				if (error) {
					console.log(`error: ${error.message}`);
					return;
				}
				if (stderr) {
					console.log(`stderr: ${stderr}`);
					return;
				}
				console.log(`stdout: ${stdout}`);
			})
			break;

		case 'string':
			robot.typeString(data.msg);
			break;

		case 'file':
			exec(data.path).unref()
			break;
	}


}
function processIncomingData2(data) {
	let incomingString = data.toString('utf8')
	console.log(incomingString)
	let key1, key2, key3
	let type = incomingString.slice(1, incomingString.search('>'))

	switch (type) {
		case 'SK':
			key1 = incomingString.slice(incomingString.search('>') + 1)
			key1 == 'cmd' ? key1 = 'command' : key1 = key1
			hitHotkey(key1)
			break;
		case 'SPK':
			key1 = incomingString.slice(incomingString.search('>') + 1)
			key1 == 'cmd' ? key1 = 'command' : key1 = key1
			hitHotkey(key1)
			break;
		case 'KCOMBO':
			key1 = incomingString.slice(8, incomingString.search('<AND>'))
			key2 = incomingString.slice(incomingString.search('<AND>') + 5)
			key1 == 'cmd' ? key1 = 'command' : key1 = key1
			key2 == 'cmd' ? key2 = 'command' : key2 = key2
			hitHotkey(key2, key1)
			break;
		case 'KTRIO':
			key1 = incomingString.slice(7, incomingString.search('<AND>'))
			key2 = incomingString.slice(incomingString.search('<AND>') + 5, incomingString.search('<AND2>'))
			key3 = incomingString.slice(incomingString.search('<AND2>') + 6)
			key1 == 'cmd' ? key1 = 'command' : key1 = key1
			key2 == 'cmd' ? key2 = 'command' : key2 = key2
			key3 == 'cmd' ? key3 = 'command' : key3 = key3
			hitHotkey(key3, [key1, key2])
			break;
		case 'KPRESS':
			key1 = incomingString.slice(8, incomingString.search('<AND>'))
			key2 = incomingString.slice(incomingString.search('<AND>') + 5)
			key1 == 'cmd' ? key1 = 'command' : key1 = key1
			key2 == 'cmd' ? key2 = 'command' : key2 = key2
			robot.keyToggle(checkKey(key2), 'down', checkKey(key1))
			break;
		case 'KRELEASE':
			key1 = incomingString.slice(8, incomingString.search('<AND>'))
			key2 = incomingString.slice(incomingString.search('<AND>') + 5)
			robot.keyToggle(checkKey(key2), 'up', checkKey(key1))
			break;
		case 'MSG':
			robot.typeString(incomingString.slice(incomingString.search('>') + 1))
			break;
	}
}
function checkKey(key) {
	switch (key){
		case 'cmd':
			return 'command';
		case 'esc':
			return 'escape';
		}
}

function checkKeys(modifier) {
	if (Array.isArray(modifier)) {
		for (mod of modifier) {
			switch (key){
				case 'cmd':
					return 'command';
				case 'esc':
					return 'escape';
				}
		}
	} else {
		checkKey(modifier)
	}
}

function hitHotkey(key, modifier) {
	key = checkKey(key);
	modifier = checkKeys(modifier);

	if (os.platform() === 'darwin') {
		if (modifier) {
			return exec(`Script="tell app \\"System Events\\" to keystroke ${key} using ${modifier} down" osascript -e "$Script"`)
		} else {
			return exec(`Script="tell app \\"System Events\\" to keystroke ${key}" osascript -e "$Script"`)
		}
	} else {
		if (modifier) {
			return robot.keyTap(key, modifier)
		} else {
			return robot.keyTap(key)
		}
	}
}

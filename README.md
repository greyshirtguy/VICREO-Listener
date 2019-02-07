# VICREO Listener
<img src="https://img.shields.io/badge/made%20with-python-blue.svg" alt="made with python">
<img src="https://img.shields.io/github/size/JeffreyDavidsz/VICREO-Listener/VICREO_Listener.py.svg?style=flat" alt="script size">

*Hotkey listener for windows & Mac*

Go to [VICREO releases](https://github.com/JeffreyDavidsz/VICREO-Listener/releases) for download.

>  VICREO Listener is a small program that sits on your machine waiting for incomming TCP connection/commands. It uses pre-defined commands to simulate keypresses on your machine. You can use this program to preform hotkey actions from remote

<img src="https://bitfocus.io/companion/badge.png?ref=vicreo" alt="Controllable by Companion">

## Installation

Download the right software package for your operating system and launch the program on the machine you would like to control (host).

On your client machine (the one you are sending commands from), send TCP string to the right IP-address from the host, to port 10001

## Usage

Below you'll find a table of pre-installed commands that the listener will accept. Firt tell the program what kind of key you are going to send and than the key itself.

| Action					| Description									| Example								|
| --------------- | --------------------------- |-----------------------|
| &lt;SK&gt;						| Single key									|&lt;SK&gt;n  								|
| &lt;KCOMBO&gt;	&lt;AND&gt;	| Key combination							|&lt;KCOMBO&gt;alt&lt;AND&gt;tab  	|
| &lt;KPRESS&gt;				| Simulates key down					|&lt;KPRESS&gt;n					  	|
| &lt;KRELEASE&gt;			| Simulates key up						|&lt;KRELEASE&gt;n				  	|
| &lt;MSG&gt;						| Send message								|&lt;MSG&gt;Hello World (only string message)		|
| &lt;FILE&gt;					| Open file (complete path)		|&lt;FILE&gt;c:\user\test\test.bat

The &lt;KPRESS&gt; and &lt;KRELEASE&gt; can be used for special cases, Example;<br>
&lt;KPRESS&gt;ctrl<br>
&lt;KPRESS&gt;c<br>
&lt;KRELEASE&gt;c<br>
&lt;KRELEASE&gt;ctrl<br>

but above is the same as &lt;KCOMBO&gt;ctrl&lt;AND&gt;c

> Be aware there is a limit of 160 bytes to receive, this because of the &lt;MSG&gt; function

> Make sure you use the backslash in the file open command

## Modifiers ##

>The following modifier are supported:

alt
ctrl
tab
shift
cmd
alt_gr
delete
backspace
space
caps_lock
end
enter
esc
f1
f2
f3
f4
f5
f6
f7
f8
f9
f10
f11
f12
home
insert
left
right
up
down
num_lock
page_up
page_down

## Build your own?

pyinstaller -y -F -w -i "PATH/icon.ico" --add-data "PATH/icon.ico";"." --hidden-import infi.systray --hidden-import pkg_resources --hidden-import plyer.platforms.win.notification "PATH/VICREO_Listener.py"

----

For additional actions, please raise a feature request on [GitHub](https://github.com/JeffreyDavidsz/VICREO-Listener/issues).

# VICREO Listener
<img src="https://img.shields.io/badge/made%20with-python-blue.svg" alt="made with python">
<img src="https://img.shields.io/github/repo-size/jeffreydavidsz/VICREO-Listener.svg?style=flat" alt="repo size">
<img src="https://img.shields.io/github/release/jeffreydavidsz/vicreo-listener.svg?style=flat" alt="current release">

*Hotkey listener for windows & Mac*

Latest [Windows release](https://github.com/JeffreyDavidsz/VICREO-Listener/releases/download/v1.3.0/VICREO_Listener_Windows.exe)
Latest [OSX release](https://github.com/JeffreyDavidsz/VICREO-Listener/releases/download/v1.3.0/VICREO_Listener_OSX.zip)

Go to [VICREO releases](https://github.com/JeffreyDavidsz/VICREO-Listener/releases) for download.

>  VICREO Listener is a small program that sits on your machine waiting for incomming TCP connection/commands. It uses pre-defined commands to simulate keypresses on your machine. You can use this program to preform hotkey actions from remote

[<img src="https://bitfocus.io/companion/badge.png?ref=vicreo" width="200px" alt="Controllable by Companion">](https://bitfocus.io/companion/)

## Installation

Download the right software package for your operating system and launch the program on the machine you would like to control (host).

On your client machine (the one you are sending commands from), send TCP string to the right IP-address from the host, to port 10001

## Usage

Below you'll find a table of pre-installed commands that the listener will accept. Firt tell the program what kind of key you are going to send and than the key itself.

| Action					| Description									| Example								|
| --------------- | --------------------------- |-----------------------|
| &lt;SK&gt;						| Single key									|&lt;SK&gt;n  								|
| &lt;KCOMBO&gt;	&lt;AND&gt;	| Key combination							|&lt;KCOMBO&gt;alt&lt;AND&gt;tab  	|
| &lt;KTRIO&gt;	&lt;AND&gt;	&lt;AND2&gt;	| Key trio combination							|&lt;KCOMBO&gt;ctrl&lt;AND&gt;shift&lt;AND2&gt;d  	|
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
insert (only windows)
left
right
up
down
num_lock (only windows)
page_up
page_down

## FAQ ##

For mac, when you need the path of a file, right-click on the file and when you see the menu, press and hold Alt to be able to copy the full path.

----

For additional actions, please raise a feature request on [GitHub](https://github.com/JeffreyDavidsz/VICREO-Listener/issues).

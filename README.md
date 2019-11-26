# VICREO Listener
<img src="https://img.shields.io/badge/made%20with-python-blue.svg" alt="made with python">
<img src="https://img.shields.io/github/repo-size/jeffreydavidsz/VICREO-Listener.svg?style=flat" alt="repo size">
<img src="https://img.shields.io/github/release/jeffreydavidsz/vicreo-listener.svg?style=flat" alt="current release">

*Hotkey listener for windows & Mac*

Latest [Windows release](https://github.com/JeffreyDavidsz/VICREO-Listener/releases/download/v1.3.1/VICREO_Listener_Windows.exe)
Latest [OSX release](https://github.com/JeffreyDavidsz/VICREO-Listener/releases/download/v1.3.1/VICREO_Listener_OSX.zip)

Go to [VICREO releases](https://github.com/JeffreyDavidsz/VICREO-Listener/releases) for download.

>  VICREO Listener is a small program that sits on your machine waiting for incomming TCP connection/commands. It uses pre-defined commands to simulate keypresses on your machine. You can use this program to preform hotkey actions from remote

[<img src="https://bitfocus.io/companion/badge.png?ref=vicreo" width="200px" alt="Controllable by Companion">](https://bitfocus.io/companion/)

## Installation

Download the right software package for your operating system and launch the program on the machine you would like to control (host).

On your client machine (the one you are sending commands from), send TCP string to the right IP-address from the host, to port 10001

## Usage

Below you'll find a table of pre-installed commands that the listener will accept. First tell the program what kind of key you are going to send and than the key itself.

| Action					| Description									| Example								|
| --------------- | --------------------------- |-----------------------|
| &lt;SK&gt;						| Single key								|&lt;SK&gt;n  								|
| &lt;SPK&gt;						| Special key (modifier)		|&lt;SKP&gt;enter 								|
| &lt;KCOMBO&gt;	&lt;AND&gt;	| Key combination							|&lt;KCOMBO&gt;alt&lt;AND&gt;tab  	|
| &lt;KTRIO&gt;	&lt;AND&gt;	&lt;AND2&gt;	| Key trio combination							|&lt;KCOMBO&gt;ctrl&lt;AND&gt;shift&lt;AND2&gt;d  	|
| &lt;KPRESS&gt;				| Simulates key down					|&lt;KPRESS&gt;n					  	|
| &lt;KRELEASE&gt;			| Simulates key up						|&lt;KRELEASE&gt;n				  	|
| &lt;MSG&gt;						| Send message								|&lt;MSG&gt;Hello World (only string message)		|
| &lt;FILE&gt;					| Open file (complete path)		|&lt;FILE&gt;c:\user\test\test.bat
| &lt;SKE&gt;	&lt;PROCESS&gt; &lt;AND&gt;	&lt;AND2&gt;	| (MacOS ONLY) - Send KeyPress Event to Process with optional modifiers	|&lt;SKE&gt;0x12&lt;PROCESS&gt;propresenter&lt;AND&gt;cmd&lt;AND2&gt;none

The &lt;KPRESS&gt; and &lt;KRELEASE&gt; can be used for special cases, Example;<br>
&lt;KPRESS&gt;ctrl<br>
&lt;KPRESS&gt;c<br>
&lt;KRELEASE&gt;c<br>
&lt;KRELEASE&gt;ctrl<br>

but above is the same as &lt;KCOMBO&gt;ctrl&lt;AND&gt;c

## &lt;SKE&gt; (MacOS Only) - Notes ##
The **&lt;SKE&gt;*keyCode*&lt;PROCESS&gt;*processSearchString*&lt;AND&gt;*optionalModifierKey1*&lt;AND2&gt;*optionalModifierKey2*** command (MacOS only) will send a keyboard keypress event directly to a specific process found by searching for any process matching \*processSearchString\* with up to two optional modifiers: none|alt|ctrl|cmd|shift.
You can find an applications process name by checking the list in the CPU pane of MacOS Activity Monitor. 

Please note that this works through a very different mechanism than the other commands in VICREO-Listener and it is **MacOS only.** You won't often need this command - as the other commands to type Keys are likely to do what you need.  However, this command can help if you need to send keystrokes to an application running in the background.

Please also note that you will need to add the VICREO Listener application to the list of "Allow the app below to control your computer" in the Privacy section of Security & Privacy MacOS system settings.

This command is virtually sending physical keyboard events with the keys identified by a KeyCode. You must send the keyboard keycode - not the character/letter being typed.

For example, if you send keycode 0x00 and your computer is setup to use a US keyboard as your current input, that will be like pressing the key with the letter **A** on it. If however, your keyboard is Greek, then sending KeyCode 0x00 will be like typing the letter **α**. Think of it as pressing a physical key in a specific location on a keyboard.  You can lookup MacOS keyboard keycodes online or refer to the map of the US keyboard below:
![KeyCodes](Apple%20Keyboard%20KeyCodes.jpg)
The US language keyboad map above shows the hex keycodes in green (*you can also send the decimal equivalent if you prefer*).
Generally, keyboards for other languages will have the **same KeyCodes for physical keys in the same locations on a keyboard** - they just have different letters printed on them.  This means you can "overlay" any other language keyboard on the US keyboard to find the right keycode you want for other languages.  

Also, note that the events are directed at the running process itself (Not the foreground application, Window or Text Control). This means it is possible to send these keyboard events to applications running in the background on MacOS.  However, depending on how the application is processing keyboard input, **this only works in very limited cases.** 
It will most likely work for application-wide hotkeys. See how your application responds - your mileage may vary.

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

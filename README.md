# VICREO Listener

*Hotkey listener for windows & Mac*

Go to [VICREO](http://vicreo.eu/listener/) for download.

>  VICREO Listener is a small program that sits on your machine waiting for incomming TCP connection/commands. It uses pre-defined commands to simulate keypresses on your machine. You can use this program to preform hotkey actions from remote

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
| &lt;MSG&gt;						| Send message								|&lt;MSG&gt;Hello World (only strig message)		|

The &lt;KPRESS&gt; and &lt;KRELEASE&gt; can be used for special cases, Example
&lt;KPRESS&gt;ctrl
&lt;KPRESS&gt;c
&lt;KRELEASE&gt;c
&lt;KRELEASE&gt;ctrl

but above is the same as &lt;KCOMBO&gt;ctrl&lt;AND&gt;c

> Be aware there is a limit of 160 bytes to receive, this because of the &lt;MSG&gt; function

## Error Codes

| Error Code | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| 400        | Bad Request -- Your request was invalid.                     |
| 405        | Method Not Allowed -- You tried to access an endpoint with an invalid method. |
| 500        | Internal Server Error -- We had a problem with our server. Try again later. |
| 503        | Service Unavailable -- We're temporarily offline for maintenance. Please try again later. |

## Modifiers ##

>The following modifier are supported:

alt
ctrl
tab,
shift
cmd
alt_gr
backspace
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
home
insert
left
right
up
down
num_lock
page_up
page_down

----

For additional actions, please raise a feature request on [GitHub](https://github.com/jeffreydavidsz/VICREO-Listener/).

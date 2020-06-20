# VICREO Listener

*Hotkey listener for windows, Mac and Linux*

Linux release will be available shortly.

Go to [VICREO releases](https://github.com/JeffreyDavidsz/VICREO-listener/releases) for download.

>  VICREO Listener is a small program that sits on your machine waiting for incoming TCP connection/commands. It uses pre-defined commands to simulate key-presses on your machine. You can use this program to preform hotkey actions from remote

[<img src="https://bitfocus.io/companion/badge.png?ref=vicreo" width="200px" alt="Controllable by Companion"/>](https://bitfocus.io/companion/)
[<img src="https://d1iczxrky3cnb2.cloudfront.net/button-small-blue.png"/>](https://donorbox.org/vicreo-listener?default_interval=o&amount=25)

## Installation

Download the right software package for your operating system and launch the program on the machine you would like to control (host).

On your client machine (the one you are sending commands from), send TCP string to the right IP-address from the host, to port 10001 (or change the port to something you like)

## Usage

You'll send an object to the listener. The application first looks a key called `type`.

The following types are available;
* press (simulate a keypress)
* file (open a file)
* shell (perform a shell command)
* down (simulate a key down)
* up (simulate a key up)
* processOSX (send keys to a process on mac via AppleScript)

### Example key press
For keypresses create a object like this;
<pre><code>{ "key":"tab", "type":"press", "modifiers":["alt"] }</code></pre>

> Put the modifiers in an array.
> Alt/option, command(win), Ctrl and Shift are supported.

### Example open file
Open a file on the local system;
<pre><code>{ "type":"file","path":"C:/Barco/InfoT1413.pdf" }</code></pre>

### Example shell
To perform a shell command on the system;
<pre><code>{ "type":"shell","shell":"dir" }</code></pre>

### Example processOSX
<pre><code>{ "key":"tab", "type":"processOSX","processName":"Microsoft PowerPoint" "modifier":["alt"] }</code></pre>

## Keys ##

>The following keys are supported:

| Key								|Description															| Notes								|
|-------------------|-----------------------------------------|---------------------|
| backspace					|																					|											|
| delete						|																					|											|
| enter							|																					|											|
| tab								|																					|											|
| escape						|																					|											|
| up								| Up arrow key														|											|
| down							| Down arrow key													|											|
| right							| Right arrow key													|											|
| left							| Left arrow key													|											|
| home							|																					|											|
| end								|																					|											|
| pageup						|																					|											|
| pagedown					|																					|											|
| f1								|																					|											|
| f2								|																					|											|
| f3								|																					|											|
| f4								|																					|											|
| f5								|																					|											|
| f6								|																					|											|
| f7								|																					|											|
| f8								|																					|											|
| f9								|																					|											|
| f10								|																					|											|
| f11								|																					|											|
| f12								|																					|											|
| command						|																					|											|
| alt								|																					|											|
| control						|																					|											|
| shift							|																					|											|
| right_shift				|																					|											|
| space							|																					|											|
| printscreen				|																					| No Mac support			|
| insert						|																					| No Mac support			|
| audio_mute				| Mute the volume													|											|
| audio_vol_down		| Lower the volume												|											|
| audio_vol_up			| Increase the volume											|											|
| audio_play				| Play																		|											|
| audio_stop				| Stop																		|											|
| audio_pause				| Pause																		|											|
| audio_prev				| Previous Track													|											|
| audio_next				| Next Track															|											|
| audio_rewind	 		|																					| Linux only					|
| audio_forward	 		|																					| Linux only					|
| audio_repeat	 		|																					| Linux only					|
| audio_random	 		|																					| Linux only					|
| numpad_0					|																					| No Linux support		|
| numpad_1					|																					| No Linux support		|
| numpad_2					|																					| No Linux support		|
| numpad_3					|																					| No Linux support		|
| numpad_4				 	|																					| No Linux support		|
| numpad_5					|																					| No Linux support		|
| numpad_6					|																					| No Linux support		|
| numpad_7					|																					| No Linux support		|
| numpad_8					|																					| No Linux support		|
| numpad_9					|																					| No Linux support		|
| lights_mon_up			| Turn up monitor brightness							| No Windows support	|
| lights_mon_down		| Turn down monitor brightness						| No Windows support	|
| lights_kbd_toggle | Toggle keyboard backlight on/off				| No Windows support	|
| lights_kbd_up			| Turn up keyboard backlight brightness		| No Windows support	|
| lights_kbd_down		| Turn down keyboard backlight brightness	| No Windows support	|

## FAQ ##

For mac, when you need the path of a file, right-click on the file and when you see the menu, press and hold Alt to be able to copy the full path.
Fill complete filepath without parentheses

----

For additional actions, please raise a feature request on [GitHub](https://github.com/JeffreyDavidsz/VICREO-listener/issues).

## NOTES ON BUILDING ##
For OSX Building you need a valid Developer certificate, which you can only get from signing up for Apple's developer program.
Install Developer ID Application certificate in your keychain, by creating a new certificate and downloading/open it in keychain
run <pre><code>security find-identity -vp codesigning </pre></code> to check if the certificate can be found by electron.
Change the identity in <pre><code>forge.config.js</pre></code> to your own certificate.
For CI Build do a <pre><code>base64 -i name.p12 -o output.txt</pre></code>
To check if the build is signed correctly do this;
<pre><code>spctl -a -vv '/Users/user/projects/VICREO-Listener/out/make/zip/darwin/x64/VICREO-Listener.app'</pre></code>
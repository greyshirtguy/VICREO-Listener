# VICREO Listener

*Hotkey listener for windows & Mac*

Go to [VICREO](http://vicreo.eu/listener/) for download.

>  VICREO Listener is a small program that sits on your machine waiting for incomming TCP connection/commands. It uses pre-defined commands to simulate keypresses on your machine. You can use this program to preform hotkey actions from remote

## Installation

Download the right software package for your operating system and launch the program on the machine you would like to control (host).

On your client machine (the one you are sending commands from), send TCP string to the right IP-address from the host, to port 10001

## Usage

Below you'll find a table of pre-installed commands that the listener will accept. Firt tell the program what kind of key you are going to send and than the key itself.

| Action					| Description									| Example			|
| --------------- | --------------------------- |-------------|
| <SK>						| Single key									|; <SK>n  		|


## Error Codes

The following table is from the PVP API documentation:

| Error Code | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| 400        | Bad Request -- Your request was invalid.                     |
| 405        | Method Not Allowed -- You tried to access an endpoint with an invalid method. |
| 500        | Internal Server Error -- We had a problem with our server. Try again later. |
| 503        | Service Unavailable -- We're temporarily offline for maintenance. Please try again later. |



----

For additional actions, please raise a feature request on [GitHub](https://github.com/jeffreydavidsz/VICREO-Listener/).

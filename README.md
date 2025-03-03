# Widevine-DRM-Browser-Player
Play Widevine &amp; Clearkey DRM Streams In Your Web Browser <br>
This is for educational purposes only - Do not play streams you do not have to right to play. You need to provide any decrypt keys or license URLs for this to work. This application does not extract/generate or provide any such keys
<br>

## Options And Limitations
If you just want to test locally load drm_player.html straight into Firefox web browser (it will not work in Chrome) <br>
But if you want to host the html file and play in any web browser including Chrome, you will need to use the proxy server. I've included a host server and proxy server as examples

## How To Load local drm_player.htm
Open drm_player.html in your web browser <br>
<br>
Technically if you wanted to watch it on your tv you could if you had a web browser on the tv that supports widevine/clearkey although see the limitation above. It maybe better running the server version <br>
<br>
Enter mpd url <br>
Enter license url or decryption key <br>

## How To Setup And Load If Running On A Server
Clone this repo ```git clone https://github.com/purplescorpion1/Widevine-DRM-Browser-Player```  <br>
<br>
Requires python eg Windows install from ```https://www.python.org/downloads/windows/``` <br>
Requires the following python modules to be installed <br>
```pip install flask requests mitmproxy``` <br>
<br>
Download and install OpenSSL Binaries <br>
Windows https://slproweb.com/products/Win32OpenSSL.html <br>
Linux/Mac sudo ```apt install openssl``` / ```brew install openssl``` <br>
<br>
Create SSL keys <br>
In Widevine-DRM-Browser-Player directory open cmd/terminal window replacing IP at the end of the command with the IP the flask server will be running on <br>
```openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=IP"``` <br>
<br>
Open ```Widevine-DRM-Browser-Player/static/drm_proxy_player.html``` in a coding text editor eg notpad++ <br>
Change the IPs in the following sections to the IP address of the machine running the script <br>
 ```await fetch('https://192.168.1.123:5098/set_proxy_config', {``` <br>
```const proxyMpdUrl = `https://192.168.1.123:5098/proxy?url=${encodeURIComponent(mpdUrl)}`;``` <br>
<br> 
Open ```Widevine-DRM-Browser-Player/drm_player_server.py``` in a coding text editor eg notpad++ <br>
Change the IP in the following line to the IP address of the machine running the script <br>
```app.run(host='192.168.1.123', port=5098, debug=True, ssl_context=('cert.pem', 'key.pem'))``` <br>
<br>
Open ```Widevine-DRM-Browser-Player/drm_player_mitmproxy.py``` in a coding text editor eg notpad++ <br>
Change the IP in the following line to the IP address of the machine running the script <br>
```
if flow.request.url.startswith("http://192.168.1.123:8080/"):
            flow.request.url = flow.request.url.replace("http://192.168.1.123:8080/", "")
``` 

python if on windows 11 <br>
python3 if on linux <br>
<br>
Run the following commands in separate cmd/terminal windows replacing the IP address in the mitmproxy command with the IP of the machine running the script <br>
```python drm_player_server.py``` <br>
```mitmdump -s drm_player_mitmproxy.py -p 8080 --listen-host 192.168.1.123``` <br>
<br>
Now in your web browser go to changing the IP address to the IP address of the machine running the server. Important to enter the https:// at the start! <br>
https://192.168.1.123 <br>
<br>
Note you will get a warning about unsafe/unsigned site due to your self signed SSL. To avoid this you will need a SSL certificate from a recognised provider. Just tell your browser you want to proceed to the site <br>
<br>
Enter mpd url <br>
Enter license url or decryption key <br>
Enter the referer <br>
Enter the origin <br>

## How To Play
To play the stream press play once all stream details have been entered <br>

## How To Save Stream Details
If you have a current streamurls.json load it first (see How To Load Stream Details) <br>
To save the stream url and keys to load later press save <br>
It will ask you to enter a name for the stream <br>
It will then download streamurls.json containing stream urls and keys <br>
If streamurls.json already exists it will amend it to eg streamurls(1).json <br>
Delete old file and rename new one streamurls.json <br>

## How To Load Stream Details
Press Browse then select your streamurls.json <br>
Select a saved stream from the drop down window <br>

## How To Delete A Stream
You can temporarily remove a stream from the list by selecting the delete stream button <br>
To permanently remove you need to delete it from the streamurls.json file <br>

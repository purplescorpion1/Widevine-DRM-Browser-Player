# Widevine-DRM-Browser-Player
Play Widevine &amp; Clearkey DRM streams In Your Web Browser <br>
This is for educational purposes only - Do not play streams you do not have to right to play. You need to provide any decrypt keys or license URLS for this to work. This application does not extract/generate or provide any such keys
<br>
## Limitations
1. You need to load the html file directly into your web browser. It will not work hosted on a server for example
2. It will not work in Chrome and I've only tested in Firefox

## How To Load
Open drm_player.html in your web browser <br>
<br>
Technically if you wanted to watch it on your tv you could if you had a web browser on the tv that supports widevine/clearkey although see the limitation above <br>
<br>
Enter mpd url <br>
Enter license url or decryption key <br>

## How To Play
To play the stream press play <br>

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

# Chall 10

https://geosint.umbccd.net/Hard-chall10

## Solution

The chances that you are able to identify this random road is close to zero. Which is why you should dig deeper.

Checking out the source code for this challenge, you can find that there is a `chall.js` file. Opening the chall.js file, we can see that a request is being made. 

```js
// GET info.json
var xhr = new XMLHttpRequest();
xhr.open("GET", '/info.json', false); // false for synchronous request
xhr.send( null );
```

This prompts us to dig deeper by going to `https://geosint.umbccd.net/info.json`. Upon opening `info.json`, we see that for chall 10, the `panoID` is exposed. 

```json
"Hard": {
"chall10": {"img": "tile_6_1_3.jpeg", "height": 6, "width": 13, "heading": 0, "panoID": "RmsBpaDYvpL-TafIFO4FbA"}
}
```

The PanoID allows for the location of a street view image to be accessed. Since we have the panoID, we can go to `https://www.google.com/maps/@?api=1&map_action=pano&pano=RmsBpaDYvpL-TafIFO4FbA`, which will give us the exact location. In this case, the location is the `Ghanzi District`, specifically at coordinates `-22.6601671, 21.9258122`

![flag](https://github.com/aqxq/CTF-Writeups/blob/main/DawgCTF/OSINT/GEOSINT/Chall%2010/chall10.png)

FLAG: `DawgCTF{ifyoudidthiswithoutapanoID--goodforyou}`

## Chall 2

https://geosint.umbccd.net/Easy-chall2

## Solution
Doing multiple Google reverse image searches allows for the country to be narrowed down to `Malta`. However, none of these reverse image searchs give me a specific location, which makes me resort to guess and check. I see that there is a store.

![store](https://github.com/aqxq/CTF-Writeups/blob/main/DawgCTF/OSINT/GEOSINT/Chall%202/store.png)

At first, I think that the name of the store starts with "Rose", so I look for stores in Malta that start with "Rose", but none of them match up with the street view in the Geosint.

So, I ask my good friend ChatGPT, and it says that the first word is "Royal."

![royal](https://github.com/aqxq/CTF-Writeups/blob/main/DawgCTF/OSINT/GEOSINT/Chall%202/royal.png)

Doing a quick Google Maps search reveals that a store in Malta that starts with "royal" is Royal Pet Store. Guessing Royal Pet Store, however, results in `within 1000`. 

So I start guessing.

![chall2](https://github.com/aqxq/CTF-Writeups/blob/main/DawgCTF/OSINT/GEOSINT/Chall%202/chall2.png)


FLAG: `DawgCTF{HaveUTriedCatFood?ihave!}`

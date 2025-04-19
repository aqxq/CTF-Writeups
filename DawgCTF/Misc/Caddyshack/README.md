## Caddyshack

locate and connect to the server running on caddyshack.umbccd.net

## Solution

I first attempted to ping the server, but the server did not respond to ICMP requests. 

![ping](https://github.com/aqxq/CTF-Writeups/blob/main/DawgCTF/Misc/Caddyshack/ping.png)

Since ping didn't work, the next step was to perform a port scan using nmap to find open services.

![nmap](https://github.com/aqxq/CTF-Writeups/blob/main/DawgCTF/Misc/Caddyshack/nmap.png)

The scan revealed port 70 open, which is running the Gopher protocol. Since port 70 is open and running Gopher, we used netcat (nc) to connect to the server and interact with the Gopher service. 

Upon connecting, by entering `/`, we were greeted with some server details, including the Gopher protocol description and information about the server. The server presented a directory listing, which included a file named Flag.txt:

![gopher](https://github.com/aqxq/CTF-Writeups/blob/main/DawgCTF/Misc/Caddyshack/gopher.png)

To retrieve the flag, I used netcat to connect to the server again and typed `/Flag.txt`, which gave me the flag. 

![flag](https://github.com/aqxq/CTF-Writeups/blob/main/DawgCTF/Misc/Caddyshack/gopherflag.png)

FLAG: `DawgCTF{60ph3r_15_n07_d34d!}`

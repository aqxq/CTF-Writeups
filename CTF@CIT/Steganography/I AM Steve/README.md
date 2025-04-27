## I AM Steve
You were supposed to be a hero, Brian!

SHA256: 01b3dbe5d8801adf27a9bb779d85ef4c8881905544642fbdbdd41e54e4d0ae5e
## Solution
Since this is a steg chall, I start by running steghide and binwalk, but I get no results. Then, I run zsteg on it:
```c
dev@dev:~$ zsteg cj.png
b1,r,lsb,xy         .. text: "v6RNA]bgD"
b1,rgb,lsb,xy       .. text: "VEhJU19pc19hX2NyYWZ0aW5nX3RhYmxl"
b2,b,msb,xy         .. text: "UUUUTU@UU"
b2,rgb,msb,xy       .. file: OpenPGP Public Key
b2,rgba,lsb,xy      .. text: ["#" repeated 8 times]
b2,abgr,msb,xy      .. text: ["S" repeated 8 times]
b3,g,msb,xy         .. file: OpenPGP Secret Key
b4,r,lsb,xy         .. text: "DB\"\"\"\"\"\""
b4,r,msb,xy         .. text: "\"BDDDDDD"
b4,g,lsb,xy         .. text: "\"\"DD\"\"\"\""
b4,g,msb,xy         .. text: "DD\"\"DDDD"
b4,b,lsb,xy         .. text: "DDDDDDDDDF"
b4,b,msb,xy         .. text: "@\"\"\"\"\"\"\"\"\"bU53s3333fffff\"\"\"DDD$\"BDD\"\"\"\"\"\"\"\"DDDD"
```

I recognize the 2nd string (`VEhJU19pc19hX2NyYWZ0aW5nX3RhYmxl`) as base64. Decoding it gives `THIS_is_a_crafting_table`. Putting it inside CIT{} gives you the flag.



FLAG: `CIT{THIS_is_a_crafting_table}`
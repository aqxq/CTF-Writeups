## Blank Image
I was gonna make a really cool challenge but then I literally forgot about it so all I have is this blank image. Good luck!

## Solution
Since this is a steg chall, I start by running steghide and binwalk, but I get no results. Then, I run zsteg on it, which helped me find the flag.
```c
dev@dev:~$ zsteg image.png
b1,b,lsb,xy         .. file: OpenPGP Public Key
b1,a,lsb,xy         .. text: "CIT{n1F0Rsm0Er40}"
b1,bgr,msb,xy       .. file: PGP Secret Sub-key -
b2,abgr,lsb,xy      .. text: "-6k^6\n<^G"
b3,rgb,msb,xy       .. text: "x&f{KH:7"
b3,bgr,lsb,xy       .. text: "AJ~HJ2oS"
b4,a,lsb,xy         .. file: TeX font metric data (\001)
b4,rgba,lsb,xy      .. text: "@2AXqmPv1"
```



FLAG: `CIT{n1F0Rsm0Er40}`
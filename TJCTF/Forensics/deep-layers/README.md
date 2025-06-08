## deep-layers
Not everything ends where it seems to...

## Solution

I began by viewing the metadata of chall.png using `exiftool`:
```c
dev@penguin:~$ exiftool chall.png
ExifTool Version Number         : 12.57
File Name                       : chall.png
Directory                       : .
File Size                       : 370 bytes
File Modification Date/Time     : 2025:06:08 11:41:35-04:00
File Access Date/Time           : 2025:06:08 11:41:56-04:00
File Inode Change Date/Time     : 2025:06:08 11:41:49-04:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1
Image Height                    : 1
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Password                        : cDBseWdsMHRwM3NzdzByZA==
Warning                         : [minor] Trailer data after PNG IEND chunk
Image Size                      : 1x1
Megapixels                      : 0.000001
```
There is a password entry, which seems to be encyrpted using base64 because of the two equal signs at the end. Decrypting this gives:

```c
dev@penguin:~$ echo "cDBseWdsMHRwM3NzdzByZA==" | base64 -d
p0lygl0tp3ssw0rd
```

Knowing that this password will be used for something, I try running steghide on the image. However, .png files are not supported. The next thing I did was run binwalk on the file:

```c
dev@penguin:~$ binwalk chall.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1 x 1, 8-bit/color RGBA, non-interlaced
90            0x5A            Zlib compressed data, default compression
119           0x77            Zip archive data, encrypted at least v1.0 to extract, compressed size: 67, uncompressed size: 55, name: secret.gz
348           0x15C           End of Zip archive, footer length: 22
```

This shows that there is an encrypted zip file inside the image. I then extracted the zip file from the image, and then tried unzipping the zip:

```c
dev@penguin:~$ binwalk -e chall.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1 x 1, 8-bit/color RGBA, non-interlaced
90            0x5A            Zlib compressed data, default compression
119           0x77            Zip archive data, encrypted at least v1.0 to extract, compressed size: 67, uncompressed size: 55, name: secret.gz
348           0x15C           End of Zip archive, footer length: 22

dev@penguin:~$ cd _chall.png.extracted
dev@penguin:~/_chall.png.extracted$ ls
5A  5A.zlib  77.zip  secret.gz
dev@penguin:~/_chall.png.extracted$ unzip 77.zip
Archive:  77.zip
[77.zip] secret.gz password:
```

This is where the password from the metadata is used. Using `p0lygl0tp3ssw0rd` to unzip the zip file reveals a gzip file. Using gunzip, the files within the gzip can be accessed. Inside secrets.gz contained the flag `secret`, which contained the flag:

```c
dev@penguin:~/_chall.png.extracted$ gunzip secret.gz
dev@penguin:~/_chall.png.extracted$ ls
5A  5A.zlib  77.zip  secret
dev@penguin:~/_chall.png.extracted$ cat secret
tjctf{p0lygl0t_r3bb1t_h0l3}
```


Flag: `tjctf{p0lygl0t_r3bb1t_h0l3}`
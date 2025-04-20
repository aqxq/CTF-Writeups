## Chunked Integrity (Forensics)
This is one of my favorite images! Unfortunately something has gone wrong and I cant see the whole thing, can you help fix it?

## Solution

First, I verified that the PNG header was valid. Then, I inspected the PNG chunks. A typical layout is `IHDR`, `sRGB`, `gAMA`, `IDAT` (image data), and `IEND`.

However, this file contained a non standard chunk called `EDAT`. It appears in the middle of `IDAT` chunks and had a similar size, which suggested that it was meant to be image data.

This caused me to suspect that `EDAT` was just a mislabeled `IDAT`, so I opened the file in hexed.it and changed `EDAT` to `IDAT` and saved it.

![fixed](imagehere)

This newly rendered image contains the flag.

FLAG: `DawgCTF{C0rrup7_Chunkz}`
## Evanesco

I was in my chambers brewing a new flag, but at the last moment I spilled my invisibility potion all over it! Can you find it for me?

## Solution

Opening the binary in Ghidra, I examine the code and find the main function interesting:
```c
builtin_strncpy(local_a8,
   "\x000e0001\x000e0044\x000e0061\x000e0077\x000e0067\x000e0043\x000e0054\x000e0046\x000e007b"
   "\x000e0075\x000e005f\x000e0063\x000e0061\x000e006e\x000e005f\x000e0074\x000e0061\x000e0067"
   "\x000e005f\x000e0062\x000e0075\x000e0074\x000e005f\x000e0075\x000e005f\x000e0063\x000e0061"
   "\x000e006e\x000e0074\x000e005f\x000e0068\x000e0069\x000e0064\x000e0065\x000e007d\x000e007f"
, 0x91);
```
This line copies an encoded string into `local_a8` using `builtin_strncpy`. The string itself is a series of hex-encoded characters, where each character is prefixed with \x000e.

Each character in the string is represented by a two-byte sequence in the format \x000eXXXX, where XXXX is the actual byte value of the character. By extracting just the last byte (the XXXX part), we can reconstruct the original string.

```c
01, 44, 61, 77, 67, 43, 54, 46, 7b, 75, 5f, 63, 61, 6e, 5f, 74,
61, 67, 5f, 62, 75, 74, 5f, 75, 5f, 63, 61, 6e, 74, 5f, 68, 69,
64, 65, 7d, 7f
```

Converting these bytes into ASCII gives the flag.

FLAG: `DawgCTF{u_can_tag_but_u_cant_hide}`


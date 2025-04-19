## ShinyClean™ Rust Remover: Budget Edition

ShinyClean™ Rust Remover is having a free car wash give away! Run the program to see if you win!

## Solution

By disassembling the binary, I identified the **main function** (`shinyclean::main`).
- This revealed a series of hardcoded byte sequences stored in the stack:

```
0x7b, 0x5e, 0x48, 0x58, 0x7c, 0x6b, 0x79, 0x44,
0x79, 0x6d, 0x0c, 0x0c, 0x60, 0x7c, 0x0b, 0x6d,
0x60, 0x68, 0x0b, 0x0a, 0x77, 0x1e, 0x42
```

- The buffer was initialized with `movb` instructions to store specific byte values starting at `[rsp + 0x41]`.

- The sequence of bytes appeared to be obfuscated and XOR’d (with `0x3f`) to check against a user’s input.

- The buffer was loaded and processed byte-by-byte in a loop. Each byte from the buffer was **XOR’d with `0x3f`** and then compared to user input.

- By reversing the XOR operation, we could decode the original string that would pass the check.

The buffer values were extracted directly from the disassembly, then the XOR operation was applied, allowing for the reconstruction of the correct input.

The result of the decoding process revealed the flag.

Flag `DawgCTF{FR33_C4R_W45H!}`

## Interns' Project

Our interns put together a little test program for us. It seems they all might have patched together their separate projects. Could you test it out for me?

nc connect.umbccd.net 20011

## Solution

The challenge involves interacting with a server running a program that provides a menu with the following options:

1. **Say hi**
2. **Print the flag**
3. **Create an account**

The goal is to print the flag, which is stored in a file named `flag.txt`. The flag is controlled by whether the user is **root** or not.

- **Option 2 (Print the flag)**:
  - If you are **not root**, the program will block flag printing when you select option `2`.
  - If you are **root**, the flag will be printed when you select option `2`.

### **Retrieving the flag**:

   - The program prevents non-root users from accessing the flag directly.
   - To bypass this, input `1 2`. This will make the program execute option `1` (Say hi) and proceed to print the flag after option `2`.

![serverflag](https://github.com/aqxq/CTF-Writeups/blob/main/DawgCTF/Misc/Interns%27%20Project/serverflag.png)

FLAG: `DawgCTF{B@d_P3rm1ssi0ns}`

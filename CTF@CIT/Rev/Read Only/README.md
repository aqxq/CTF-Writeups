## Read Only 

Here we go!

Flag Format: CIT{example_flag}


## Solution

First, before I decide to open this binary in a decompiler, I run strings on it. Specifically, this command: 

```bash
strings readonly | grep -i "CIT{"
```

This results in this:
```bash
┌──(dev㉿dev)-[~/Downloads]
└─$ strings readonly | grep -i "CIT{"
CIT{87z1BjG1968G}
```

FLAG: `CIT{87z1BjG1968G}`

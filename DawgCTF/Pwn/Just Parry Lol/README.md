## Just Parry Lol

Welcome, warrior. Inspired by his favorite game, For Honor, my friend made a turn-based combat simulator to familiarize people with frame data. However, the system is against you. Every move you make is just too slow. You have one secret tool: the ability to manipulate time.

Can you win the fight and retrieve the flag?

nc connect.umbccd.net 25699

## Solution

I decompiled the binary using Ghidra and noticed the function that asks for your warrior name.
```c
puts("Enter your warrior name: ");
gets(s_Player_004040c0);
if ((_s_Player_004040c0 == 0x525241504f545541) && (DAT_004040c8 == 0x59)) {
  DAT_004042d4 = 1;
  puts("You feel faster...");
}c
```

If you input the warrior name "**AUTOPARRY**", the auto-parry feature is activated by setting the flag `DAT_004042d4 = 1`, making you faster in combat.

### Retrieving the flag

![flag](https://github.com/aqxq/CTF-Writeups/blob/main/DawgCTF/Pwn/Just%20Parry%20Lol/flag.png)


FLAG: `DawgCTF{fr4me_d4ta_m4nipulat10n}`


## Ask Nicely

I made this program, you just have to ask really nicely for the flag!

## Solution
Running the binary, it asks you
`How badly do you want the flag?` and then says `Ask nicely...`. 

Running strings on the binary, we find a string: 
```
pretty pretty pretty pretty pretty please with sprinkles and a cherry on top
```
We can assume this to be the key to getting the flag. 

Running the binary again, and using this as the response to "Ask nicely...", you get the flag. 

```
┌──(dev㉿dev)-[~/Downloads]
└─$ ./asknicely
How badly do you want the flag?
@aqxq on github!
Ask nicely...
pretty pretty pretty pretty pretty please with sprinkles and a cherry on top
Good job, I'm so proud of you!
CIT{2G20kX09yF3F}
```
FLAG: `CIT{2G20kX09yF3F}`

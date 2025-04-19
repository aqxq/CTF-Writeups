## Don't Touch My Fone

Looks like someone's dialing a phone number, see if you can figure out what it is! The flag format is the decoded phone number wrapped in DawgCTF{} with no formatting, so if the number is 123-456-7890, then the flag is DawgCTF{1234567890}.

## Solution

Listening to the audio file, you can hear tones that are heard when you punch numbers into your phone's keypad. 
This is called Dual-tone multi-frequency, or DTMF. You can search online for a DTMF decoder. 
I chose to use [this one](https://dtmf.netlify.app/)

By uploading the audio file and setting the sensitivity threshold to 0.1, you are given the phone number, which you can then put into the DawgCTF{} formatting.

FLAG: `DawgCTF{4104553500}`

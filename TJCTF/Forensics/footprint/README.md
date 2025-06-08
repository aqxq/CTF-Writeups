## footprint
The folder used to hold some important files — including one with the flag as its name.
Unfortunately, all the files were deleted. Can you piece together the flag from what’s left behind?

## Solution
Unzipping files.zip reveals that there is one file in the zip: 

```c
dev@penguin:~$ unzip files.zip
Archive:  files.zip
   creating: files/
  inflating: files/.DS_Store
```

.DS_Store is a hidden file that is made by macOS in every folder that is opened in Finder. It stores metadata about how the folder's contents are displayed. It can also contain names of files that were previously in a folder, even if they were deleted. 

However, in order to view the contents, .DS_Store must be parsed. This can be done with a simple [Python script](dsstore.py). Running it results in:

```c
<-FumtF3yx-kSP11OD8mFPA b'Iloc'>
<0wnNJd_pKKNtfhG-HL8iJw b'Iloc'>
<1VmhSaBo9ymK5dUhB3cPEQ b'Iloc'>
<1zp7dw6eF3co0VaPDKhUag b'Iloc'>
<27bCy1Bt-9nnLG4W8oxkNA b'Iloc'>
<4vsxjPs-c9hBNmmaE8HJ8Q b'Iloc'>
<5rc69mw3DNjUvLolTrP3ew b'Iloc'>
<6zed3-nVA008etbNxGTNEQ b'Iloc'>
<78ICY1U_sI9qqF6vv97RhA b'Iloc'>
<7AJTVqVtlVelnulrRMUCaQ b'Iloc'>
<7P7nopvmQj2usona47YjSA b'Iloc'>
<7v9Vn8ci1_C1tyjKpOrDjA b'Iloc'>
<9lZ0k-7YFRkQu1QhA-d-DA b'Iloc'>
<_KxyLnw2LZxOc0Tk9U0cig b'Iloc'>
<A69F-dk9M1nQFfzi06gLPw b'Iloc'>
<abvFjWgNkHKQYbaMyCjdlw b'Iloc'>
<AFEvM2adjTHq0E8noIE0kw b'Iloc'>
<aNHzuom-c5UIGbW5ceGc9g b'Iloc'>
<aNPc9lG0gpLnRvGI2JPQMA b'Iloc'>
<aXNfdXNlZnVsP30gICAgIA b'Iloc'>
<b-PeUWwmlHzmh613ikEFWw b'Iloc'>
<b0HMxEHbs7pA9uHtxRPPTQ b'Iloc'>
<Bg9XKyNnYRSpUIYeK_2knA b'Iloc'>
<CE4CzpPMjNHuYeLi2dLNHg b'Iloc'>
<CPyvVdX_ynvUTdxXWYr7Mw b'Iloc'>
<D0FvxLGtoba2wKJQQEjUKA b'Iloc'>
<D3LWCMzIQyc12SQUw5uDnw b'Iloc'>
<DFhc0ROB762T-pZvtdPFqA b'Iloc'>
<dGpjdGZ7ZHNfc3RvcmVfIA b'Iloc'>
<dtiqv7O15HVT3k4aL1sTDA b'Iloc'>
<Dwv-qkn0QQLu8RlhwUNNeA b'Iloc'>
<e1xUP4GStK_lTs2W6gEkPA b'Iloc'>
<E6IuP9ouzpQDYXSNNdSyFw b'Iloc'>
<E8tEXrVCNAqQmSji8cDWqQ b'Iloc'>
<eNSX5RnqD95dCp7TNI2zOg b'Iloc'>
<eSRLCk2xqnpx1htFqlBAvw b'Iloc'>
<f0wkaX7NmMMATw1grKXIyw b'Iloc'>
<FsmKr0zCKawO9TVNgKkVvA b'Iloc'>
<FxWYnzxWEHMQGNLR_7uXRw b'Iloc'>
<g8azPwD-y-_2VU-dmRK7IA b'Iloc'>
<GQxeqKQR4yLZIz889h8awQ b'Iloc'>
<iHFj7XDSIesD-TJ-aSiTyA b'Iloc'>
<jg1spCuL4Vix9bgpToP5Hg b'Iloc'>
<JuARuIvr7ZvOOpeJ9LTOvA b'Iloc'>
<kAbgNCWwQGUZWFktiIIHeA b'Iloc'>
<kfAVM8pkh2jSSeuP0uWGog b'Iloc'>
<LWUOeeOqK7mlQOTJmSmwVA b'Iloc'>
<LxtZhpBRiU8PSE4eXQZV0w b'Iloc'>
<meMIlojtiqbBuHOGDYud_Q b'Iloc'>
<mLO_JmXEG0tcWougAWQ6Qw b'Iloc'>
<MnbgbJqhwFXlh_kKGIYLJQ b'Iloc'>
<N3lsvxkjSRnwIfz3Z7C5uw b'Iloc'>
<n8KZj1W3tx2WIXg8HqtF3g b'Iloc'>
<niZvI6zZ8yzoSl17d963mQ b'Iloc'>
<Ns2Tpp4fQxW5zhYLLGIVdA b'Iloc'>
<NUhhZkAZsgdvPVVF3KzZpA b'Iloc'>
<p7s4fwmK70UDkM_ApzmX3A b'Iloc'>
<PgbanHSdf0H3qDXVUrVAaA b'Iloc'>
<PGjsQh7wml99RXiA-gta6Q b'Iloc'>
<pJ_ampVpcIVGVZErPVONDQ b'Iloc'>
<pm_TeJmHmlL-5Mdv3R1YoA b'Iloc'>
<pMOW9YUc2Zrd-6B5G3-NSQ b'Iloc'>
<Po5jOoQ4HUssvLHuCmDj5g b'Iloc'>
<pOGlM0FXA5tvruLyZ5AVRA b'Iloc'>
<pPd8nFycxgq3SD67StjdCQ b'Iloc'>
<PqYOp2_ps2oErxR5U5uSXA b'Iloc'>
<PrceMk6k6v8-gPc6YUfuvQ b'Iloc'>
<prsJSTpQJJX5eKJQF3akDg b'Iloc'>
<PuAZy-41HFCOsKTCZkwDBw b'Iloc'>
<QJWXuKXCsnG2mjGYYbyoaA b'Iloc'>
<QLpbpFhcDb2oapdj3Ygutg b'Iloc'>
<Qs13PznBoQJC9yjgWm-clQ b'Iloc'>
<QzopSLFcXVCF5sII8C8jJA b'Iloc'>
<r4NAxKJ_RMhOLA468CAuLQ b'Iloc'>
<rhnhvlSsjRdNv35ZYwqSMg b'Iloc'>
<rkFwpUQRoffUQmfnqKFCNg b'Iloc'>
<sOcYOUIJIYjTYFNud5htCA b'Iloc'>
<sPEu3qqkuJDSVB6LZ0x82w b'Iloc'>
<tCSdwHZsNBvNS3h4qih6tA b'Iloc'>
<TibD2LWT-7Xua5Wmivc-6A b'Iloc'>
<TM0MhKzOCDKMYolGyoYc3g b'Iloc'>
<TxlnTHhAAyM7wIn3PGdLEg b'Iloc'>
<Ur4ktp41Mmf49_FANNugHQ b'Iloc'>
<uvIo5poX5D2dGKif1JiWIA b'Iloc'>
<uXcTlwm5yaS69kQd0YlYgQ b'Iloc'>
<V2XHU0KaptQFjruBnOeYJw b'Iloc'>
<V3JQfigsgWSgJ2bu8IuPOQ b'Iloc'>
<vNgO1oK2Ft-Q_OVtcjk7og b'Iloc'>
<VRU6bDaPkqPqFxsfBjrPQA b'Iloc'>
<VVa_NUjLLaMsO2_Jwko-SA b'Iloc'>
<w1oE_3GO5OTRADuEQ9Pqnw b'Iloc'>
<W62TUuIfC_ma91QdMu4ISA b'Iloc'>
<wzeP722FHEtirWHFJrgP2A b'Iloc'>
<xcTHd2ZbYtO9LQ2fmaQo1Q b'Iloc'>
<XfjqZgZvquXzdnfbcMKQMA b'Iloc'>
<Xnji8EXzCRLmKJvoAkZftA b'Iloc'>
<yfmS9_zOUIcxfSY-obWMhg b'Iloc'>
<ylFen4T5uMeqvJC6p8dfkA b'Iloc'>
<yx7GMqzc5YejMzOO5F087g b'Iloc'>
<Z3cpkGAUMlLgzQctzCo2Zg b'Iloc'>
```

There are two strings in this that are valid base64: `dGpjdGZ7ZHNfc3RvcmVfIA` and `aXNfdXNlZnVsP30gICAgIA`. Decrypting them gives both the first and seocnd halves of the flag.

```c
dev@penguin:~$ echo "dGpjdGZ7ZHNfc3RvcmVfIA" | base64 -d
tjctf{ds_store_
dev@penguin:~$ echo "aXNfdXNlZnVsP30gICAgIA" | base64 -d
is_useful?}
```



Flag: `tjctf{ds_store_is_useful?}`
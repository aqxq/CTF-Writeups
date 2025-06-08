## loopy  
Can you access the admin page? Running on port 5000

loopy.tjc.tf

## Solution
The given website is a website preview tool that allows you to fetch and preview the HTML of a given URL via a POST form. This hints at a Service Side Request Forgery, or SSRF, challenge. 

The main page renders an HTML form:

```html
<form action="/" method="POST">
    <input type="url" name="url" placeholder="Input a URL here">
    <button type="submit">Submit</button>
</form>
```

Submitting something like `https://example.com` returns a preview of the sites HTML. Trying to submit something like `http://127.0.0.1:5000/admin` results in an error:

> Access denied. URL parameter included one or more of the following banned keywords:
> [::], 017700000001, 0.0.0.0, ffff, ::1, 2130706433, local, 127

This shows that representations of localhost, including IPv4, IPv6, and number encodings, are all blacklisted. 

The address `127.0.0.0` can be written in serveral different ways, like 2130706433 in decimal, and 017700000001 in octal. However, these are blocked as well. The trick is to use a different `loopback address`, which resolves to localhost but isn't on the blacklist. An example is the address `127.0.0.2`. In decimal, this address is 2130706434. Submitting `http://2130706434:5000` returns the HTML of loopy.tjc.tf, which means it is not blocked. 

Submitting `http://2130706434:5000/admin` returns the flag.

Flag: `tjctf{i_l0v3_ssssSsrF_9o4a8}`
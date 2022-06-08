# nekonohako
[![PyPI version](https://badge.fury.io/py/nekonohako.svg)](https://badge.fury.io/py/nekonohako)  

A Python wrapper for [catbox.moe](https://catbox.moe) API.

### Installation
```pip install nekonohako```

### Usage

```
from nekonohako import nekonohako

box = nekonohako.NekoNoHako.get('d12esefjoi3jfnsiuefh3f23') # your token, found in User Home -> 
Manage Account; use an empty string for anonimous uploads
 
box.upload_url('https://i.imgur.com/V9ewTLE.png') # upload a file by it's url
box.upload_file('F:\\important\\bloke.png') # upload a file by it's location on your hard drive 
```

Both functions return the uploaded file's URL as a string.

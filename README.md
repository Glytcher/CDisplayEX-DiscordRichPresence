# CDisplayEX Discord Rich Presence

Discord rich presence for the manga/comic reader CDdisplayEX. The script was made with manga in mind, but should work fine for comics too. The script will auto close when CDisplayEX has been closed after a set time. Also includes 2 buttons which can be configured with a config.

![example](https://files.catbox.moe/gkgece.png)

## How does it work?

This program works by getting the window title of CDdisplayEX, therefore your manga/comic needs to have proper naming.

## Dependencies

- Python 3.9+
- CDisplayEx v1.10.33

## Installation

1. Download this repository
2. Install the required packages using `pip install -r requirements.txt`
3. In the same folder, create a config file named `config.json`
4. Copy and paste everything from the template below in the `config.json` and modify it to your liking.
5. Start the script with `python CDisplayEX-RPC.py`

## Config file

```json
{
    "clientID": "873700035227967558",

    "images" : {
        "largeImage": "logo",
        "smallImage": "allogo"
    },

    "hoverText": {
        "largeImageText": "CDisplayEx v1.10.33",
        "smallImageText": "CHANGE THIS"
    },

    "buttons": [
        {
            "label": "Anilist",
            "url" : "https://anilist.co/user/CHANGE THIS/"
        },
        {
            
            "label": "Anilist - Manga List",
            "url" : "https://anilist.co/user/CHANGE THIS/mangalist"
        }
    ],
    "time": {
        "closeTime": "10"
    }
}
```

- smallImageText is the text that will show when you hover over the small AniList logo
- closeTime is the time (in seconds) the script will stay active after CDisplayEX has been closed

## Todo

- [x] Config JSON file
- [ ] Less hardcoding
- [ ] Combine and make some functions smaller
- [ ] Make findProcessIdByName() only return PID instead of filtering the lazy way with the current for loop trick
- [x] Make closing the script easier
- [ ] Toggle option
- [ ] Notifications
- [x] Add requirements.txt for easy installation of dependencies

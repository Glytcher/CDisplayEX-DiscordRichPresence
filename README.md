# CDisplayEX Discord Rich Presence

Discord rich presence for the manga/comic reader [CDisplayEX](https://www.cdisplayex.com/). The script was made with manga in mind, but should work fine for comics too. The script will auto close when CDisplayEX has been closed after a set time (Default 10 seconds). Also includes 2 buttons which can link to a site of your choosing. Both can be configured in a simple JSON config file.

Profile view | Server view
:-------------------------:|:-------------------------:
![Profile view](https://share.wildbook.me/ucONi0JvXZKnnQwT.png)  |  ![Server view](https://share.wildbook.me/wfjLdeLtlY8xhIbe.png)

## How does it work?

This program works by getting the window title of CDisplayEX, therefore your manga/comic needs to have proper naming.

## Dependencies

- Python 3.9+
- CDisplayEx v1.10.33

## Installation

1. Download/git clone this repository
2. Install the required Python packages using `pip install -r requirements.txt`
3. In the same folder, create a config JSON file named `config.json`
4. Copy and paste everything from the config file template below in the `config.json` and modify it to your liking.
5. Start the script with `python CDisplayEX-RPC.py`

### Config file template

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

- smallImage can also be set to `mallogo`, to use the MyAnimeList logo instead
- smallImageText is the text that will show when you hover over the small AniList/MAL logo
- closeTime is the time (in seconds) the script will stay active after CDisplayEX has been closed

## Todo

- [ ] Make findProcessIdByName() only return PID instead of filtering the lazy way with the current for loop trick
- [ ] Toggle option
- [ ] Handle multiple CDisplayEX instances

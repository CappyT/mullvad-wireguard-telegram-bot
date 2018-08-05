# MULLVAD WIREGUARD TELEGRAM BOT (MWTB)
## PLEASE NOTE THAT I'M A COMPLETE DISASTER AT CODING
##### So teach me the proper way to do it.
###### Also note that english is not my native language


This tool is designed to help manage forward and get various account informations (such as wireguard configs) from
a telegram bot. (since mullvad doesn't provide an api for that)

**It is far from being pretty and uses hacks and poor performing method to get the job done.** (but since i don't know any other way ¯\_(ツ)_/¯)

Feel free to contribute via PR request stating your changes and PLEASE be gentle with me. I just started coding.


```
from brain import disclaimer

PLEASE DO NOT USE THIS TOOL TO ABUSE MULLVAD SERVICE.
THIS TOOL IS NOT SUPPORTED NOR DEVELOPED OR OFFICALY APPROVED FOR USE 
FROM MULLVAD.

THE USE OF THIS TOOL CAN GET YOU PERMANENTLY SUSPENDED FROM THEIR SERVICES.
PLEASE USE THIS TOOL FOR PERSONAL PURPOSES AND PERSONAL RESEARCH ONLY.

YOU HAVE BEEN WARNED.
```

Currently in the to do list:
* Get all the account info from Mullvad
* Implement a telegram bot
* Handle renew
* Handle updates from mullvad
* Handle new clients (for multiplexing servers)
* Manage (activate/deactivate/change) wireguard configs
* Get and set forwarded ports
* Handle iptables and redirection (for multiplexing servers)
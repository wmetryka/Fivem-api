# FiveM-Api

[![Downloads](https://pepy.tech/badge/fivem)](https://pepy.tech/project/fivem)

Small API Wrapper for interacting with the FiveM API

**How-to install :**

```
pip install fivem
```

**How-to use :** 

```python
import fivem

server = fivem.getServer("88.214.59.183:30120")
print(server.players)
```
Display the number of players online on a server

```python
fivem.getServer("ip-address:port") # default port is 30120
```
Returns a Server Class with those attributes:
```
players: [{
        "endpoint"; string,
        "id": int, // The server ID og the player
        "identifiers": array, // Identifiers of the player
        "name": string, // Username's player
        "ping": int, // Le ping
}],
info: {
    "enhancedHostSupport": boolean,
    "icon": string, // Icon of the server (Base64)
    "resources": array, // All started resources
    "server": string, // FXServer's version (string format)
    "vars": { // Some convars defined in server.cfg
        "sv_enhancedHostSupport": boolean,
        "sv_lan": boolean,
        "sv_licenseKeyToken": string,
        "sv_maxClients": int,
        "sv_scriptHookAllowed": boolean,
        "sv_hostname": string,
    },
    "version": int, // FXServer's version (numeric format)
},
name: string // Name of the server
```

This API is loosely based on the [node.js Fivem API](https://github.com/Heavenston/FiveM-Api/).

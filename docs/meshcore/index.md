# Meshcore
![Meshcore Logo](/media/meshcore/meshcore_logo.png)

[MeshCore](https://meshcore.co.uk/) is a multi platform system for enabling secure text based communications utilizing LoRa radio hardware. It can be used for Off-Grid Communication, Emergency Response & Disaster Recovery, Outdoor Activities, Tactical Security including law enforcement and private security and also IoT sensor networks.

## Joining

Are you interested in joining the mesh? You will need to purchase a LoRa radio from the [MeshCore Supported Devices](https://meshcore.co.uk/get.html) list. Outside of the mesh, we are most active on our public [Discord Server](https://discord.gg/ANvUg3AyZt) including a whole section for MeshCore discussions. 


### Roles
- **Companion**: Intended role for end-user devices which provide an interface via the phone or web app (via BLE or USB)
- **Repeater**: Nodes in this role extend the range of a MeshCore Network. It does **NOT** forward or retransmit every packet it receives.
- **Room Server**: Turns the node into a simple BBS server for sharing posts. Room servers store message history on them and push the stored messages to users. Room servers allow roaming users to come back later and retrieve message history. 
- **Room-Peater**: A combination of Room Server and Repeater roles. Install the Room Server then enable repeater role via the "set repeat {on|off}" command.

### Radio Settings
Use these settings to connect to other nodes in our area. More information about these settings can be [found in the MeshCore documentation](https://github.com/ripplebiz/MeshCore/blob/main/docs/faq.md#51-q-what-are-bw-sf-and-cr).

Setting | Value
---: | :---
Frequency | 910.525 MHz
Bandwidth | 250 kHz
Spreading Factor | 11
Coding Rate | 5

## Map
Be sure to checkout the official [MeshCore Map](https://meshcore.co.uk/map.html) as well. Here is a screenshot of the local area in June 2025.

![MeshCore Map as of April 2025](/media/meshcore/Meshcore_2025-06-25.png)


## Member Projects

### Ciesen's "meshcoretomqtt"
[https://github.com/cisien/meshcoretomqtt/](https://github.com/cisien/meshcoretomqtt/) "A python based script to send meshcore debug and packet capture data to MQTT for analysis. Requires meshcore repeater to be connected to a raspberry pi, server or similar linux device able to run python."

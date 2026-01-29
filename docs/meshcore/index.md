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

These settings can be found in the MeshCore app listed as `USA/Canada (Recommended)`

Setting | Value
---: | :---
Frequency | 910.525 MHz
Bandwidth | 62.5 kHz
Spreading Factor | 7
Coding Rate | 5

## Repeaters

Meshcore works well with neighborhood repeaters, increase the range and reliability of Puget Mesh by setting up your own repeater. The [Repeater Setup Guide](repeater_setup.md) walks you through the process.

## Channels
Hashtag topic keys are automatically calculated by the system. The keys are included to help users on devices that cannot type the # (hash) symbol or lack the key calculation functionality.

Topic | Key
---: | :---
#bot | eb50a1bcb3e4e5d7bf69a57c9dada211
#bot-tacoma | 278df637e12a0dda01c826e1fd9779fd
#bot-van | bf07fbf914e37710561cb741e914efeb
#capitolhill | 7f281916c8ec32e13c5ef687d182160a
#emergency | e1ad578d25108e344808f30dfdaaf926
#hamradio | 83c8b01997654265938da8765cbc7db9
#protest | 195e9167baf010c4538d8532b6d7296e
#queer | 5754476f162d93bbee3de0efba136860
#seattle | ef627a9bbbb549347fdb76bf0cd3bc14
#seahawks | 4973d6ceb6c35a09894a83688847c8a3
#sports | e8ee81f3aabf105d9ba2d2d4bd94fe4a
#testing | cde5e82cf515647dcb547a79a4f065d1

## Map

Here is an embed of the live map of nodes from [MeshExplorer](https://map.w0z.is). Be sure to checkout the official [MeshCore Map](https://meshcore.co.uk/map.html) as well.

<iframe src="https://map.w0z.is/embed/map?lat=47.81315&lng=-122.77222" width="100%" height="500" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>

## Member Projects

### MeshExplorer

[https://map.w0z.is](https://map.w0z.is) "MeshExplorer is a web-based visualization tool for exploring and monitoring mesh networks. It provides real-time mapping of network nodes, message tracking, and statistical analysis for MeshCore and Meshtastic networks." (source: MeshExplorer Info modal)

### Ciesen's "meshcoretomqtt"

[https://github.com/cisien/meshcoretomqtt/](https://github.com/cisien/meshcoretomqtt/) "A python based script to send meshcore debug and packet capture data to MQTT for analysis. Requires meshcore repeater to be connected to a raspberry pi, server or similar linux device able to run python."

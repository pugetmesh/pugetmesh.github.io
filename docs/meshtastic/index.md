# Meshtastic
![Meshtastic Logo](/media/Meshtastic_Banner_Logo.png)

Meshtastic® is a project that lets you use inexpensive LoRa radios as a long range off-grid communication platform in areas without existing or reliable communications infrastructure. This project is 100% community driven and open source! The radios automatically create a mesh to forward packets to neighbors (up to 3 hops from origin). The radios will optionally work with your phone, but no phone is required. Puget Mesh is working to build a mesh in our region that anyone can connect to. The intention is for this off-grid network to be available as an Emergency/Disaster response tool. One large advantage of Meshtastic over GMRS or Amateur radio services is that no license is required to use Meshtastic. Please note. Meshtastic is still in active development and should not be considered as a life-critical service. 

## Joining

Are you interested in joining the mesh? You will need to purchase a LoRa radio from the [Supported Hardware](https://meshtastic.org/docs/hardware/devices/) list. Outside of the mesh, we are most active on our public [Discord Server](https://discord.gg/ANvUg3AyZt).

* Read about fundamental concepts of Meshtastic in [Adam's Presentation](https://docs.google.com/presentation/d/1xx2Ae8VMTQzYbq140SX4FAlHGFCDjrVD/edit#slide=id.p1)
* Review the [FAQ](/meshtastic/faq)
* Review the [Configuration](config) page
* Checkout our [Equipment](/meshtastic/equipment)

## Weekly Net
Every Monday evening at 6:13:45pm (906.875x2 = 1813.75 hours) we have our weekly net on the public default LongFast channel, on the default LONG_FAST frequency slot 20. We also touch base on our [discord weekly-net channel](https://discord.com/channels/1291139029814739084/1323907750690029578) and voice channel.

**Net Control Guide**

At 6:13:45pm please send the following message:

```
##### Welcome to the Puget Mesh Net! #####
Every Monday at 1813.75 please check in with:
"Hello KK4GKF, this is <my_name> in <my_location>"
I will acknowledge all check-ins that I receive.
```

Respond to every check-in that you receive and include their name and location.

```
KK4GKF (Net Control) received check-in from <their_name> in <location>.
```

It may feel redundant to include names in the messages, but this ensures all parties have the node name available. Node lists typically only remember the 100 most recent node names and this is easy to exceed in high mesh-density areas.

At the end of the net, send your results to the Meshtastic discord channel (list of who was heard, their location, your location).

---

## MQTT and Maps

MQTT [Message Queue Telemetry Transport](https://en.wikipedia.org/wiki/MQTT) is a lightweight publish-subscribe network protocol from the late 90's designed for connections with remote locations that have devices with resource constraints or limited network bandwidth. Meshtastic comes with the option to connect your node to a MQTT server on the internet and exchange information (Mostly device information and messages). MQTT comes with benefits and considerations.

**MQTT Benefits**

- MQTT is a reliable way for a computer to interact with your node directly, not over LoRa.
- Messages can be sent (Uplink), and received (Downlink), to an MQTT server allowing for two nodes to exchange messages when they are outside of range of each other over LoRa. In fact, we have an [entire channel just for sending and receiving messages over mqtt (PS-MQTT!)](http://localhost:8000/meshtastic/config/#ps-mqtt-channel).
- The device information, and telemetry information sent to the MQTT server can be used by software to make fun things [like the online web map server that we use hosted by a local member](https://mqtt.davekeogh.com/).
- You can "self-report" or see who on the mesh has received your messages. We have software that takes all of the channel messages any of our MQTT contributing nodes have seen and posts them to our discord server (look at the threads under the "mqtt-messages" channel). This is extremely helpful for choosing the best hop value for your node at your location.

**MQTT Considerations**

- Some Meshtastic groups use MQTT heavily for messaging. We have decided that we want our mesh to work over RF so we are focused on building and improving it there. We do have the local PS-MQTT! channel for messaging over MQTT, but all other messaging is RF. 
- We do not use the default MQTT server for our area. This allows us to exchange messages with people in our area, vs the whole world, as well as having more control over the data on the MQTT server (privacy and moderation). In our area we use [https://meshtastic.davekeogh.com/](https://meshtastic.davekeogh.com/)
- Your node info and channel messages are sent to MQTT servers. Either by you directly connecting your node to a server, or via other nodes on the mesh that uplink (send). Enabling "OK to MQTT" on your node helps ensure that your node info/messages is sent to MQTT by others (Note: This is just a flag that nodes optionally respect, so disabling this feature does not entirely prevent it from being sent).
- If your node is connected to an MQTT server, please do not enable downlink on LongFast (or other channels without consideration). This causes a large increase in traffic from your node, which impacts the mesh around you. For nodes not connected to an MQTT server, the "Ignore MQTT" setting helps block this traffic, but this is not enabled by default.


</br>
**Local Map**

[![Dave Keogh Meshtastic Map](/media/11Nov2024_MapSShot.png){ width="300", align=left }](https://meshtastic.davekeogh.com/?lat=47.73284666107599&lng=237.66448974609378&zoom=9)

On [this map](https://meshtastic.davekeogh.com/?lat=47.73284666107599&lng=237.66448974609378&zoom=9) you will see blue and green dots. These are each nodes in our area that have chosen to share their position. You can also search at the top for any node seen by the mesh, including nodes not on the map. Green dots are MQTT contributors to this MQTT server, blue nodes are not. The vast majority of us have chosen not to use MQTT with Meshtastic in the spirit of embracing the RF mesh itself. However, we do utilize our own MQTT server for exchanging position data which is plotted on a map. This is helpful for understanding where the mesh needs to grow, and is helpful for onboarding new users.

- Use the Layers menu in the top right to view Node types and Overlays.
- Click on a Node for Node-specific information.
- [Visit our guide](/meshtastic/config/#get-on-the-map) to see how to get onto the public MQTT maps.

<!--
### Collaborative Map

<iframe style="height:500px; width:100%; border:none;" src="https://facilmap.org/NOb2ESIvTxlC3Z?search=false#10/47.6462/-122.3625/Lima"></iframe>

This collaborative map allows users to place their fixed nodes for others to see. Regardless of their MQTT settings or connectivity. This also allows us to coordinate potential new sites to help grow the mesh.
-->

## Member Projects
We have a lot of talented folks in our area working on interesting Meshtastic projects. Here are a few:

### SpudGunMan "Meshing Around"
[https://github.com/SpudGunMan/meshing-around](https://github.com/SpudGunMan/meshing-around) "This feature-rich bot is designed to enhance your Meshtastic network experience with a variety of powerful tools and fun features, connectivity and utility through text-based message delivery. Whether you're looking to perform network tests, send messages, or even play games, mesh_bot.py has you covered."

### Aforney "APRStastic"
[https://github.com/afourney/aprstastic](https://github.com/afourney/aprstastic) "aprstastic is a bidirectional Meshtastic APRS gateway for Meshtastic users with amateur radio licenses. It runs on stock Meshtastic devices (LongFast, 915MHz, etc.), allowing you to participate and extend the public network, while using pre-registered associations between Meshtastic device IDs and amateur radio call signs to bidirectionally gate APRS packets in a way that is compliant with FCC regulations... "

### Aforney "Discord Mesh Bot" (As seen on our discord) 
[https://github.com/afourney/discord_mesh_bot](https://github.com/afourney/discord_mesh_bot) "Simple script for relaying meshtastic messages onto Discord." Our's utilizes the same MQTT server as our local maps.

### Mike Carper's "Mesh Firmware"
[https://github.com/mikecarper/meshfirmware](https://github.com/mikecarper/meshfirmware) "This Bash script automates the process of selecting, downloading, and applying firmware updates from the meshtastic/firmware GitHub repository. It is designed to simplify firmware management for meshtastic devices by handling everything from version selection to device update.

### Adam Gessaman's Customized "Mesh Info Lite"
[https://meshinfo.gessaman.com](https://meshinfo.gessaman.com/) "A highly customized version of MeshInfo written in Python that inspects and visualizes Meshtastic traffic. NeighborInfo, NodeInfo, and Telemetry are used to provide a mesh map, connectivity information, and other insights into nodes and the mesh as a whole."

---

## Other Local Meshtastic Groups
A large list of Meshtastic groups can be found [on Meshtastic.org](https://meshtastic.org/docs/community/local-groups/#washington)

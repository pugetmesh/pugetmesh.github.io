# Meshtastic
![Puget Mesh Logo](/media/Meshtastic_Banner_Logo.png)

Meshtastic® is a project that lets you use inexpensive LoRa radios as a long range off-grid communication platform in areas without existing or reliable communications infrastructure. This project is 100% community driven and open source! The radios automatically create a mesh to forward packets to neighbors (up to 3 hops from origin). The radios will optionally work with your phone, but no phone is required. Puget Mesh is working to build a mesh in our region that anyone can connect to. The intention is for this off-grid network to be avaialable as an Emergency/Disaster response tool. One large advantage of Meshtastic over GMRS or Amateur radio services is that no license is required to use Meshtastic.

## Joining
Are you interested in joining the mesh? You will need to purchase a LoRa radio from the [Supported Hardware](https://meshtastic.org/docs/hardware/devices/) list. Outside of the mesh, we are most active on our public [Discord Server](https://discord.gg/ANvUg3AyZt).

* Review the [FAQ](/meshtastic/faq)
* Review the [Configuration](config) page
* Checkout our [Site Installations](/meshtastic/installations).

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
[![Dave Keogh Meshtastic Map](/media/11Nov2024_MapSShot.png){ width="250", align=left }](https://meshtastic.davekeogh.com/?lat=47.73284666107599&lng=237.66448974609378&zoom=9)
Meshtastic devices can be connected to the internet and exchange information (messages, data, telemetry, etc) by using a MQTT server.

The vast majority of us have chosen not to use MQTT with Meshtastic in the spirit of embracing the RF mesh itself. However, we do utilize our own MQTT server for exchanging position data which is plotted on a map. This is helpful for understanding where the mesh needs to grow, and is helpful for onboarding new users.

There are a few public maps available showing nodes (that choose to share their position) but we use [https://meshtastic.davekeogh.com/](https://meshtastic.davekeogh.com/).

- Use the Layers menu in the top right to view Node types and Overlays.
- Click on a Node for Node-specific information.

## Member Projects
We have a lot of talented folks in our area working on interesting Meshtastic projects. Here are a few:

### SpudGunMan "Meshing Around"
[https://github.com/SpudGunMan/meshing-around](https://github.com/SpudGunMan/meshing-around) "This feature-rich bot is designed to enhance your Meshtastic network experience with a variety of powerful tools and fun features, connectivity and utility through text-based message delivery. Whether you're looking to perform network tests, send messages, or even play games, mesh_bot.py has you covered."

### afourney APRStastic
[https://github.com/afourney/aprstastic](https://github.com/afourney/aprstastic) "aprstastic is a bidirectional Meshtastic APRS gateway for Meshtastic users with amateur radio licenses. It runs on stock Meshtastic devices (LongFast, 915MHz, etc.), allowing you to participate and extend the public network, while using pre-registered associations between Meshtastic device IDs and amateur radio call signs to bidirectionally gate APRS packets in a way that is compliant with FCC regulations... "

---

## Other Local Meshtastic Groups
A large list of Meshtastic groups can be found [on Meshtastic.org](https://meshtastic.org/docs/community/local-groups/#washington)

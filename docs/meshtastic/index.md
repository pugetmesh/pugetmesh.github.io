# Meshtastic
![Puget Mesh Logo](/media/Meshtastic_Banner_Logo.png)

Meshtastic® is a project that lets you use inexpensive LoRa radios as a long range off-grid communicator for areas without reliable cellular service. These radios are great for hiking, skiing, paragliding - essentially any hobby where you don't have reliable internet access. Each member of the mesh can send and view text messages and enable optional GPS based location features.

The radios automatically create a mesh to forward packets as needed, so everyone in the group can receive messages from even the furthest member. The radios will optionally work with your phone, but no phone is required. Visit [Verified Keys](verifiedkeys) to verify users on the mesh. 

## Joining
Are you interested in joining the mesh? You will need to purchase a LoRa radio from the [Supported Hardware](https://meshtastic.org/docs/hardware/devices/) list which start at about $35. Outside of the mesh, we are most active on our public [Discord Server](https://discord.gg/ANvUg3AyZt).

Puget Mesh node installed at Maple Leaf in Seattle:

[![Puget Mesh Logo](/media/MLA_Node.jpg)](/media/MLA_Node.jpg)

**Note**: Node names beginning with "PugetMesh.org" are not actively monitored so a direct message reply is unlikely.

### MQTT and Maps
[![Dave Keogh Meshtastic Map](/media/11Nov2024_MapSShot.png){ width="250", align=left }](https://meshtastic.davekeogh.com/?lat=47.73284666107599&lng=237.66448974609378&zoom=9)
Meshtastic devices can be connected to the internet and exchange information (messages, data, telemetry, etc) by using a MQTT server. 

The vast majority of us have chosen not to use MQTT with meshtastic in the spirit of embracing the RF mesh itself. However, we do utilize our own MQTT server for exchanging position data which is plotted on a map. This is helpful for understanding where the mesh needs to grow, and is helpful for onboarding new users.

There are a few public maps available showing nodes (that choose to share their position) but we use [https://meshtastic.davekeogh.com/](https://meshtastic.davekeogh.com/).

- Use the Layers menu in the top right to view Node types and Overlays.
- Click on a Node for Node-specific information.

## Best Practices
There are a lot of configuration options and it can be difficult to know where to start. 
### TL;DR;
- **LoRa**: Modem Preset=LONG_FAST, Frequency slot=20 (906.875MHz)
- **Role**: Client (Router modes are reserved for towers and mountains)
- **Hop Count**: 3 (Everyone can see when you use hop counts over 3)
- **Broadcast Intervals(info, position, telemetry)**: 3hours (10800 seconds)
- **Leave your node running for 24 hours the first time to get well connected to the mesh.**

Alternate Frequency/Preset standardizations for the area:

- **LoRa**: Modem Preset=MEDIUM_FAST, Frequency slot=45 (913.125MHz)
- **LoRa**: Modem Preset=SHORT_FAST, Frequency slot=68 (918.875MHz)

[Configuration Recommendations](config)

## New User Expectations
It is important to know that Meshtastic is under rapid development, and is not yet a *polished* product. There are bugs and quirks but that is part of the fun. If you have just turned on your Meshtastic device for the first time, get it in a good location (being next to a window can help) and let it run overnight. It takes time to see other nodes, and for other nodes to see you, assuming you are somewhere with decent coverage. 

## Common Configurations

Here are some common configurations and use cases highlighting configurations you should consider using. In all of the below examples, all Meshtastic radios are configured with the default settings, which allow them to communicate with each other over the LongFast channel on the default frequency slot and default modem preset of LONG_FAST with ham mode not enabled. 

Commonly, users have a Meshtastic radio paired with their phone via bluetooth, they are then able to send and receive messages with other Meshtastic users using the app on their phone. No internet connection is required. Both of these nodes are within LoRa range of each other.

![Meshtastic Bluetooth-LoRa diagram](/media/meshtastic_device-to-device.png)

When users are **not** within range of each other, they can utilize the mesh that meshtastic offers. Your messages do not have to be received directly by another user, they can hop over users of the network until they arrive at their destination or stop trying. Be sure to review the New User Expectation above if you are a first time user.

### Understanding "hops"
Unfortunately, as of V2.5.*, Meshtastic still uses the term "hop" incorrectly. Using the default "hop" limit of 3 actually means you get 4 hops as demonstrated below. It is highly recommended you keep the default hop count unless you are in a special circumstance such as using CLIENT_MUTE in the scenario shown later on.

![Meshtastic hops diagram](/media/meshtastic_max-hops.png)

### CLIENT_MUTE
One common setup people have at home is a Meshtastic node in their house connected to their phone via bluetooth (Node A). They have another node, often solar powered, located on a roof or at a high point on their property (Node B). 

In this example below, we have introduced Node B which is solar powered and you can imagine it installed on a rooftop or somewhere very high. Node A and Node C cannot communicate directly, but both can communicate back and forth with Node B. 

![Meshtastic CLIENT_MUTE example](/media/meshtastic_client-mute-example.png)

This is a common situation if Node A is indoors and Node B is on your roof. You can choose to set Node A to CLIENT_MUTE, and increase the hop count to 4. CLIENT_MUTE prevents Node A from repeating any messages that it hears which allows Node B to repeat them (and much more successfully be heard since it is mounted in a better location).

### Unhelpful Repeater/Router
Unfortunately for the network, many people believe router/repeater modes are their best choice for a node on their roof or in a tree when in reality it usually hurts the network. This is almost always not intentional. This clarification is something that needs to be made much clearer in the Meshtastic software and documentation. Client mode is the best option for this scenario. Nodes in CLIENT mode repeat your messages to other nodes and will repeat their messages back to you so you can hear them.

Router and Repeater modes should be saved for mountain tops and towers. Even then, careful consideration should be made before using one of these nodes. Ideally you can connect with your local mesh group (like this one!) and come to a determination. Please use CLIENT mode.

In this example we have the same scenario as shown in CLIENT_MUTE above except we have introduced Node D configured as a Router. Node A and Node C cannot communicate directly with each other, and Node C and Node D cannot communicate directly either. When Node A sends a message, Node B repeats it first (since it is configured as a Router). Because of this, Node B will not rebroadcast the message out since it has already heard the message twice. Node C will never receive the message. What can be even more confusing is that Node C can send messages to Node A successfully, this can be difficult to troubleshoot and diagnose.

![Meshtastic unhelpful repeater example](/media/meshtastic_bad-repeater-example.png)

**What to do if someone near you is using a Router or Repeater mode?** Firstly, be kind. They may not realize that their node is negatively impacting the network, also they may have it configured in a way in which it is indeed helping greatly but that is not obvious. Send a kind message asking them to consider moving to CLIENT mode instead. Also consider pointing them to our discord or this website, we are here to help communicate and figure out what is best for the mesh as a group. Just a reminder that Meshtastic is a public, unlicensed, network. Puget Mesh is not responsible for how others use the mesh or what they publish on it.

## Troubleshooting
- Is your device misbehaving?
- Are you struggling to get connected to the mesh (after letting your device run for 24 hours)?
- Have other questions or comments?
- [Austin Mesh](https://www.austinmesh.org/join/) is a good resource for Meshtastic information.

Come join our [Discord](https://discord.gg/ANvUg3AyZt)

## Other Local Meshtastic Groups
A large list of Meshtastic groups can be found [on Meshtastic.org](https://meshtastic.org/docs/community/local-groups/#washington)


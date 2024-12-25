# Meshtastic Configuration

The following two sections ([Common Configs](/meshtastic/config/#common-configurations) and [Recommended Configs](/meshtastic/config/#recommended-configurations)) are intended to help new users understand common use cases and choose settings that work well for them and for the mesh as a whole. Checkout the [FAQ](/meshtastic/faq) page for troubleshooting tips. In our area we are still building out the mesh on the default frequency slot (20) and model preset (LONG_FAST).

Frequency/Preset standardizations for the area:

- **LoRa**: Modem Preset=LONG_FAST, Frequency slot=20 (906.875MHz)
- **LoRa**: Modem Preset=MEDIUM_FAST, Frequency slot=45 (913.125MHz)
- **LoRa**: Modem Preset=SHORT_FAST, Frequency slot=68 (918.875MHz)

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

## Recommended Configurations
Can't find a setting?  Check the [Meshtastic docs](https://meshtastic.org/docs/configuration/) for more info - each page has tabs for iOS, Android, CLI, and Web.

### Fixed Nodes

*If your node will move, please use the portable node configuration*


=== "Radio>User"
    * **Long name:** Please consider adding "📵" to your node long name for nodes that are not monitored.
    * **Licensed amateur radio:** `FALSE` 

=== "Radio>Device"

    * **Role:** usually should be `CLIENT` or `CLIENT_MUTE` or other roles as appropriate by situation. It is rare that `ROUTER` or `REPEATER` are appropriate, so please consult with the group on Discord before doing so.  Adding nodes with these roles can negatively impact the mesh.  The role `ROUTER_CLIENT` (deprecated) should not be used.  For more information see the [Meshtastic docs](https://meshtastic.org/docs/configuration/radio/device/#roles).
    * **Node Info Broadcast Interval:** `10800` seconds

=== "Radio>Position"

    * **GPS Mode:** `ENABLED` if present, else `NOT_PRESENT`.  *Note: when connected to iOS or Android, phone GPS can be relayed to the node if the node does not have GPS.*
    * **Fixed Position:** `TRUE` is often appropriate for fixed nodes, but not required.  This can be set via CLI or sent from phone GPS.
    * **Broadcast Interval:** `18000` seconds

=== "Radio>LoRa"

    * **Region:** `US`
    * **Hop Limit:** `3`
    * **OK to MQTT:** `TRUE` - this allows packets to be uploaded to MQTT, required to show up on the map if not directly uploading to MQTT.  *Note: this is a request and may not necessarily be honored.*

=== "Radio>Bluetooth"

    *If present & desired to be enabled (optional)*

    * **Enabled:** `TRUE`
    * **Pairing Mode:** `Random PIN` or `Fixed PIN` (if no screen/ screen visible to public: fixed; else either as desired).
    * **PIN:** (if fixed) anything but `123456` - remember to change this if using fixed PIN.

=== "Modules>Neighbor Info"
    *NOTE: Neighbor Info is no longer shared across the mesh on long_fast*

    * **Enabled:** `TRUE` *If you are MQTT Connected, otherwise* `FALSE`
    * **Update Interval:** `18000` seconds

### Portable Nodes

=== "Radio>Device"
    * **Role:** usually should be `CLIENT` or `CLIENT_MUTE` or other roles as appropriate by situation.  `ROUTER`, `REPEATER`, and `ROUTER_CLIENT` should not be used. For more information see the [Meshtastic docs](https://meshtastic.org/docs/configuration/radio/device/#roles).
    * **Node Info Broadcast Interval:** `1200` seconds

=== "Radio>Position"

    * **GPS Mode:** `ENABLED` if present, else `NOT_PRESENT`.  *Note: when connected to iOS or Android, phone GPS can be relayed to the node if the node does not have GPS.*
    * **Fixed Position:** `FALSE` is often appropriate for fixed nodes, but not required.  This can be set via CLI or sent from phone GPS.
    * **Broadcast Interval:** `1200` seconds

=== "Radio>LoRa"

    * **Region:** `US`
    * **Hop Limit:** `3`
    * **OK to MQTT:** `TRUE` - this allows packets to be uploaded to MQTT, required to show up on the map if not directly uploading to MQTT.  *Note: this is a request and may not necessarily be honored.*

=== "Radio>Bluetooth"
    *If present & desired to be enabled (optional)*

    * **Enabled:** `TRUE`
    * **Pairing Mode:** `Random PIN` or `Fixed PIN` (if no screen/ screen visible to public: fixed; else either as desired).
    * **PIN:** (if fixed) anything but `123456` - remember to change this if using fixed PIN.

=== "Modules>Neighbor Info"
    *Please do not enable neighbor info for portable nodes as it makes telemetry difficult to interpret*

    * **Enabled:** `FALSE`

### Get on the Map
The following changes are necessary for your node to appear on the map.

=== "Channels>Primary"

    * **Allow Position Requests:** `TRUE`
    * **Precise Location:** `FALSE`
    * **Approximate Location:** Choose a value you are comfortable with.

    #### If Enabling MQTT

    * **Uplink Enabled:** `TRUE`
    * **Downlink Enabled:** `FALSE`

=== "Modules>MQTT"

    Enabling MQTT will guarantee you will appear on the map, otherwise you must have "OK to MQTT" (Found under LoRa), position on, and connect to a node uplinked to MQTT.

    * **Enabled:** `TRUE`
    * **MQTT Server Address:** `mqtt.davekeogh.com` - this server is required to show up on our map.
    * **Username/Password:** Leave default or go to [the map](https://mqtt.davekeogh.com/) for details.
    * **Encryption Enabled:** `TRUE`
    * **JSON Enabled:** `FALSE`
    * **TLS Enabled:** `FALSE`
    * **Root Topic:** `msh/US`
    * **Map Reporting Enabled:** `TRUE`
    * **Map Report Publish Interval:** Fixed: `3600`, Portable: `300`
    * **Approximate Location:** Choose a value you are comfortable with.

---
## Alternate Channels

### PS-Mesh! Channel
There are more channels than the default LongFast, one of them is our PS-Mesh! channel which you are welcome to join and is related to this group. be sure to pay attention when adding the channel so you don't replace your current channels.

- Channel Name: "PS-Mesh!"
- PSK: "jHrxpQOq6dEBC5Ldr3ULrQ=="

[![PS-Mesh! QR Code](/media/ps-mesh-qr.png){ width=250 }](https://meshtastic.org/e/?add=true#CiESEIx68aUDqunRAQuS3a91C60aCFBTLU1lc2ghJQIAAAASDwgBOAFABUgBUB5oAcgGAQ)

### PS-MQTT! Channel

If you wish to communicate with others in the area over MQTT, use this channel. You will need to enable "OK to MQTT" under the LoRa settings, and you will need to enable uplink and downlink for the channel. Reminder that connecting your node to MQTT does send your data to the mqtt server. You do not need to directly connect your node to MQTT for this to work. 

- Channel Name: "PS-MQTT!"
- PSK: "mqttmqttmqttmqttmqttQQ=="

[![PS-MQTT! QR Code](/media/ps-mqtt-qr.png){ width=250 }](https://meshtastic.org/e/?add=true#CiESEJqrbZqrbZqrbZqrbZqrbUEaCFBTLU1RVFQhJQMAAAASDggBOAFABkgBUB5YFGgB)


All Messages sent to PS-MQTT! (that are received by a node connected to the MQTT server) are published to our ps-mqtt Discord Channel.
<iframe src="https://e.widgetbot.io/channels/1291139029814739084/1319416890820395019" allow="clipboard-write; fullscreen" height="550" width="100%"></iframe>
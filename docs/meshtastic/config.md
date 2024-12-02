# Recommend Configuration
Can't find a setting?  Check the [Meshtastic docs](https://meshtastic.org/docs/configuration/) for more info - each page has tabs for iOS, Android, CLI, and Web.

## Fixed Nodes
*If your node will move, please use the portable node configuration*
=== "Radio>Device"
**Role:** usually should be `CLIENT` or `CLIENT_MUTE` or other roles as appropriate by situation. It is rare that `ROUTER` or `REPEATER` are appropriate, so please consult with the group on Discord before doing so.  Adding nodes with these roles can negatively impact the mesh.  The role `ROUTER_CLIENT` (deprecated) should not be used.  For more information see the [Meshtastic docs](https://meshtastic.org/docs/configuration/radio/device/#roles).

**Node Info Broadcast Interval:** `10800` seconds

=== "Radio>Position"
**GPS Mode:** `ENABLED` if present, else `NOT_PRESENT`.  _Note: when connected to iOS or Android, phone GPS can be relayed to the node if the node does not have GPS._

**Fixed Position:** `TRUE` is often appropriate for fixed nodes, but not required.  This can be set via CLI or sent from phone GPS.

**Broadcast Interval:** `18000` seconds

=== "Radio>LoRa"
**Region:** `US`

**Hop Limit:** `3`

**OK to MQTT:** `TRUE` - this allows packets to be uploaded to MQTT, required to show up on the map if not directly uploading to MQTT.  _Note: this is a request and may not necessarily be honored._

=== "Radio>Bluetooth"
_If present & desired to be enabled (optional)_

**Enabled:** `TRUE`

**Pairing Mode:** `Random PIN` or `Fixed PIN` (if no screen/ screen visible to public: fixed; else either as desired).

**PIN:** (if fixed) anything but `123456` - remember to change this if using fixed PIN.

=== "Modules>Neighbor Info"
**Enabled:** `TRUE`

**Update Interval:** `18000` seconds

---

## Portable Nodes

=== "Radio>Device"
**Role:** usually should be `CLIENT` or `CLIENT_MUTE` or other roles as appropriate by situation.  `ROUTER`, `REPEATER`, and `ROUTER_CLIENT` should not be used. For more information see the [Meshtastic docs](https://meshtastic.org/docs/configuration/radio/device/#roles).

**Node Info Broadcast Interval:** `1200` seconds

=== "Radio>Position"
**GPS Mode:** `ENABLED` if present, else `NOT_PRESENT`.  *Note: when connected to iOS or Android, phone GPS can be relayed to the node if the node does not have GPS.*

**Fixed Position:** `FALSE` is often appropriate for fixed nodes, but not required.  This can be set via CLI or sent from phone GPS.

**Broadcast Interval:** `1200` seconds

=== "Radio>LoRa"
**Region:** `US`

**Hop Limit:** `3`

**OK to MQTT:** `TRUE` - this allows packets to be uploaded to MQTT, required to show up on the map if not directly uploading to MQTT.  *Note: this is a request and may not necessarily be honored.*

=== "Radio>Bluetooth"
*If present & desired to be enabled (optional)*

**Enabled:** `TRUE`

**Pairing Mode:** `Random PIN` or `Fixed PIN` (if no screen/ screen visible to public: fixed; else either as desired).

**PIN:** (if fixed) anything but `123456` - remember to change this if using fixed PIN.

=== "Modules>Neighbor Info"
*Please do not enable neighbor info for portable nodes as it makes telemetry difficult to interpret*

**Enabled:** `FALSE`

---

## Get on the Map
=== "Channels>Primary"
**Allow Position Requests:** `TRUE`

**Precise Location:** `FALSE`

**Approximate Location:** Choose a value you are comfortable with.

#### If Enabling MQTT

**Uplink Enabled:** `TRUE`

**Downlink Enabled:** `FALSE`

=== "Modules>MQTT"
Enabling MQTT will guarantee you will appear on the map, otherwise you must have OK to MQTT & position on and connect to a node uplinked to MQTT.

**Enabled:** `TRUE`

**MQTT Server Address:** `mqtt.davekeogh.com` - this server is required to show up on our map.

**Username/Password:** Leave default or go to [the map](https://mqtt.davekeogh.com/) for details.

**Encryption Enabled:** `TRUE`

**JSON Enabled:** `FALSE`

**TLS Enabled:** `FALSE`

**Root Topic:** `msh/US`

**Map Reporting Enabled:** `TRUE`

**Map Report Publish Interval:** Fixed: `3600`, Portable: `300`

**Approximate Location:** Choose a value you are comfortable with.

---

## Add the Puget Mesh Channel
Use [this link](https://meshtastic.org/e/?add=true#CiESEIx68aUDqunRAQuS3a91C60aCFBTLU1lc2ghJQIAAAASDwgBOAFABUgBUB5oAcgGAQ) or QR code to add the channel - be sure to pay attention when adding the channel so you don't replace your current channels.

![PS-Mesh! QR Code](/media/ps-mesh-qr.png)

## Join the Discord
We love chatting on and off of the mesh.  The [Discord](https://discord.gg/ANvUg3AyZt) is also a great place to get help, share pictures, and get ideas for projects.

# Recommend Configuration
Can't find a setting?  Check the [Meshtastic docs](https://meshtastic.org/docs/configuration/) for more info - each page has tabs for iOS, Android, CLI, and Web.

## Fixed Nodes
_If your node will move, please use the portable node configuration_
# [Radio>Device](#tab/device)
__Role:__ usually should be `CLIENT` or `CLIENT_MUTE` or other roles as appropriate by situation. It is rare that `ROUTER` or `REPEATER` are appropriate, so please consult with the group on Discord before doing so.  Adding nodes with these roles can negatively impact the mesh.  The role `ROUTER_CLIENT` (deprecated) should not be used.  For more information see the [Meshtastic docs](https://meshtastic.org/docs/configuration/radio/device/#roles).

__Node Info Broadcast Interval:__ `3600` seconds

# [Radio>Position](#tab/position)
__GPS Mode:__ `ENABLED` if present, else `NOT_PRESENT`.  _Note: when connected to iOS or Android, phone GPS can be relayed to the node if the node does not have GPS._

__Fixed Position:__ `TRUE` is often appropriate for fixed nodes, but not required.  This can be set via CLI or sent from phone GPS.

__Broadcast Interval:__ `3600` seconds

# [Radio>LoRa](#tab/lora)
__Region:__ `US`

__Hop Limit:__ todo - do we have a suggestion?  Meshtastic says usually 3, but some other communities have this higher (e.g. ChicagolandMesh says 7).

__OK to MQTT:__ `TRUE` - this allows packets to be uploaded to MQTT, required to show up on the map if not directly uploading to MQTT.  _Note: this is a request and may not necessarily be honored._

# [Radio>Bluetooth](#tab/bluetooth)
_If present & desired to be enabled (optional)_

__Enabled:__ `TRUE`

__Pairing Mode:__ `Random PIN` or `Fixed PIN` (if no screen/ screen visible to public: fixed; else either as desired).

__PIN:__ (if fixed) anything but `123456` - remember to change this if using fixed PIN.

# [Modules>Neighbor Info](#tab/neighbor)
__Enabled:__ `TRUE`

__Update Interval:__ `3600` seconds

---

## Portable Nodes

# [Radio>Device](#tab/device)
__Role:__ usually should be `CLIENT` or `CLIENT_MUTE` or other roles as appropriate by situation.  `ROUTER`, `REPEATER`, and `ROUTER_CLIENT` should not be used. For more information see the [Meshtastic docs](https://meshtastic.org/docs/configuration/radio/device/#roles).

__Node Info Broadcast Interval:__ `1200` seconds

# [Radio>Position](#tab/position)
__GPS Mode:__ `ENABLED` if present, else `NOT_PRESENT`.  _Note: when connected to iOS or Android, phone GPS can be relayed to the node if the node does not have GPS._

__Fixed Position:__ `FALSE` is often appropriate for fixed nodes, but not required.  This can be set via CLI or sent from phone GPS.

__Broadcast Interval:__ `1200` seconds

# [Radio>LoRa](#tab/lora)
__Region:__ `US`

__Hop Limit:__ todo - do we have a suggestion?  Meshtastic says usually 3, but some other communities have this higher (e.g. ChicagolandMesh says 7).

__OK to MQTT:__ `TRUE` - this allows packets to be uploaded to MQTT, required to show up on the map if not directly uploading to MQTT.  _Note: this is a request and may not necessarily be honored._

# [Radio>Bluetooth](#tab/bluetooth)
_If present & desired to be enabled (optional)_

__Enabled:__ `TRUE`

__Pairing Mode:__ `Random PIN` or `Fixed PIN` (if no screen/ screen visible to public: fixed; else either as desired).

__PIN:__ (if fixed) anything but `123456` - remember to change this if using fixed PIN.

# [Modules>Neighbor Info](#tab/neighbor)
_Please do not enable neighbor info for portable nodes as it makes telemetry difficult to interpret_

__Enabled:__ `FALSE`

---

## Get on the Map
# [Channels>Primary](#tab/primary)
__Allow Position Requests:__ `TRUE`

__Precise Location:__ `FALSE`

__Approximate Location:__ Choose a value you are comfortable with.

#### If Enabling MQTT

__Uplink Enabled:__ `TRUE`

__Downlink Enabled:__ `FALSE`

# [Modules>MQTT](#tab/mqtt)
Enabling MQTT will guarantee you will appear on the map, otherwise you must have OK to MQTT & position on and connect to a node uplinked to MQTT.

__Enabled:__ `TRUE`

__MQTT Server Address:__ `mqtt.davekeogh.com` - this server is required to show up on our map.

__Username/Password:__ Leave default or go to [the map](https://mqtt.davekeogh.com/) for details.

__Encryption Enabled:__ `TRUE`

__JSON Enabled:__ `FALSE`

__TLS Enabled:__ `FALSE`

__Root Topic:__ `msh/US`

__Map Reporting Enabled:__ `TRUE`

__Map Report Publish Interval:__ Fixed: `3600`, Portable: `300`

__Approximate Location:__ Choose a value you are comfortable with.

---

## Add the Puget Mesh Channel
Use [this link](https://meshtastic.org/e/?add=true#CiESEIx68aUDqunRAQuS3a91C60aCFBTLU1lc2ghJQIAAAASDwgBOAFABUgBUB5oAcgGAQ) or QR code to add the channel - be sure to pay attention when adding the channel so you don't replace your current channels.

![PS-Mesh! QR Code](/media/ps-mesh-qr.png)

## Join the Discord
We love chatting on and off of the mesh.  The Discord is also a great place to get help, share pictures, and get ideas for projects.

# Repeater Setup

These are guidelines to help you setup a new Meshcore repeater which will work well within Puget Mesh. Repeaters in Meshcore are encouraged, each enhances the coverage of the mesh.

## Sourcing Your Repeater Parts

^^@Jade's $50 Repeater Parts List (Prices as of 9/19/25)^^

- XIAO nRF52840 + Wio-SX1262 — $14.00 - [Seeed Studio](https://www.seeedstudio.com/)
- Antenna (Linx ANT-916-CW-HW-SMA-ND) — $10.00 [Digi-Key](https://www.digikey.com/)
- RAKwireless Solar Panel with JST 1.5 connector (Large 5.5 x 3.5 inch) SKU 920433 (3 Pack) $11 ($33 divided by 3) - [Rokland](https://store.rokland.com/)
- AITRIP 5PCS Type-C USB 3.7V 4.2V 1A 5W Lithium Li-ion 18650 Battery Charger Board DC-DC Step Up Boost Module TP4056 DIY Kit Parts $1.40 ($7 divided by 5) - [Amazon](https://www.amazon.com/) 
- LeMotech Waterproof Dustproof IP65 ABS Plastic Junction Box Universal Electric Project Enclosure Pale Gray 6.2 x 3.54 x 2.3 inch (158 x 90 x 60 mm) $7 - [Amazon](https://www.amazon.com/)
- MakerFocus 1pcs 3.7V 10000mAh Lithium Polymer Rechargeable Battery $20 - [Amazon](https://www.amazon.com/)

^^@Ded (SalishMesh) has a similar [simple build guide](https://salishmesh.net/how-to/simple-repeater/)^^

## Assembling Your Repeater

Each mesher has their own way of assembling their components. You can find many builds on YouTube. A simple MeshCore or Meshtastic repeater can be built following [@Rootkit Dev's build video](https://www.youtube.com/watch?v=1H6_Da1xRVs).

>NOTE: Your repeater needs to operate within unlicensed power limits (1W or 30 dBm). Modifying repeater setups to broadcast at higher wattages may violate these limits - if you aren't sure, ask before building. Be aware that many nodes include an amplifier, so the tx power setting you use needs to be reduced. See your node's manual to understand how to configure it.

## Locating your Repeater

A repeater with an omnidirectional antenna (which is most of them) needs to have good line of sight to other repeaters. This means getting it up high. On your roof or on a mast that is above the roof or in the yard free in a clear space. For directional antennas you need good line of sight to the other repeater you aim to mesh with.

## Repeater Setup

Once you have [flashed your repeater](https://meshcore.io/flasher) with the web flasher (chromium browser required). The Meshcore documentation explains how to [configure your repeater](https://docs.meshcore.io/faq/#31-q-how-do-you-configure-a-repeater-or-a-room-server) over USB.  The web based config app is at [https://config.meshcore.io/](https://config.meshcore.io/)

Key items for you to get right:

- **Name**: It is helpful if your repeater gives a hint about the location, such as a landmark, neighborhood or cross streets.
- **Location**: Set the Latitude and Longitude in decimal format (47.xxxx, -122.xxxx)
- **Guest and Admin Password**: Use a strong password. Repeaters can be administered over the mesh from the Meshcore app.
- **Advert Interval (minutes)**: 0
- **Flood Advert Interval (hours)**: 47
- **Flood max**: 16 -- adjust according to your liking, default is 64
- **Owner Info**: This is a free-text field, place your email, discord name, or any other identifier to contact you with in case you need to be reached (optional)

- **Radio Settings**: Repeaters and clients use the “USA/Canada (Recommended)” preset.

    Frequency | 910.525 MHz
    -- | --
    Bandwidth | 62.5 kHz
    Spreading Factor | 7
    Coding Rate | 5
    TX Power (dBm)* | 22

*Some hardware options have an external power amplifier which will increase the final transmit power over the limit of 30dBm. The TX Power in the config interface or in the cli does not take this external amplifier into consideration. Common nodes that have an external amplifier are: Station G2, Ikoka 1w/2w, RAK 1w, Heltec V4, etc. Reffer to the documentation of your node to understand how to configure this.

## Advanced Settings

- **Loop Detection**: Moderate
- **Path hash mode**: 3-byte
- **AGC reset interval**: If you notice your node going "deaf" after some time, try setting this value to something greater than 0. The lower the value, the more often the node will reset the AGC. The minimum is `4`.
- **RX Delay and TX Delay**: Nodes that are in very good locations should set these, otherwise the defaults are fine.
- **Multi ACKs**: Enable -- this instructs the repeater to send 2 acks instead of 1, often leading to a better remote admin experience. 

## Remote Management

Before you put your repeater up on a pole where you can't easily reach it, practice remotely managing it with a Meshcore companion device. With your Meshcore companion app open:

1. Go to Contact
2. In the menu, select Add Contact and fill in the form:  
    **Contact Type**: Repeater  
    **Name**: Your Repeater Name  
    **Public Key**: The public key you generated earlier  
3. Save the contact (check mark)  
4. Open the contact in the list
5. Select Remote Management (and wait the seconds..)
6. Put in your admin password and Login

You should now be logged in and able to Get Stats from the menu, or issue console commands. For all the commands see the [CLI Commands](https://docs.meshcore.io/cli_commands/).

## Repeater Testing

You can search for your repeater by name or public key using [MeshExplorer https://analyzer.letsmesh.net/nodes/repeaters](https://analyzer.letsmesh.net/nodes/repeaters)

Using the Config app or managing remotely from a companion deviceissue the advert command on your repeater. If your location is good, your antenna is good and you have other repeaters in range you will see your repeater show up in MeshExplorer and on the Map (assuming you set the location).

Once you see your repeater in MeshExplorer, expand a Recent Advert and look at the Paths and Graph views to see who is receiving your adverts directly and which are also receiving it via the mesh.

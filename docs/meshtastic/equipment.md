# Meshtastic Equipment
The following sections detail our builds and installations around the area. Additionally you will find approximate coverage maps of each node. Use these to help get connected if you are inside the coverage areas (red). PLEASE NOTE: Some nodes are on LongFast, some are on ShortFast, some have radios on both (not bridged). 

### Build Tips:

- I find these ABS 5.9"x 3.9"x 2.8" enclosures (pictures below) are a good size, price, and build quality.
- Butyl tape works well to seal antennas (Don't block/cover any gaskets that your antenna mounts come with). This is very helpful for the gaps on the sides of N-Type through-panel mount connectors.
- I like to use TP4056 modules to charge the batteries. They do need a regulated input but allow for battery charging when the units are in storage (radio disconnected) and at faster rates than the rak wis-block solar connectors. I do usually desolder the charge LED for units with smaller solar panels.
- The 6 Watt "Camera" solar panels have a 5v regulated output. These also come with a mounting pole that is handy.
- I spray my antennas and enclosures with Krylon Clear Triple Glaze Coating spray. This protects the plastics from UV damage (somewhat) but also seals any small holes where the antenna passes through. 
- I used to install switches inside the enclosures but now I prefer using the battery connector as a switch. I still use external (waterproof) switches when the enclosure requires a tool to open it. The switch goes between the radio and all power sources.
- All enclosures include a weep hole on the bottom. This allows pressure equalization as well as somewhere for water to go.
- Lubricant on all enclosure gaskets. This prevents the gasket material from drying out so quickly, but also seals better. I have been using Vaseline which is not the best for rubber-based gaskets. 
- Clearly label power. It should be easy to walk someone through powering the unit down over the phone, or ideally intuitively for them. Also label the unit so it is clear what it is, and I like to include contact information inside.
- After trying several antenna types. I prefer the Alfa 5dbi Omni antennas. They are a good price point, they come with an N Type male connector which connects directly to through-mount antenna connectors. They are short, which is good for wind load and stresses on the case. They work well as a good wide-beam omnidirectional antenna for general purpose locations.

---
## Paine East (Everett)

Node Name | Radio | Antenna | Battery | Solar | Modem Preset | Slot | Rebroadcast Mode
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: 
PugetMesh.org - Paine East | rak4631 | Alfa 5dbi Omni | 1x lipo (5ah) | 10 watt (shared) | {==LONG_FAST==} | 20 | CORE_PORTNUMS_ONLY
(OFFLINE) | rak4631 | Alfa 5dbi Omni | 1x lipo (5ah) | 10 watt (shared) | N/A | N/A | N/A

![Paine East Node](/media/PugetMesh_PaineEast.jpg)

Click to enlarge and see the larger coverage map.
[![Capitol Hill Coverage Map](/media/PaineEast_sml.png)](https://www.heywhatsthat.com/?view=QAXF4HU7)

---
## Clearview
Node Name | Radio | Antenna | Battery | Solar | Modem Preset | Slot | Rebroadcast Mode
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: 
PugetMesh.org - Clearview | rak4631 | Alfa 5dbi Omni | 2x 18650 (3ah/ea) | 6 watt | {==LONG_FAST==}| 20 | CORE_PORTNUMS_ONLY

Host asked not to be named. Location shared below is approximate.

Click to enlarge and see the larger approximate coverage map.
[![Clearview Coverage Map](/media/ClearviewNodeMap.png)](https://www.heywhatsthat.com/?view=BAXN1N63)

---
## North City, Shoreline

Node Name | Radio | Antenna | Battery | Solar | Modem Preset | Slot | Rebroadcast Mode
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: 
PugetMesh.org - North City | rak4631 | Alfa 5dbi Omni | 1x 18650 (3ah) | 6 watt | {==LONG_FAST==} | 20| CORE_PORTNUMS_ONLY

Click to enlarge and see the larger coverage map.
[![North City Node Coverage Map](/media/NorthCity_sml.png)](/media/NorthCity_big.png)

---
## Firestation 61 (Shoreline ACS, Shoreline)

Node Name | Radio | Antenna | Battery | Solar | Modem Preset | Slot | Rebroadcast Mode
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: 
Shoreline ACS | rak4631 | Alfa 5dbi Omni | 2x 18650 (3ah/ea) | 2 watt | {==LONG_FAST==} | 20 | ALL

<!---![Shoreline ACS Meshtastic Node](/media/ShorelineACS_MeshtasticNode.png)--->

Click to enlarge and see the larger coverage map.
[![Shoreline ACS Node Coverage Map](/media/Firestation61_sml.png)](https://www.heywhatsthat.com/?view=X2SS81R7)

---
## Maple Leaf Apartments (Seattle)

Node Name | Radio | Antenna | Battery | Solar | Modem Preset | Slot | Rebroadcast Mode
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: 
PugetMesh.org - Maple Leaf Apartments | rak4631 | Alfa 5dbi Omni | 1x 18650 (3ah) | 6 watt | {==LONG_FAST==} | 20 | CORE_PORTNUMS_ONLY

![Puget Mesh Node Version 3](/media/PugetMesh_NodeV3.png)
[![Puget Mesh Maple Leaf Meshtastic Node](/media/MLA_Node.jpg)](/media/MLA_Node.jpg)

Click to enlarge and see the larger coverage map.
[![Maple Leaf Node Coverage Map](/media/MapleLeaf_sml.png)](https://www.heywhatsthat.com/?view=FGCQDXDC)

---
## Capitol Hill (Seattle)

Node Name | Radio | Antenna | Battery | Solar | Modem Preset | Slot | Rebroadcast Mode
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: 
PugetMesh.org - Capitol Hill | rak4631 | Alfa 5dbi Omni | 1x lipo (5ah) | 10 watt (shared) | {==LONG_FAST==} | 20 | CORE_PORTNUMS_ONLY
PugetMesh.org - Capitol Hill | rak4631 | Alfa 5dbi Omni | 1x lipo (5ah) | 10 watt (shared) | {==MEDIUM_FAST==} | (907.845 Freq Override) | CORE_PORTNUMS_ONLY

Click to enlarge and see the larger coverage map.
[![Capitol Hill  Coverage Map](/media/CapitolHill_sml.jpg)](https://www.heywhatsthat.com/?view=T29861XC)

---
## Beacon Hill (Seattle)

Node Name | Radio | Antenna | Battery | Solar | Modem Preset | Slot | Rebroadcast Mode
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: 
PugetMesh.org - Beacon Hill| rak4631 | Alfa 5dbi Omni | 1x 18650 (3ah) | 6 watt | {==LONG_FAST==} | 20 | CORE_PORTNUMS_ONLY

Click to enlarge and see the larger coverage map.
[![Beacon Hill  Coverage Map](/media/BeaconHill_sml.jpg)](https://www.heywhatsthat.com/?view=CD5GQ9BW)

---
## Skyway Radio

Node Name | Radio | Antenna | Battery | Solar | Modem Preset | Slot | Rebroadcast Mode
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: 
PugetMesh.org - Skyway Radio | rak4631 | Alfa 5dbi Omni | 2x 18650 (3ah/each) | 10 watt | {==MEDIUM_FAST==} | (907.845 Freq Override) | CORE_PORTNUMS_ONLY

Click to enlarge and see the larger coverage map.
[![Skyway Radio Coverage Map](/media/SkywayRadioNodeMap.png)](https://www.heywhatsthat.com/?view=DS4BGWQM)
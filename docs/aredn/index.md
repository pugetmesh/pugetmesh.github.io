# AREDN

![AREDN Mesh Logo](/media/AREDN-Logo.png){ align=left }

The [Amateur Radio Emergency Data Network](https://www.arednmesh.org/) (AREDN®) is high-speed IP mesh networking for amateur radio operators. It runs on commercial and consumer WiFi hardware in place of the factory firmware, handling the routing, addressing, and link management needed to build a self-configuring data network with no internet and a focus on Emergency Communications (EmComm).

While it is possible to legally use AREDN on some bands without a ham radio license, the frequencies and power levels used in the Puget Sound region **do require a license**.

Unlike the LoRa networks [MeshCore](/meshcore/) and [Meshtastic](/meshtastic/)—which are optimized for short text messages at very low power—AREDN carries real IP traffic at megabit speeds: IP phones, [Winlink](https://www.winlink.org/), chat, file transfer, cameras, and more.

In this section:

- **[Getting Started](getting_started.md)** — supported hardware, flashing, and our local band/channel settings
- **[Equipment](equipment.md)** — device families and what works well in our region
- **[HaLow (802.11ah)](halow.md)** — emerging 900 MHz long-range links, now under local test
- **[Coverage & Map](map.md)** — where the mesh reaches today, and how to put your node on the map

## Why AREDN?

At a high level, an Amateur Radio Emergency Data Network is simply another tool for your EmComm toolbox. As an operator involved in emergency communication you already have RF resources you use regularly; AREDN® is one more to have available when a served agency needs a genuine data network—not just voice or short text.

## Uses

There are two primary ways to build an AREDN mesh:

1. **Proactive** — built before it is needed
2. **Reactive** — deployed when it is needed

### Proactive

Proactive mesh networks are set up today, ahead of any emergency need. An example is the established network in West Seattle, visible on the [AREDN Worldmap](https://worldmap.arednmesh.org/#6.66/47.5395/-122.3973). These networks can grow large, linking sites over long distances with highly directional antennas.

### Reactive

These networks can do everything a proactive network can, but are stood up as needed rather than maintained over time. Assume that natural disasters will impact traditional communications (cell tower failures, last-mile or backbone internet outages)—but they will also impact proactive mesh networks: directional antennas knocked out of alignment, nodes lost to power problems, new line-of-sight obstructions, and so on.

For example, an AREDN network could link an emergency shelter to an incident command post. IP phones, messaging services like Winlink Express, or file-sharing services connect to the mesh, enabling rapid information transfer between the sites. After the incident, the equipment packs away for its next reactive deployment.

Practice both: build out a mesh ahead of an incident, and stand up impromptu deployments in new and unique locations.

## Other Local AREDN Groups

- [MBARC Digital Group](https://mbarc.groups.io/g/digital)
- [http://www.clallammesh.k7wwp.net/](http://www.clallammesh.k7wwp.net/)
- [Chilliwack ARC](https://www.chwkarc.ca/)
- [CECA](http://va7eca.ca/)
- [https://w7aw.org/](https://w7aw.org/)
- [https://groups.io/g/nwmesh](https://groups.io/g/nwmesh)
